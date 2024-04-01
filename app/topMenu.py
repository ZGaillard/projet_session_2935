from tkinter import Menu


from app.menuFunctions import onNewMovie, onNewTheaterPlay, onNewActor, onNewCasting, onSearchMovie, onSearchTheaterPlay, onSearchActor, onSearchCasting

from app.style import STYLE_CONFIG


class TopMenu(Menu):

    def __init__(self, parent):
        Menu.__init__(self, parent)
        self.initMenu(parent)

    def initMenu(self, parent):
        self.config(background=STYLE_CONFIG["background"])
        file_menu = Menu(self, background=STYLE_CONFIG["background"])

        # sub menu new
        sub_menu_new = Menu(file_menu, background=STYLE_CONFIG["background"])
        self.new_menu_command(sub_menu_new, "New movie", onNewMovie)
        self.new_menu_command(sub_menu_new, "New theater play", onNewTheaterPlay)
        self.new_menu_command(sub_menu_new, "New actor", onNewActor)
        self.new_menu_command(sub_menu_new, "New casting", onNewCasting)

        # sub menu search
        sub_menu_search = Menu(file_menu, background=STYLE_CONFIG["background"])
        self.new_menu_command(sub_menu_search, "Search movie", onSearchMovie)
        self.new_menu_command(sub_menu_search, "Search theater play", onSearchTheaterPlay)
        self.new_menu_command(sub_menu_search, "Search actor", onSearchActor)
        self.new_menu_command(sub_menu_search, "Search casting", onSearchCasting)

        file_menu.add_cascade(label="New", menu=sub_menu_new, font=STYLE_CONFIG["font"])
        file_menu.add_cascade(label="Search", menu=sub_menu_search, font=STYLE_CONFIG["font"])
        file_menu.add_separator()
        self.new_menu_command(file_menu, "Exit", self.onExit)

        self.add_cascade(label="Menu", menu=file_menu, font=STYLE_CONFIG["font"])

    @staticmethod
    def new_menu_command(menu, text, command):
        menu.add_command(label=text, command=command, font=STYLE_CONFIG["font"])

    def onExit(self):
        self.quit()