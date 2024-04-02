from tkinter import *

from app.style import STYLE_CONFIG, create_button


class NewElemMenu(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
        self.initFrame()

    def initUI(self):
        self.parent.title("New Element Menu")
        self.parent.geometry("1600x900")
        self.configure(background=STYLE_CONFIG["background"])
        self.pack(fill=BOTH, expand=True)

    def initFrame(self):
        # title
        title = Label(self, text="New Element Menu",
                      background=STYLE_CONFIG["background"])
        title.config(font=("Arial", 40))
        title.pack(pady=60)

        # button for each new element
        button_container_1 = Frame(self, background=STYLE_CONFIG["background"])
        button_container_1.pack(pady=20)

        n_movie_button = create_button(button_container_1, "New movie",
                                       lambda: self.parent.switch_frame(
                                           NewMovieMenu))
        n_movie_button.pack(side=LEFT, padx=10)
        n_theater_play_button = create_button(button_container_1,
                                              "New theater play",
                                              lambda: self.parent.switch_frame(
                                                  NewTheaterPlayMenu))
        n_theater_play_button.pack(side=LEFT, padx=10)

        button_container_2 = Frame(self, background=STYLE_CONFIG["background"])
        button_container_2.pack(pady=20)

        n_actor_button = create_button(button_container_2, "New actor",
                                       lambda: self.parent.switch_frame(
                                           NewActorMenu))
        n_actor_button.pack(side=LEFT, padx=10)
        n_casting_button = create_button(button_container_2, "New casting",
                                         lambda: self.parent.switch_frame(
                                             NewCastingMenu))
        n_casting_button.pack(side=LEFT, padx=10)

        separator = Frame(self, height=3, bd=0, relief=SUNKEN)
        separator.pack(fill=X, pady=10)

        # button to go back to main menu
        from app.mainMenu import MainMenu
        back_button = create_button(self, "Back",
                                    lambda: self.parent.switch_frame(MainMenu))
        back_button.pack(pady=20)


class NewMovieMenu(Frame):
    pass


class NewTheaterPlayMenu(Frame):
    pass


class NewActorMenu(Frame):
    pass


class NewCastingMenu(Frame):
    pass
