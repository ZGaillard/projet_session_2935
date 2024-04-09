import ttkbootstrap as ttk


def new_primary_button(container, text, command, width=18):
    button = ttk.Button(
        container,
        text=text,
        command=command,
        style="primary.TButton",
        width=width
    )
    return button


def new_secondary_button(container, text, command):
    button = ttk.Button(
        container,
        text=text,
        command=command,
        style="danger.TButton",
        width=18

    )
    return button
