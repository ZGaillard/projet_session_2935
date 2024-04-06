from datetime import datetime
from tkinter import *

import ttkbootstrap as ttk

from app.DBManager import DBManager
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
        self.artists_table = SearchableTable(self, artists)
        self.artists_table.pack(pady=20)

        see_habit_sport_button = new_primary_button(
            self, "See Artist's Habits and Sports",
            self.see_artist_habit_sport,
            width=32
        )
        see_habit_sport_button.pack(pady=10)

        see_relations_button = new_primary_button(
            self, "See Artist's Relations",
            self.see_artist_relations,
            width=32
        )
        see_relations_button.pack(pady=10)

        back_button = new_primary_button(
            self, "Back",
            lambda: self.parent.switch_frame(SearchMenu)
        )
        back_button.pack(pady=40)

    def see_artist_relations(self):
        selected_artist_id = self.get_selected_artist_id()
        if selected_artist_id is None:
            return
        self.parent.switch_frame(ArtistRelationMenu, selected_artist_id)

    def see_artist_habit_sport(self):
        selected_artist_id = self.get_selected_artist_id()
        if selected_artist_id is None:
            return
        self.parent.switch_frame(ArtistHabitSportMenu, selected_artist_id)

    def destroy(self):
        Frame.destroy(self)

    def get_selected_artist_id(self):
        selected_artist_id = self.artists_table.selection()
        if not selected_artist_id:
            return None

        # format the data to be able to compare it
        selected_artist = self.artists_table.item(selected_artist_id[0])[
            'values']
        selected_artist[2] = selected_artist[2].split('-')
        selected_artist[2] = "-".join(selected_artist[2][::-1])
        selected_artist[2] = datetime.strptime(selected_artist[2],
                                               "%d-%m-%Y").date()
        selected_artist[8] = str(selected_artist[8])
        if selected_artist[-1] == 'None':
            selected_artist[-1] = None
        selected_artist = tuple(selected_artist)

        # we got rid of the first column which is the id
        # we need to retrieve it from the data
        artist_id = None
        for row in self.artists_table.data:
            if row[1:] == selected_artist:
                artist_id = row[0]
                break
        if artist_id is None:
            return None

        return artist_id


class ArtistHabitSportMenu(Frame):
    def __init__(self, parent, artist_id):
        habits = DBManager().run_procedure_with_args(
            "getArtistHabits", artist_id
        )
        if habits is None:
            habits = []
        sports = DBManager().run_procedure_with_args(
            "getArtistSports", artist_id
        )
        if sports is None:
            sports = []

        artist_name = DBManager().read_where(
            "Artiste",
            "prenom, nom",
            f"id={artist_id}"
        )

        Frame.__init__(self, parent)
        self.parent = parent
        self.parent.title(
            f"{artist_name[0][0]} {artist_name[0][1]}'s Habits and Sports")
        self.pack(fill=BOTH, expand=True)

        title = ttk.Label(self,
                          text=f"{artist_name[0][0]} {artist_name[0][1]}'s Habits and Sports", )
        title.config(font=("Arial", 20))
        title.pack(pady=40)

        details_container = Frame(self)
        details_container.pack(pady=20)

        habits_container = Frame(details_container)
        habits_container.pack(side=LEFT, padx=10)

        habits_label = ttk.Label(habits_container, text="Habits")
        habits_label.pack(pady=10)

        habits_listbox = Listbox(habits_container)
        habits_listbox.pack(pady=10)

        for habit in habits:
            habits_listbox.insert(END, habit[2])

        sports_container = Frame(details_container)
        sports_container.pack(side=LEFT, padx=10)

        sports_label = ttk.Label(sports_container, text="Sports")
        sports_label.pack(pady=10)

        sports_listbox = Listbox(sports_container)
        sports_listbox.pack(pady=10)

        for sport in sports:
            sports_listbox.insert(END, sport[2])

        back_button = new_primary_button(
            self, "Back",
            lambda: self.parent.switch_frame(SearchArtistMenu)
        )
        back_button.pack(pady=20)


