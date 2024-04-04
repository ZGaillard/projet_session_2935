from tkinter import *

import ttkbootstrap as ttk

from style import new_primary_button


class SearchMenu(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)

        self.parent = parent
        self.parent.title("Search Menu")
        self.pack(fill=BOTH, expand=True)

        self.initFrame()

    def initFrame(self):
        # title
        title = ttk.Label(self, text="Search Menu")
        title.config(font=("Arial", 40))
        title.pack(pady=60)

        # button for each search
        button_container_1 = Frame(self)
        button_container_1.pack(pady=20)

        s_movie_button = new_primary_button(
            button_container_1,
            "Search movie",
            lambda: self.parent.switch_frame(SearchMovieMenu))
        s_movie_button.pack(side=LEFT, padx=10)
        s_theater_play_button = new_primary_button(
            button_container_1,
            "Search theater play",
            lambda:
            self.parent.switch_frame(SearchTheaterPlayMenu))
        s_theater_play_button.pack(side=LEFT, padx=10)

        button_container_2 = Frame(self)
        button_container_2.pack(pady=20)

        s_artist_button = new_primary_button(
            button_container_2,
            "Search artist",
            lambda: self.parent.switch_frame(SearchArtistMenu))
        s_artist_button.pack(side=LEFT, padx=10)
        s_casting_button = new_primary_button(
            button_container_2,
            "Search casting",
            lambda: self.parent.switch_frame(SearchCastingMenu))
        s_casting_button.pack(side=LEFT, padx=10)

        separator = Frame(self, height=3, bd=0, relief=SUNKEN)
        separator.pack(fill=X, pady=10)

        # button to go back to main menu
        from mainMenu import MainMenu
        back_button = new_primary_button(
            self, "Back",
            lambda: self.parent.switch_frame(MainMenu)
        )
        back_button.pack(pady=20)

    def destroy(self):
        Frame.destroy(self)


class SearchableTable(ttk.Treeview):

    def __init__(self, parent, data):

        # Search bar and combobox for column selection
        search_bar_container = Frame(parent)
        search_bar_container.pack(pady=20)

        self.search_text = StringVar()
        search_bar = ttk.Entry(
            search_bar_container,
            textvariable=self.search_text
        )
        search_bar.pack(side=LEFT, padx=10)

        self.search_combobox_value = StringVar()
        self.search_combobox = ttk.Combobox(
            search_bar_container,
            textvariable=self.search_combobox_value,
            values=data.get_column_names(),
            state='readonly', width=10
        )
        self.search_combobox.current(0)
        self.search_combobox.pack(side=LEFT, padx=10)

        self.search_text.trace(
            "w",
            lambda *args: self.search()
        )

        self.search_combobox.bind(
            "<<ComboboxSelected>>",
            lambda *args: self.search()
        )

        self.parent = parent
        self.data = data.get_tuples()

        self.column_names = data.get_column_names()
        ttk.Treeview.__init__(
            self, parent,
            columns=self.column_names,
            show="headings"
        )

        # determine the width of the columns based on the data
        for i, column_name in enumerate(self.column_names):
            mean_width = sum(
                len(str(row[i + 1])) for row in self.data
            ) // len(self.data)
            self.column(column_name, width=mean_width * 24,
                        minwidth=100, stretch=YES
                        )
            self.heading(column_name, text=column_name, anchor=W)

        # insert data (skip the first column which is the id)
        for row in self.data:
            visible_row = row[1:]
            self.insert("", "end", values=visible_row)

    def search(self):
        self.reset()
        search_text = self.search_text.get().lower()
        search_column = self.search_combobox.get()
        search_index = self.column_names.index(search_column)
        for row in self.data:
            visible_row = row[1:]
            if search_text in str(visible_row[search_index]).lower():
                self.insert("", "end", values=visible_row)

    def reset(self):
        x = self.get_children()
        for item in x:
            self.delete(item)


class SearchMovieMenu(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.parent.title("Search Movie Menu")
        self.pack(fill=BOTH, expand=True)

        title = ttk.Label(self, text="Search Movie Menu", )
        title.config(font=("Arial", 20))
        title.pack(pady=40)

        from data import movies
        movies_table = SearchableTable(self, movies)
        movies_table.pack(pady=20)

        separator = Frame(self, height=3, bd=0, relief=SUNKEN)
        separator.pack(fill=X, pady=10)

        back_button = new_primary_button(
            self, "Back",
            lambda: self.parent.switch_frame(SearchMenu)
        )
        back_button.pack(pady=20)

    def destroy(self):
        Frame.destroy(self)


class SearchTheaterPlayMenu(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.parent.title("Search Theater Play Menu")
        self.pack(fill=BOTH, expand=True)

        title = ttk.Label(self, text="Search Theater Play Menu", )
        title.config(font=("Arial", 20))
        title.pack(pady=40)

        from data import theater_plays
        theater_plays_table = SearchableTable(self, theater_plays)
        theater_plays_table.pack(pady=20)

        separator = Frame(self, height=3, bd=0, relief=SUNKEN)
        separator.pack(fill=X, pady=10)

        back_button = new_primary_button(
            self, "Back",
            lambda: self.parent.switch_frame(SearchMenu)
        )
        back_button.pack(pady=20)

    def destroy(self):
        Frame.destroy(self)


class SearchArtistMenu(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.parent.title("Search Artist Menu")
        self.pack(fill=BOTH, expand=True)

        title = ttk.Label(self, text="Search Artist Menu", )
        title.config(font=("Arial", 20))
        title.pack(pady=40)

        from data import artists
        artists_table = SearchableTable(self, artists)
        artists_table.pack(pady=20)

        separator = Frame(self, height=3, bd=0, relief=SUNKEN)
        separator.pack(fill=X, pady=10)

        back_button = new_primary_button(
            self, "Back",
            lambda: self.parent.switch_frame(SearchMenu)
        )
        back_button.pack(pady=20)

    def destroy(self):
        Frame.destroy(self)


class SearchCastingMenu(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.parent.title("Search Casting Menu")
        self.pack(fill=BOTH, expand=True)

        title = ttk.Label(self, text="Search Casting Menu", )
        title.config(font=("Arial", 20))
        title.pack(pady=40)

        from data import castings
        castings_table = SearchableTable(self, castings)
        castings_table.pack(pady=20)

        separator = Frame(self, height=3, bd=0, relief=SUNKEN)
        separator.pack(fill=X, pady=10)

        back_button = new_primary_button(
            self, "Back",
            lambda: self.parent.switch_frame(SearchMenu)
        )
        back_button.pack(pady=20)

    def destroy(self):
        Frame.destroy(self)
