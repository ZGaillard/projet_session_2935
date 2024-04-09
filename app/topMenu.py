import ttkbootstrap as ttk


class TopMenu(ttk.Menu):

    def __init__(self, parent):
        ttk.Menu.__init__(self, parent)
        self.initMenu(parent)

    def initMenu(self, parent):
        # sub menu new
        sub_menu_new = ttk.Menu(self)
        from newElemMenu import NewMovieMenu, NewTheaterPlayMenu, \
            NewArtistMenu, NewCastingMenu
        self.new_menu_command(sub_menu_new, "New movie",
                              lambda: parent.switch_frame(NewMovieMenu))
        self.new_menu_command(sub_menu_new, "New theater play",
                              lambda: parent.switch_frame(NewTheaterPlayMenu))
        self.new_menu_command(sub_menu_new, "New artist",
                              lambda: parent.switch_frame(NewArtistMenu))
        self.new_menu_command(sub_menu_new, "New casting",
                              lambda: parent.switch_frame(NewCastingMenu))

        # sub menu search
        sub_menu_search = ttk.Menu(self)
        from searchMenu import SearchMovieMenu, SearchTheaterPlayMenu, \
            SearchArtistMenu, SearchCastingMenu
        self.new_menu_command(sub_menu_search, "Search movie",
                              lambda: parent.switch_frame(SearchMovieMenu))
        self.new_menu_command(sub_menu_search, "Search theater play",
                              lambda: parent.switch_frame(
                                  SearchTheaterPlayMenu))
        self.new_menu_command(sub_menu_search, "Search artist",
                              lambda: parent.switch_frame(SearchArtistMenu))
        self.new_menu_command(sub_menu_search, "Search casting",
                              lambda: parent.switch_frame(SearchCastingMenu))

        self.add_cascade(label="New", menu=sub_menu_new)
        self.add_cascade(label="Search", menu=sub_menu_search)
        self.add_separator()
        self.new_menu_command(self, "Exit", self.onExit)

    @staticmethod
    def new_menu_command(menu, text, command):
        menu.add_command(label=text, command=command)

    def onExit(self):
        self.quit()
