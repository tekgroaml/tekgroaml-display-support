#!/usr/bin/env python3
"""Application-only cut-panel compensation; never writes EDID or input settings."""
import argparse
import os
from pathlib import Path
import signal
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--screen', type=int, choices=(1, 2), required=True)
    parser.add_argument('--left', type=int, default=60, help='Visible window start in input pixels')
    parser.add_argument('--width', type=int, default=360, help='Logical/visible canvas width')
    parser.add_argument('--raw-touch', action='store_true', help='Compare without touch scaling')
    args = parser.parse_args()
    if os.getuid() == 0:
        parser.error('Run as the logged-in desktop user, without sudo.')
    if args.left < 0 or args.width <= 0 or args.left + args.width > 420:
        parser.error('Visible window must fit inside the 420-pixel input.')
    installed = Path('/opt/pi-setting/src')
    if not installed.is_dir():
        parser.error('Install TEKGROAML Pi Display Tools 2.3.2+ and its GTK dependencies first.')
    sys.path.insert(0, str(installed))
    UserError = RuntimeError
    try:
        from pi_setting.common import UserError, desktop_env
        _, env = desktop_env()
        for key in ('XDG_RUNTIME_DIR', 'WAYLAND_DISPLAY', 'GDK_BACKEND',
                    'DBUS_SESSION_BUS_ADDRESS'):
            os.environ[key] = env[key]
        from pi_setting.color_worker import TestWindow, monitor_for, Gdk, Gtk, GLib
        from pi_setting.outputs import outputs
        from pi_setting.touch import TouchTest
        connector = f'HDMI-A-{args.screen}'
        output = outputs().get(connector)
        if not output or not output['enabled']:
            raise UserError(f'{connector} is not enabled.')
        mode = next((m for m in output['modes'] if m['current']), None)
        if not mode or (mode['width'], mode['height']) != (420, 960):
            raise UserError('Requires an existing 420x960 mode; this demo never changes timing.')
        if output['scale'] != 1 or output['transform'] != 'normal':
            raise UserError('Requires scale 1 and normal transform; no automatic calibration.')
        if len(outputs()) > 1:
            print('Use only the measured sample; identify the selected connector and USB pair.')
        # Confirm the installed version provides shape-aware touch state before opening a window.
        TouchTest('rect').geometry(args.width, 960)
        monitor = monitor_for(Gdk.Display.get_default(), output)

        class CutWindow(TestWindow):
            def draw_touch(self, context, width, height):
                context.set_source_rgb(0, 0, 0)
                context.paint()
                if (width, height) != (420, 960):
                    print('Window geometry changed; close and recheck output before restarting.', flush=True)
                    GLib.idle_add(Gtk.main_quit)
                    return False
                context.save()
                context.rectangle(args.left, 0, args.width, height)
                context.clip()
                context.translate(args.left, 0)
                super().draw_touch(context, args.width, height)
                context.set_source_rgb(1, 1, 1)
                context.set_line_width(2)
                context.rectangle(1, 1, args.width-2, height-2)
                context.stroke()
                context.restore()
                return False

            def interact(self, area, kind, sequence, x, y, source):
                # Input x is an uncalibrated coordinate spanning the full 420-wide window.
                # State uses logical canvas pixels; drawing adds the visible-window offset.
                local_x = x-args.left if args.raw_touch else x*args.width/420
                self.touch.event(kind, sequence, local_x, y, args.width, 960, source)
                if kind == 'begin':
                    print(f'raw=({x:.2f},{y:.2f}) canvas=({local_x:.2f},{y:.2f}) '
                          f'targets={len(self.touch.hits)}/5', flush=True)
                area.queue_draw()

        window = CutWindow(monitor, args.screen-1, output, {'action': 'touch', 'shape': 'rect'})
        close_handler = window.connect('destroy', Gtk.main_quit)
        GLib.unix_signal_add(GLib.PRIORITY_DEFAULT, signal.SIGTERM, Gtk.main_quit)
        GLib.unix_signal_add(GLib.PRIORITY_DEFAULT, signal.SIGINT, Gtk.main_quit)
        print(f'{connector}: HDMI 420x960 at {mode["refresh"]:.6f}Hz; '
              f'visible x={args.left}..{args.left+args.width-1}; '
              f'touch correction={not args.raw_touch}. Ctrl+C to exit.', flush=True)
        Gtk.main()
        window.disconnect(close_handler)
        window.destroy()
        return 0
    except (ImportError, OSError, ValueError, TypeError, UserError) as error:
        print(f'cut-panel demo: {error}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
