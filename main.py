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
        self.fullscreen()
        self.show_all()
        Gtk.main()

    def on_open_clicked(x,y):
        Gtk.main_quit()

if __name__ == '__main__':
    win = CompletionApp()
    # win.fullscreen()
