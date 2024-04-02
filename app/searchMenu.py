from tkinter import *
from tkinter.ttk import Treeview

from app.style import STYLE_CONFIG, create_button


class SearchMenu(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
        self.initFrame()

    def initUI(self):
        self.parent.title("Search Menu")
        self.parent.geometry("1600x900")
        self.configure(background=STYLE_CONFIG["background"])
        self.pack(fill=BOTH, expand=True)

    def initFrame(self):
        # title
        title = Label(self, text="Search Menu",
                      background=STYLE_CONFIG["background"])
        title.config(font=("Arial", 40))
        title.pack(pady=60)

        # button for each search
        button_container_1 = Frame(self, background=STYLE_CONFIG["background"])
        button_container_1.pack(pady=20)

        s_movie_button = create_button(button_container_1, "Search movie",
                                       lambda: self.parent.switch_frame(
                                           SearchMovieMenu))
        s_movie_button.pack(side=LEFT, padx=10)
        s_theater_play_button = create_button(button_container_1,
                                              "Search theater play",
                                              lambda: self.parent.switch_frame(
                                                  SearchTheaterPlayMenu))
        s_theater_play_button.pack(side=LEFT, padx=10)

        button_container_2 = Frame(self, background=STYLE_CONFIG["background"])
        button_container_2.pack(pady=20)

        s_actor_button = create_button(button_container_2, "Search actor",
                                       lambda: self.parent.switch_frame(
                                           SearchActorMenu))
        s_actor_button.pack(side=LEFT, padx=10)
        s_casting_button = create_button(button_container_2, "Search casting",
                                         lambda: self.parent.switch_frame(
                                             SearchCastingMenu))
        s_casting_button.pack(side=LEFT, padx=10)

        separator = Frame(self, height=3, bd=0, relief=SUNKEN)
        separator.pack(fill=X, pady=10)

        # button to go back to main menu
        from app.mainMenu import MainMenu
        back_button = create_button(self, "Back",
                                    lambda: self.parent.switch_frame(MainMenu))
        back_button.pack(pady=20)

    def destroy(self):
        Frame.destroy(self)


class SearchableTable(Treeview):
    def __init__(self, parent, data):

        self.parent = parent
        self.data = data.get_tuples()
        self.column_names = data.get_column_names()
        Treeview.__init__(self, parent, columns=self.column_names,
                          show="headings")

        self.column("#0", width=270, minwidth=270, stretch=YES)
        for column_name in self.column_names:
            self.column(column_name, width=150, minwidth=150, stretch=YES)
            self.heading(column_name, text=column_name, anchor=W)

        # insert data
        for row in self.data:
            self.insert("", "end", values=row)


class SearchMovieMenu(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
        self.initFrame()

    def initUI(self):
        self.parent.title("Search Movie Menu")
        self.parent.geometry("1600x900")
        self.configure(background=STYLE_CONFIG["background"])
        self.pack(fill=BOTH, expand=True)

    def initFrame(self):
        # title
        title = Label(self, text="Search Movie Menu",
                      background=STYLE_CONFIG["background"])
        title.config(font=("Arial", 40))
        title.pack(pady=60)

        # Search bar
        search_bar = Entry(self, width=50)
        search_bar.pack(pady=20)

        # list of movies
        from app.data import movies
        movies_table = SearchableTable(self, movies)
        movies_table.pack(pady=20)

        separator = Frame(self, height=3, bd=0, relief=SUNKEN)
        separator.pack(fill=X, pady=10)

        # button to go back to main menu
        from app.mainMenu import MainMenu
        back_button = create_button(
            self, "Back",
            lambda: self.parent.switch_frame(MainMenu)
        )
        back_button.pack(pady=20)

    def destroy(self):
        Frame.destroy(self)


class SearchTheaterPlayMenu(Frame):
    pass


class SearchActorMenu(Frame):
    pass


class SearchCastingMenu(Frame):
    pass
