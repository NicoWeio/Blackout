#!/usr/bin/python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

class CompletionApp(Gtk.Window):
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
        self.entry.set_name("myentry")
        self.add(self.entry)
        self.connect("destroy", Gtk.main_quit)
        self.entry.connect("changed", self.on_open_clicked)
        self.show_all()


    def on_open_clicked(foo,bar):
        Gtk.main_quit()

def fullscreen_at_monitor(window, n):
    display = Gdk.Display.get_default()
    monitor = Gdk.Display.get_monitor(display, n)
    geometry = monitor.get_geometry()
    x = geometry.x
    y = geometry.y
    window.move(x,y)
    window.fullscreen()


if __name__ == '__main__':
    win = CompletionApp()
    fullscreen_at_monitor(win, 2)
    win2 = CompletionApp()
    fullscreen_at_monitor(win2, 1)

    Gtk.main()
