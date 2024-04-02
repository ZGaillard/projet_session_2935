from tkinter import Menu

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
        from app.newElemMenu import NewMovieMenu, NewTheaterPlayMenu, \
            NewActorMenu, NewCastingMenu
        self.new_menu_command(sub_menu_new, "New movie",
                              lambda: parent.switch_frame(NewMovieMenu))
        self.new_menu_command(sub_menu_new, "New theater play",
                              lambda: parent.switch_frame(NewTheaterPlayMenu))
        self.new_menu_command(sub_menu_new, "New actor",
                              lambda: parent.switch_frame(NewActorMenu))
        self.new_menu_command(sub_menu_new, "New casting",
                              lambda: parent.switch_frame(NewCastingMenu))

        # sub menu search
        sub_menu_search = Menu(file_menu, background=STYLE_CONFIG["background"])
        from app.searchMenu import SearchMovieMenu, SearchTheaterPlayMenu, \
            SearchActorMenu, SearchCastingMenu
        self.new_menu_command(sub_menu_search, "Search movie",
                              lambda: parent.switch_frame(SearchMovieMenu))
        self.new_menu_command(sub_menu_search, "Search theater play",
                              lambda: parent.switch_frame(
                                  SearchTheaterPlayMenu))
        self.new_menu_command(sub_menu_search, "Search actor",
                              lambda: parent.switch_frame(SearchActorMenu))
        self.new_menu_command(sub_menu_search, "Search casting",
                              lambda: parent.switch_frame(SearchCastingMenu))

        file_menu.add_cascade(label="New", menu=sub_menu_new,
                              font=STYLE_CONFIG["font"])
        file_menu.add_cascade(label="Search", menu=sub_menu_search,
                              font=STYLE_CONFIG["font"])
        file_menu.add_separator()
        self.new_menu_command(file_menu, "Exit", self.onExit)

        self.add_cascade(label="Menu", menu=file_menu,
                         font=STYLE_CONFIG["font"])

    @staticmethod
    def new_menu_command(menu, text, command):
        menu.add_command(label=text, command=command, font=STYLE_CONFIG["font"])

    def onExit(self):
        self.quit()
