import tkinter as tk

import mainMenu
from app.DBManager import DBManager


class MainApplication(tk.Tk):
    def __init__(self):
        # Database
        self.db_manager = DBManager()
        self.db_manager.execute_file("database/CreateUpdated.sql")
        self.db_manager.execute_file("database/Populate.sql")
        #self.db_manager.execute_file("database/GenArtisteHabit.sql")
        #self.db_manager.execute_file("database/GenArtisteSport.sql")



        # UI
        tk.Tk.__init__(self)
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