class ArtistRelationMenu(Frame):
    def __init__(self, parent, artist_id):
        relations = DBManager().run_procedure_with_args(
            "getArtistRelations", artist_id
        )

        artist_name = DBManager().read_where(
            "Artiste",
            "prenom, nom",
            f"id={artist_id}"
        )

        Frame.__init__(self, parent)
        self.parent = parent
        self.parent.title(
            f"{artist_name[0][0]} {artist_name[0][1]}'s Relations")
        self.pack(fill=BOTH, expand=True)

        title = ttk.Label(
            self,
            text=f"{artist_name[0][0]} {artist_name[0][1]}'s Relations"
        )
        title.config(font=("Arial", 20))
        title.pack(pady=40)

        details_container = Frame(self)
        details_container.pack(pady=20)

        relations_label = ttk.Label(details_container, text="Relations")
        relations_label.pack(pady=10)

        relations_treeview = ttk.Treeview(details_container,
                                          columns=("Artist", "Relation"))
        relations_treeview.heading("Artist", text="Artist")
        relations_treeview.heading("Relation", text="Relation")
        relations_treeview.column("#0", width=0, stretch=NO)
        relations_treeview.column("Artist", width=400)
        relations_treeview.column("Relation", width=400)
        relations_treeview.config(height=10)
        relations_treeview.pack(pady=10)

        for relation in relations:
            full_name = str(relation[0]) + " " + str(relation[1])
            relations_treeview.insert("", "end",
                                      values=(full_name, relation[2])
                                      )

        back_button = new_primary_button(
            self, "Back",
            lambda: self.parent.switch_frame(SearchArtistMenu)
        )
        back_button.pack(pady=20)


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
        self.castings_table = SearchableTable(self, castings)
        self.castings_table.pack(pady=20)

        see_artist_button = new_primary_button(
            self, "See the artists participating in the casting",
            self.see_artist_castings,
            width=38
        )
        see_artist_button.pack(pady=10)

        back_button = new_primary_button(
            self, "Back",
            lambda: self.parent.switch_frame(SearchMenu)
        )
        back_button.pack(pady=20)

    def destroy(self):
        Frame.destroy(self)

    def see_artist_castings(self):
        selected_casting_id = self.get_selected_casting_id()
        if selected_casting_id is None:
            return
        self.parent.switch_frame(ArtistCastingMenu, selected_casting_id)

    def get_selected_casting_id(self):
        selected_casting_id = self.castings_table.selection()
        if not selected_casting_id:
            return None
        selected_casting = self.castings_table.item(selected_casting_id[0])['values']
        selected_casting = tuple(selected_casting)
        casting_id = None
        from data import castings
        for row in castings.get_tuples():
            if row[1:] == selected_casting:
                casting_id = row[0]
                break

        return casting_id

class ArtistCastingMenu(Frame):

    def __init__(self, parent, casting_id):
        artists = DBManager().run_procedure_with_args(
            "getCastingArtists", casting_id
        )

        casting_name = DBManager().read_where(
            "Oeuvre",
            "titre",
            f"id={casting_id}"
        )

        Frame.__init__(self, parent)
        self.parent = parent
        self.parent.title(
            f"{casting_name[0][0]}'s Artists")
        self.pack(fill=BOTH, expand=True)

        title = ttk.Label(self,
                          text=f"{casting_name[0][0]}'s Artists", )
        title.config(font=("Arial", 20))
        title.pack(pady=40)

        details_container = Frame(self)
        details_container.pack(pady=20)

        artists_label = ttk.Label(details_container, text="Artists")
        artists_label.pack(pady=10)

        artists_treeview = ttk.Treeview(details_container,
                                          columns=("Artist", "Role"))
        artists_treeview.heading("Artist", text="Artist")
        artists_treeview.heading("Role", text="Role")
        artists_treeview.column("#0", width=0, stretch=NO)
        artists_treeview.column("Artist", width=400)
        artists_treeview.column("Role", width=400)
        artists_treeview.config(height=10)
        artists_treeview.pack(pady=10)

        for artist in artists:
            full_name = str(artist[0]) + " " + str(artist[1])
            artists_treeview.insert("", "end",
                                      values=(full_name, artist[2])
                                      )

        back_button = new_primary_button(
            self, "Back",
            lambda: self.parent.switch_frame(SearchCastingMenu)
        )
        back_button.pack(pady=20)