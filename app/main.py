import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

import mainMenu
from app.DBManager import DBManager



class MainApplication(tk.Tk):
    def __init__(self):
        # Database
        self.db_manager = DBManager()
        self.db_manager.run_file("database/CreateUpdated.sql")
        self.db_manager.run_file("database/GenArtisteHabit.sql")
        self.db_manager.run_file("database/GenArtisteSport.sql")
        self.db_manager.run_file("database/Populate.sql")

        # IMPORTANT
        # Queries will need to be separated into different files
        # for each procedure, because pymssql does not like the
        # GO keyword between procedures for some reason
        # for now, execute the whole file in azure data studio or something
        # and then refresh the database in pycharm
        #self.db_manager.execute_file("database/Queries.sql")

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
