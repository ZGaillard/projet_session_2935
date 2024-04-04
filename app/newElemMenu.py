import ttkbootstrap as ttk
from tkinter import Frame, Label, LEFT, SUNKEN, X, BOTH
from ttkbootstrap.constants import *
from DBManager import DBManager
from ttkbootstrap.dialogs.dialogs import Messagebox
import traceback

from style import new_primary_button


class NewElemMenu(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
        self.initFrame()

    def initUI(self):
        self.parent.title("New Element Menu")
        self.parent.geometry("1600x900")

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
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
        self.initFrame()

    def initUI(self):
        self.parent.title("New Movie Menu")
        self.parent.geometry("1600x900")

        self.pack(fill=BOTH, expand=True)

    def initFrame(self):
        title = Label(self, text="New Movie Menu")
        title.config(font=("Arial", 40))
        title.pack(pady=60)

        self.titre = ttk.StringVar(value="")
        self.budget = ttk.IntVar(value="")
        self.date = ttk.StringVar(value="")
        self.duree = ttk.IntVar(value=0)
        self.origine = ttk.StringVar(value="")
        self.langue = ttk.StringVar(value="")
        self.genre = ttk.StringVar(value="")
        # form entries
        self.create_form_entry("Titre", self.titre)
        self.create_form_entry("Budget", self.budget)
        self.create_form_entry("Date de sortie", self.date)
        self.create_form_entry("Durée", self.duree)
        self.create_form_entry("Origine", self.origine)
        self.create_form_entry("Langue", self.langue)
        self.create_form_entry("Genre", self.genre)
        self.producteur_treeview = ttk.Treeview(
            self, columns=("Producteur"), show="headings"
        )
        self.producteur_treeview.heading("#1", text="Producteur")
        self.producteur_treeview.column("#1", width=200, stretch=True)
        self.producteur_treeview.pack(pady=20)
        self.populate_producteur_treeview()
        self.selected_producteur_id = ttk.IntVar()
        back_button = new_primary_button(
            self, "Back", lambda: self.parent.switch_frame(NewElemMenu)
        )
        self.create_buttonbox()
        back_button.pack(pady=20)

    def populate_producteur_treeview(self):
        from data import compagnies

        # Clear the Treeview before populating it with new results
        for item in self.producteur_treeview.get_children():
            self.producteur_treeview.delete(item)

        # Populate the Treeview with the results
        for result in compagnies.tuples:
            self.producteur_treeview.insert(
                "", ttk.END, values=result[1], iid=result[0]
            )

        def on_treeview_select(event):
            selected_item = self.producteur_treeview.selection()[0]
            self.selected_producteur_id.set(int(selected_item))

        self.producteur_treeview.bind("<<TreeviewSelect>>", on_treeview_select)

    def create_form_entry(self, label, variable):
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=5)

        lbl = ttk.Label(master=container, text=label.title(), width=10)
        lbl.pack(side=LEFT, padx=5)

        ent = ttk.Entry(master=container, textvariable=variable)
        ent.pack(side=LEFT, padx=5, fill=X, expand=YES)

    def create_buttonbox(self):
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=(15, 10))

        sub_btn = ttk.Button(
            master=container,
            text="Add",
            command=self.on_submit,
            bootstyle=SUCCESS,
            width=6,
        )
        sub_btn.pack(padx=5)
        sub_btn.focus_set()

    def on_submit(self):
        try:
            DBManager().run_procedure_with_args(
                "AddMovies",
                f"@id={600}, @titre='{self.titre.get()}', @budget={self.budget.get()}, @date_sortie='{self.date.get()}', @duree={self.duree.get()}, @origine='{self.origine.get()}', @langue='{self.langue.get()}', @genre='{self.genre.get()}', @id_producteur={self.selected_producteur_id.get()}",
            )
            Messagebox.ok("Movie added successfully", "Success")
            self.clear_form()
        except:
            Messagebox.show_error("Enter valid datas please", "Error")

    def clear_form(self):
        self.titre.set("")
        self.budget.set("")
        self.date.set("")
        self.duree.set(0)
        self.origine.set("")
        self.langue.set("")
        self.genre.set("")


