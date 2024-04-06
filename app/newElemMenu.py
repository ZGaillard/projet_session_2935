import ttkbootstrap as ttk
from tkinter import Frame, Label, LEFT, SUNKEN, X, BOTH
from ttkbootstrap.constants import *
from DBManager import DBManager
from ttkbootstrap.dialogs.dialogs import Messagebox
import traceback

from style import new_primary_button


class BaseMenu(Frame):
    def __init__(self, parent, title):
        Frame.__init__(self, parent)
        self.parent = parent
        self.title = title
        self.initUI()
        self.initFrame()

    def initUI(self):
        self.parent.title(self.title)
        self.parent.geometry("1600x900")
        self.pack(fill=BOTH, expand=True)

    def initFrame(self):
        title = Label(self, text=self.title)
        title.config(font=("Arial", 40))
        title.pack(pady=60)

    def create_form_entry(self, label, variable):
        container = ttk.Frame(self)
        container.pack(pady=5, fill=X)

        inner_frame = ttk.Frame(container)
        inner_frame.grid(row=0, column=0, padx=(20, 0))

        lbl = ttk.Label(master=inner_frame, text=label.title(), width=25, anchor="e")
        lbl.grid(row=0, column=0, padx=(0, 5))

        ent = ttk.Entry(master=inner_frame, textvariable=variable, width=30)
        ent.grid(row=0, column=1, padx=(5, 0))

        container.columnconfigure(0, weight=1)

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

    def clear_form(self):
        pass


class NewElemMenu(BaseMenu):
    def __init__(self, parent):
        super().__init__(parent, "New Element Menu")

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


class NewMovieMenu(BaseMenu):
    def __init__(self, parent):
        super().__init__(parent, "New Movie Menu")

        self.titre = ttk.StringVar(value="")
        self.budget = ttk.IntVar(value="")
        self.date = ttk.StringVar(value="")
        self.duree = ttk.IntVar(value=0)
        self.origine = ttk.StringVar(value="")
        self.langue = ttk.StringVar(value="")
        self.genre = ttk.StringVar(value="")
        self.objectif = ttk.StringVar(value="")
        self.theme = ttk.StringVar(value="")

        # form entries
        self.create_form_entry("Titre", self.titre)
        self.create_form_entry("Budget", self.budget)
        self.create_form_entry("Date de sortie", self.date)
        self.create_form_entry("Durée", self.duree)
        self.create_form_entry("Origine", self.origine)
        self.create_form_entry("Langue", self.langue)
        self.create_form_entry("Genre", self.genre)
        self.create_form_entry("Objectif", self.objectif)
        self.create_form_entry("Theme", self.theme)

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

    def on_submit(self):
        try:
            DBManager().run_procedure_with_args(
                "AddMovies",
                f"@titre='{self.titre.get()}', @budget={self.budget.get()}, @date_sortie='{self.date.get()}', @duree={self.duree.get()}, @origine='{self.origine.get()}', @langue='{self.langue.get()}', @genre='{self.genre.get()}',@objectif='{self.objectif.get()}', @theme='{self.theme.get()}', @id_producteur={self.selected_producteur_id.get()}",
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


class NewTheaterPlayMenu(BaseMenu):
    def __init__(self, parent):
        super().__init__(parent, "New Play Menu")

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

    def on_submit(self):
        try:
            DBManager().run_procedure_with_args(
                "AddPlays",
                f"@titre='{self.titre.get()}', @budget={self.budget.get()}, @date_sortie='{self.date.get()}', @duree={self.duree.get()}, @origine='{self.origine.get()}', @langue='{self.langue.get()}', @genre='{self.genre.get()}', @theatre='{self.theatre.get()}'",
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
        self.theatre.set("")


class NewArtistMenu(BaseMenu):
    def __init__(self, parent):
        super().__init__(parent, "New Artist Menu")

        self.prenom = ttk.StringVar(value="")
        self.nom = ttk.StringVar(value="")
        self.date_naissance = ttk.StringVar(value="")
        self.salaire_min = ttk.IntVar(value=0)
        self.domaine = ttk.StringVar(value="")
        self.no_civique = ttk.IntVar(value=0)
        self.rue = ttk.StringVar(value="")
        self.ville = ttk.StringVar(value="")
        self.code_postal = ttk.StringVar(value="")
        self.pays = ttk.StringVar(value="")
        self.no_appartement = ttk.IntVar(value=None)

        # form entries
        self.create_form_entry("Prénom", self.prenom)
        self.create_form_entry("Nom", self.nom)
        self.create_form_entry("Date de naissance", self.date_naissance)
        self.create_form_entry("Salaire minimum", self.salaire_min)
        self.create_form_entry("Domaine", self.domaine)
        self.create_form_entry("Numéro Civique", self.no_civique)
        self.create_form_entry("Rue", self.rue)
        self.create_form_entry("Ville", self.ville)
        self.create_form_entry("Code Postal", self.code_postal)
        self.create_form_entry("Pays", self.pays)
        self.create_form_entry("Numéro appartement", self.no_appartement)

        back_button = new_primary_button(
            self, "Back", lambda: self.parent.switch_frame(NewElemMenu)
        )
        self.create_buttonbox()
        back_button.pack(pady=20)

    def on_submit(self):
        try:
            DBManager().run_procedure_with_args(
                "AddArtist",
                f"@nom='{self.nom.get()}', @prenom='{self.prenom.get()}', @date_naissance='{self.date_naissance.get()}', @salaire_min={self.salaire_min.get()},@domaine='{self.domaine.get()}', @no_civique={self.no_civique.get()}, @rue='{self.rue.get()}', @ville='{self.ville.get()}', @code_postal='{self.code_postal.get()}', @pays='{self.pays.get()}', @no_appartement={self.no_appartement.get()}",
            )
            Messagebox.ok("Artist added successfully", "Success")
            self.clear_form()
        except:
            traceback.print_exc()
            Messagebox.show_error("Enter valid datas please", "Error")

    def clear_form(self):
        self.nom.set("")
        self.prenom.set("")
        self.date_naissance.set("")
        self.domaine.set("")
        self.pays.set("")
        self.no_appartement.set("")
        self.no_civique.set(0)
        self.code_postal.set("")
        self.rue.set("")
        self.salaire_min.set(0)
        self.ville.set("")


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
