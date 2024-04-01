from tkinter import *

from app.style import STYLE_CONFIG, create_button
from app.topMenu import TopMenu


class NewMenu:
    pass


class MainMenu(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.menu = None
        self.parent = parent
        self.initUI()
        self.initFrame()

    def initUI(self):
        self.parent.title("Main Menu")
        self.parent.geometry("1600x900")
        self.configure(background=STYLE_CONFIG["background"])
        self.pack(fill=BOTH, expand=True)

        self.menu = TopMenu(self.parent)
        self.parent.config(menu=self.menu)

    def initFrame(self):
        # title
        title = Label(self, text="Welcome to Casting Manager", background=STYLE_CONFIG["background"])
        title.config(font=("Arial", 40))
        title.pack(pady=60)

        # image from : https://www.vecteezy.com/vector-art/620081-film-logo-and-symbols-vector-template
        image = PhotoImage(file="/home/zakary/Documents/uni/h24/2935/projet_session/app/ressources/logo.png")
        label = Label(self, image=image)
        label.image = image
        label.pack(pady=30)

        # separator
        separator = Frame(self, height=3, bd=0, relief=SUNKEN)
        separator.pack(fill=X, pady=10)

        # button container
        button_container = Frame(self, background=STYLE_CONFIG["background"])
        button_container.pack(pady=20)

        # button to search
        from app.searchMenu import SearchMenu
        search_button = create_button(button_container, "Search", lambda: self.parent.switch_frame(SearchMenu))
        search_button.pack(side=LEFT, padx=10)

        # button to new
        new_button = create_button(button_container, "New", lambda: self.parent.switch_frame(NewMenu))
        new_button.pack(side=LEFT, padx=10)

        # separator
        separator = Frame(self, height=3, bd=0, relief=SUNKEN)
        separator.pack(fill=X, pady=10)

        # button exit
        exit_button = create_button(self, "Exit", self.onExit)
        exit_button.pack(pady=20)

    def onExit(self):
        self.quit()

    def destroy(self):
        Frame.destroy(self)
