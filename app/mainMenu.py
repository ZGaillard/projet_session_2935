from tkinter import *
from tkinter import ttk

from app.newElemMenu import NewElemMenu as NewMenu
from app.style import new_primary_button, new_primary_butt
from app.topMenu import TopMenu


class MainMenu(ttk.Frame):

    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.menu = None
        self.parent = parent
        self.initUI()
        self.initFrame()

    def initUI(self):
        self.parent.title("Main Menu")

        self.pack(fill=BOTH, expand=True)

        self.menu = TopMenu(self.parent)
        self.parent.config(menu=self.menu)

    def initFrame(self):
        # title
        title = ttk.Label(self, text="Welcome to Casting Manager")
        title.config(font=("Arial", 40))
        title.pack(pady=60)

        # image from : https://www.vecteezy.com/vector-art/620081-film-logo-and-symbols-vector-template
        image = PhotoImage(
            file="app/ressources/logo.png")
        label = Label(self, image=image)
        label.image = image
        label.pack(pady=30)

        # separator
        separator = ttk.Frame(self, height=3, relief=SUNKEN)
        separator.pack(fill=X, pady=10)

        # button container
        button_container = ttk.Frame(self)
        button_container.pack(pady=20)

        # button to search
        from app.searchMenu import SearchMenu
        search_button = new_primary_button(button_container, "Search",
                                           lambda: self.parent.switch_frame(
                                          SearchMenu))
        search_button.pack(side=LEFT, padx=10)

        # button to new
        new_button = new_primary_button(button_container, "New",
                                        lambda: self.parent.switch_frame(NewMenu))
        new_button.pack(side=LEFT, padx=10)

        # separator
        separator = ttk.Frame(self, height=3, relief=SUNKEN)
        separator.pack(fill=X, pady=10)

        # button exit
        exit_button = new_primary_butt(self, "Exit", self.onExit)
        exit_button.pack(pady=20)

    def onExit(self):
        self.quit()

    def destroy(self):
        ttk.Frame.destroy(self)
