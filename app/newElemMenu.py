import ttkbootstrap as ttk
from tkinter import Frame, Label, LEFT, SUNKEN, X, BOTH

from style import new_primary_button


class NewElemMenu(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
        self.initFrame()

    def initUI(self):
        self.parent.title("New Element Menu")
        self.pack(fill=BOTH, expand=True)

    def initFrame(self):
        # title
        title = Label(self, text="New Element Menu")
        title.config(font=("Arial", 40))
        title.pack(pady=60)

        # button for each new element
        button_container_1 = Frame(self)
        button_container_1.pack(pady=20)

        n_movie_button = new_primary_button(
            button_container_1,
            "New movie",
            lambda: self.parent.switch_frame(NewMovieMenu),
        )
        n_movie_button.pack(side=LEFT, padx=10)
        n_theater_play_button = new_primary_button(
            button_container_1,
            "New theater play",
            lambda: self.parent.switch_frame(NewTheaterPlayMenu),
        )
        n_theater_play_button.pack(side=LEFT, padx=10)

        button_container_2 = Frame(self)
        button_container_2.pack(pady=20)

        n_artist_button = new_primary_button(
            button_container_2,
            "New artist",
            lambda: self.parent.switch_frame(NewArtistMenu),
        )
        n_artist_button.pack(side=LEFT, padx=10)
        n_casting_button = new_primary_button(
            button_container_2,
            "New casting",
            lambda: self.parent.switch_frame(NewCastingMenu),
        )
        n_casting_button.pack(side=LEFT, padx=10)

        separator = Frame(self, height=3, bd=0, relief=SUNKEN)
        separator.pack(fill=X, pady=10)

        # button to go back to main menu
        from mainMenu import MainMenu

        back_button = new_primary_button(
            self, "Back", lambda: self.parent.switch_frame(MainMenu)
        )
        back_button.pack(pady=20)


class NewMovieMenu(Frame):
    pass


class NewTheaterPlayMenu(Frame):
    pass


class NewArtistMenu(Frame):
    pass


class NewCastingMenu(Frame):
    pass
