import tkinter as tk

import mainMenu


class MainApplication(tk.Tk):
    def __init__(self):
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
