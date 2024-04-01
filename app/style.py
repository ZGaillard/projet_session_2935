from tkinter import Button

STYLE_CONFIG = {
    "background": "white",
    "font": ("Arial", 20),
    "small_font": ("Arial", 15),
    "big_font": ("Arial", 40),
    "button_background": "blue",
    "button_hover": "#30D0FF",
    "button_foreground": "white",
}


def create_button(container, text, command):
    button = Button(
        container,
        text=text,
        command=command,
        background=STYLE_CONFIG["button_background"],
        activebackground=STYLE_CONFIG["button_hover"],
        foreground=STYLE_CONFIG["button_foreground"],
        font=STYLE_CONFIG["font"],
        width=20
    )
    return button
