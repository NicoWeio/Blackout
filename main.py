#!/usr/bin/python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

class BlackoutApp(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)

        screen = Gdk.Screen.get_default()
        provider = Gtk.CssProvider()
        style_context = Gtk.StyleContext()
        style_context.add_provider_for_screen(
            screen, provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )
        css = b"""
        entry {
            background: black;
        }
        """
        provider.load_from_data(css)

        self.entry = Gtk.Entry()
        self.add(self.entry)
        self.connect("destroy", Gtk.main_quit)
        self.entry.connect("changed", self.on_quit_requested)
        self.show_all()

    def on_quit_requested(foo,bar):
        Gtk.main_quit()

def fullscreen_at_monitor(window, n):
    display = Gdk.Display.get_default()
    monitor = Gdk.Display.get_monitor(display, n)
    geometry = monitor.get_geometry()
    window.move(geometry.x, geometry.y)
    window.fullscreen()

def get_active_monitor_geometry():
    display = Gdk.Display.get_default()
    seat = Gdk.Display.get_default_seat(display)
    pointer = seat.get_pointer()
    x = pointer.get_position().x
    y = pointer.get_position().y
    print(f"cursor is at {x},{y}")

    monitor = Gdk.Display.get_monitor_at_point(display, x, y).get_geometry()
    return monitor


if __name__ == '__main__':
    display = Gdk.Display.get_default()
    num_monitors = Gdk.Display.get_n_monitors(display)
    print(f"{num_monitors} monitors detected")
    active_monitor_geometry = get_active_monitor_geometry()

    for i in range(0, num_monitors):
        monitor = Gdk.Display.get_monitor(display, i)
        if active_monitor_geometry.equal(monitor.get_geometry()):
            print(f"Cursor is currently on monitor {i} – won't cover")
        else:
            print(f"Monitor {i} will be covered")
            win = BlackoutApp()
            fullscreen_at_monitor(win, i)

    Gtk.main()
