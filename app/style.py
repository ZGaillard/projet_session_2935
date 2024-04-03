import tkinter as tk
import ttkbootstrap as ttk

from ttkbootstrap.constants import *


def new_primary_button(container, text, command):
    button = ttk.Button(
        container,
        text=text,
        command=command,
        style="primary.TButton",
        width=18
    )
    return button


def new_primary_butt(container, text, command):
    button = ttk.Button(
        container,
        text=text,
        command=command,
        style="danger.TButton",
        width=18

    )
    return button
