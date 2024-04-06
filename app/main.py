import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

import mainMenu
from DBManager import DBManager


class MainApplication(tk.Tk):
    def __init__(self):
        # Database
        self.db_manager = DBManager()
        # This needs to be run first
        self.db_manager.run_file("../database/CreateUpdated.sql")

        # This two procedure definition needs to be run before Populate.sql
        self.db_manager.run_file("../database/GenArtisteHabit.sql")
        self.db_manager.run_file("../database/GenArtisteSport.sql")

        self.db_manager.run_file("../database/Populate.sql")

        self.db_manager.run_file("../database/DefGetArtists.sql")
        self.db_manager.run_file("../database/DefGetMovies.sql")
        self.db_manager.run_file("../database/DefGetPlays.sql")
        self.db_manager.run_file("../database/DefGetCastings.sql")
        self.db_manager.run_file("../database/DefAddMovies.sql")
        self.db_manager.run_file("../database/DefGetCompagnies.sql")
        self.db_manager.run_file("../database/DefAddPlays.sql")
        self.db_manager.run_file("../database/DefAddArtist.sql")
        self.db_manager.run_file("../database/DefAddAdresse.sql")

        # UI
        tk.Tk.__init__(self)

        style = ttk.Style()

        self.title("Casting Manager")
        self.geometry("1600x900")
        self.frame = None
        self.switch_frame(mainMenu.MainMenu)

    def switch_frame(self, frame):
        if self.frame is not None:
            self.frame.destroy()
        new_frame = frame(self)
        self.frame = new_frame
        self.frame.pack(fill=tk.BOTH, expand=True)


if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