class NewTheaterPlayMenu(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
        self.initFrame()

    def initUI(self):
        self.parent.title("New Play Menu")
        self.parent.geometry("1600x900")

        self.pack(fill=BOTH, expand=True)

    def initFrame(self):
        title = Label(self, text="New Play Menu")
        title.config(font=("Arial", 40))
        title.pack(pady=60)

        self.titre = ttk.StringVar(value="")
        self.budget = ttk.IntVar(value="")
        self.date = ttk.StringVar(value="")
        self.duree = ttk.IntVar(value=0)
        self.origine = ttk.StringVar(value="")
        self.langue = ttk.StringVar(value="")
        self.genre = ttk.StringVar(value="")
        self.theatre = ttk.StringVar(value="")
        # form entries
        self.create_form_entry("Titre", self.titre)
        self.create_form_entry("Budget", self.budget)
        self.create_form_entry("Date de sortie", self.date)
        self.create_form_entry("Durée", self.duree)
        self.create_form_entry("Origine", self.origine)
        self.create_form_entry("Langue", self.langue)
        self.create_form_entry("Genre", self.genre)
        self.create_form_entry("Theatre", self.theatre)
        back_button = new_primary_button(
            self, "Back", lambda: self.parent.switch_frame(NewElemMenu)
        )
        self.create_buttonbox()
        back_button.pack(pady=20)

    def create_form_entry(self, label, variable):
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=5)

        lbl = ttk.Label(master=container, text=label.title(), width=10)
        lbl.pack(side=LEFT, padx=5)

        ent = ttk.Entry(master=container, textvariable=variable)
        ent.pack(side=LEFT, padx=5, fill=X, expand=YES)

    def create_buttonbox(self):
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=(15, 10))

        sub_btn = ttk.Button(
            master=container,
            text="Add",
            command=self.on_submit,
            bootstyle=SUCCESS,
            width=6,
        )
        sub_btn.pack(padx=5)
        sub_btn.focus_set()

    def on_submit(self):
        try:

            DBManager().run_procedure_with_args(
                "AddPlays",
                f"@id={700}, @titre='{self.titre.get()}', @budget={self.budget.get()}, @date_sortie='{self.date.get()}', @duree={self.duree.get()}, @origine='{self.origine.get()}', @langue='{self.langue.get()}', @genre='{self.genre.get()}', @theatre='{self.theatre.get()}'",
            )
            Messagebox.ok("Play added successfully", "Success")
            self.clear_form()
        except:
            traceback.print_exc()
            Messagebox.show_error("Enter valid datas please", "Error")

    def clear_form(self):
        self.titre.set("")
        self.budget.set("")
        self.date.set("")
        self.duree.set(0)
        self.origine.set("")
        self.langue.set("")
        self.genre.set("")


class NewArtistMenu(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
        self.initFrame()

    def initUI(self):
        self.parent.title("New Artist Menu")
        self.parent.geometry("1600x900")

        self.pack(fill=BOTH, expand=True)

    def initFrame(self):
        title = Label(self, text="New Artist Menu")
        title.config(font=("Arial", 40))
        title.pack(pady=60)

        back_button = new_primary_button(
            self, "Back", lambda: self.parent.switch_frame(NewElemMenu)
        )
        back_button.pack(pady=20)


class NewCastingMenu(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
        self.initFrame()

    def initUI(self):
        self.parent.title("New Casting Menu")
        self.parent.geometry("1600x900")

        self.pack(fill=BOTH, expand=True)

    def initFrame(self):
        title = Label(self, text="New Casting Menu")
        title.config(font=("Arial", 40))
        title.pack(pady=60)
