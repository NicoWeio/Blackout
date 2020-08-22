A small and dirty script utilizing GTK3 (PyGObject) to make all screens black(ish) except the one where the cursor is. Inspired by an [xplayer](https://github.com/linuxmint/xplayer) feature. Hacked together in a few hours (i.e. I have no idea what I'm doing).

## Usage

-   I'd suggest assigning a keyboard shortcut to the (executable) Python file.
-   Put your cursor on the screen you want to focus on.
-   Execute the keyboard shortcut of your choice.
-   Then you can binge your favourite content (or do something productive) without distraction from your other screens.
-   Type something in one of the black windows this script opens to close all of them.

## Alternatives

You can achieve similar results by using `xrandr --output <name> --brightness 0`. Unfortunately, on my setup the brightness resets after a few seconds. If you don't mind active windows being moved to another screen, you could also _disable_ the screen completely: `xrandr --output <name> --off`.
