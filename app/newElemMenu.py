from tkinter import Frame, Label

import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs.dialogs import Messagebox

from DBManager import DBManager
from data import update_data
from style import new_primary_button
from SearchableTable import SearchableTable


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


def create_text_entry(self, label, variable):
    container = ttk.Frame(self)
    container.pack(fill=X, expand=YES, pady=5)

    lbl = ttk.Label(master=container, text=label.title(), width=10)
    lbl.pack(side=LEFT, padx=5)

    ent = ttk.Entry(master=container, textvariable=variable)
    ent.pack(side=LEFT, padx=5, fill=X, expand=YES)


def create_date_entry(self, label, variable):
    container = ttk.Frame(self)
    container.pack(fill=X, expand=YES, pady=5)

    lbl = ttk.Label(master=container, text=label.title(), width=10)
    lbl.pack(side=LEFT, padx=5)

    date_ent = ttk.DateEntry(master=container)
    date_ent.entry.config(textvariable=variable)
    date_ent.pack(side=LEFT, padx=5, fill=X, expand=YES)

    return date_ent


def create_spinbox_entry(self, label, variable):
    container = ttk.Frame(self)
    container.pack(fill=X, expand=YES, pady=5)

    lbl = ttk.Label(master=container, text=label.title(), width=10)
    lbl.pack(side=LEFT, padx=5)

    spin_ent = ttk.Spinbox(master=container, textvariable=variable, from_=0,
                           to=1000000)
    spin_ent.pack(side=LEFT, padx=5, fill=X, expand=YES)


def create_form_entry(parent, label, variable):
    container = ttk.Frame(parent)
    container.pack(fill=X, expand=YES, pady=5)

    lbl = ttk.Label(master=container, text=label.title(), width=10)
    lbl.pack(side=LEFT, padx=5)

    ent = ttk.Entry(master=container, textvariable=variable)
    ent.pack(side=LEFT, padx=5, fill=X, expand=YES)


def create_submit_button(parent):
    container = ttk.Frame(parent)
    container.pack(fill=X, expand=YES, pady=(15, 10))

    sub_btn = ttk.Button(
        master=container,
        text="Add",
        command=parent.on_submit,
        style=SUCCESS,
        width=6,
    )
    sub_btn.pack(padx=5)
    sub_btn.focus_set()


def create_back_button(parent):
    back_button = new_primary_button(
        parent, "Back", lambda: parent.parent.switch_frame(NewElemMenu)
    )
    back_button.pack(pady=20)


class NewMovieMenu(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.date_ent = None
        self.producteur_treeview = None
        self.selected_producteur_id = ttk.IntVar()

        self.genre = ttk.StringVar(value="")
        self.langue = ttk.StringVar(value="")
        self.origine = ttk.StringVar(value="")
        self.duree = ttk.IntVar(value=0)
        self.date = ttk.StringVar(value="")
        self.budget = ttk.IntVar(value=0)
        self.titre = ttk.StringVar(value="")

        self.parent = parent

        self.parent.title("New Movie Menu")
        self.pack(fill=BOTH, expand=True)

        self.initFrame()

    def initFrame(self):
        title = Label(self, text="New Movie Menu")
        title.config(font=("Arial", 40))
        title.pack(pady=60)

        container = ttk.Frame(self)
        container.pack(fill=BOTH, expand=YES, pady=20)

        form_container = ttk.Frame(container)
        form_container.pack(side=LEFT, fill=BOTH, expand=YES, pady=20)
        # form entries
        create_form_entry(form_container, "Titre", self.titre)
        create_spinbox_entry(form_container, "Budget", self.budget)
        create_date_entry(form_container, "Date de sortie", self.date)
        create_spinbox_entry(form_container, "Durée", self.duree)
        create_form_entry(form_container, "Origine", self.origine)
        create_form_entry(form_container, "Langue", self.langue)
        create_form_entry(form_container, "Genre", self.genre)
        self.producteur_treeview = ttk.Treeview(
            container, columns="Producteur", show="headings"
        )
        self.producteur_treeview.heading("#1", text="Producteur")
        self.producteur_treeview.column("#1", width=200, stretch=False)
        self.producteur_treeview.pack(side=LEFT, fill=BOTH, expand=YES, padx=20)
        self.populate_producteur_treeview()

        create_submit_button(self)
        create_back_button(self)

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
        if self.selected_producteur_id.get() == 0:
            Messagebox.show_error("Select a producteur", "Error")
            return
        if self.titre.get() == "":
            Messagebox.show_error("Enter a title", "Error")
            return
        if self.date.get() == "":
            Messagebox.show_error("Enter a date", "Error")
            return
        if self.genre.get() == "":
            Messagebox.show_error("Enter a genre", "Error")
            return
        if self.langue.get() == "":
            Messagebox.show_error("Enter a langue", "Error")
            return
        if self.origine.get() == "":
            Messagebox.show_error("Enter an origine", "Error")
            return
        if self.duree.get() == 0:
            Messagebox.show_error("Enter a duree", "Error")
            return
        if self.budget.get() == 0:
            Messagebox.show_error("Enter a budget", "Error")
            return

        sql_args = (
            f" '{self.titre.get()}',"
            f" {self.budget.get()},"
            f" '{self.date.get()}',"
            f" {self.duree.get()},"
            f" '{self.origine.get()}',"
            f" '{self.langue.get()}',"
            f" '{self.genre.get()}',"
            f" '{self.selected_producteur_id.get()}';"
        )
        print(sql_args)

        DBManager().run_procedure_with_args("AddMovies", sql_args)
        update_data()

        Messagebox.ok("Movie added successfully", "Success")
        self.clear_form()

    def clear_form(self):
        self.titre.set("")
        self.budget.set(0)
        self.date.set("")
        self.duree.set(0)
        self.origine.set("")
        self.langue.set("")
        self.genre.set("")


class NewTheaterPlayMenu(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.theatre = ttk.StringVar(value="")
        self.genre = ttk.StringVar(value="")
        self.langue = ttk.StringVar(value="")
        self.origine = ttk.StringVar(value="")
        self.duree = ttk.IntVar(value=0)
        self.date = ttk.StringVar(value="")
        self.budget = ttk.IntVar(value=0)
        self.titre = ttk.StringVar(value="")
        self.parent = parent
        self.parent.title("New Play Menu")
        self.pack(fill=BOTH, expand=True)
        self.initFrame()

    def initFrame(self):
        title = Label(self, text="New Play Menu")
        title.config(font=("Arial", 40))
        title.pack(pady=60)

        # form entries
        create_form_entry(self, "Titre", self.titre)
        create_spinbox_entry(self, "Budget", self.budget)
        create_date_entry(self, "Date de sortie", self.date)
        create_spinbox_entry(self, "Durée", self.duree)
        create_form_entry(self, "Origine", self.origine)
        create_form_entry(self, "Langue", self.langue)
        create_form_entry(self, "Genre", self.genre)
        create_form_entry(self, "Théâtre", self.theatre)

        create_submit_button(self)
        create_back_button(self)

    def on_submit(self):
        if self.titre.get() == "":
            Messagebox.show_error("Enter a title", "Error")
            return
        if self.date.get() == "":
            Messagebox.show_error("Enter a date", "Error")
            return
        if self.genre.get() == "":
            Messagebox.show_error("Enter a genre", "Error")
            return
        if self.langue.get() == "":
            Messagebox.show_error("Enter a langue", "Error")
            return
        if self.origine.get() == "":
            Messagebox.show_error("Enter an origine", "Error")
            return
        if self.duree.get() == 0:
            Messagebox.show_error("Enter a duree", "Error")
            return
        if self.budget.get() == 0:
            Messagebox.show_error("Enter a budget", "Error")
            return
        if self.theatre.get() == "":
            Messagebox.show_error("Enter a theatre", "Error")
            return

        sql_args = (
            f" '{self.titre.get()}',"
            f" {self.budget.get()},"
            f" '{self.date.get()}',"
            f" {self.duree.get()},"
            f" '{self.origine.get()}',"
            f" '{self.langue.get()}',"
            f" '{self.genre.get()}',"
            f" '{self.theatre.get()}';"
        )
        print(sql_args)

        DBManager().run_procedure_with_args("AddPlays", sql_args)
        update_data()

        Messagebox.ok("Play added successfully", "Success")
        self.clear_form()

    def clear_form(self):
        self.titre.set("")
        self.budget.set(0)
        self.date.set("")
        self.duree.set(0)
        self.origine.set("")
        self.langue.set("")
        self.genre.set("")


class NewArtistMenu(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.parent.title("New Play Menu")
        self.pack(fill=BOTH, expand=True)

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

        self.initFrame()

    def initFrame(self):
        title = Label(self, text="New Play Menu")
        title.config(font=("Arial", 40))
        title.pack(pady=60)

        # form entries
        create_form_entry(self, "Prénom", self.prenom)
        create_form_entry(self, "Nom", self.nom)
        create_date_entry(self, "Date de naissance", self.date_naissance)
        create_spinbox_entry(self, "Salaire minimum", self.salaire_min)
        create_form_entry(self, "Domaine", self.domaine)
        create_spinbox_entry(self, "Numéro civique", self.no_civique)
        create_form_entry(self, "Rue", self.rue)
        create_form_entry(self, "Ville", self.ville)
        create_spinbox_entry(self, "Code postal", self.code_postal)
        create_form_entry(self, "Pays", self.pays)
        create_spinbox_entry(self, "Numéro appartement", self.no_appartement)

        create_submit_button(self)
        create_back_button(self)

    def on_submit(self):
        if self.prenom.get() == "":
            Messagebox.show_error("Enter a prenom", "Error")
            return
        if self.nom.get() == "":
            Messagebox.show_error("Enter a nom", "Error")
            return
        if self.date_naissance.get() == "":
            Messagebox.show_error("Enter a date de naissance", "Error")
            return
        if self.salaire_min.get() == 0:
            Messagebox.show_error("Enter a salaire minimum", "Error")
            return
        if self.domaine.get() == "":
            Messagebox.show_error("Enter a domaine", "Error")
            return
        if self.no_civique.get() == 0:
            Messagebox.show_error("Enter a no civique", "Error")
            return
        if self.rue.get() == "":
            Messagebox.show_error("Enter a rue", "Error")
            return
        if self.ville.get() == "":
            Messagebox.show_error("Enter a ville", "Error")
            return
        if self.code_postal.get() == "":
            Messagebox.show_error("Enter a code postal", "Error")
            return
        if self.pays.get() == "":
            Messagebox.show_error("Enter a pays", "Error")
            return

        if self.no_appartement.get() is None:
            sql_args_addr = (
                f" {self.no_civique.get()},"
                f" '{self.rue.get()}',"
                f" '{self.ville.get()}',"
                f" '{self.code_postal.get()}',"
                f" '{self.pays.get()}',"
                f" NULL;"
            )
        else:
            sql_args_addr = (
                f" {self.no_civique.get()},"
                f" '{self.rue.get()}',"
                f" '{self.ville.get()}',"
                f" '{self.code_postal.get()}',"
                f" '{self.pays.get()}',"
                f" {self.no_appartement.get()};"
            )

        id_adresse = DBManager().run_procedure_with_args(
            "AddAdresse", sql_args_addr)[0][0]

        print(id_adresse)

        sql_args = (
            f" '{self.prenom.get()}',"
            f" '{self.nom.get()}',"
            f" '{self.date_naissance.get()}',"
            f" {self.salaire_min.get()},"
            f" '{self.domaine.get()}',"
            f" {id_adresse};"
        )

        print(sql_args)
        DBManager().run_procedure_with_args("AddArtist", sql_args)
        update_data()

        Messagebox.ok("Artist added successfully", "Success")
        self.clear_form()

    def clear_form(self):
        self.nom.set("")
        self.prenom.set("")
        self.date_naissance.set("")
        self.domaine.set("")
        self.pays.set("")
        self.no_appartement.set(0)
        self.no_civique.set(0)
        self.code_postal.set("")
        self.rue.set("")
        self.salaire_min.set(0)
        self.ville.set("")


class NewCastingMenu(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.oeuvre_treeview = None
        self.parent = parent
        self.parent.title("New Casting Menu")
        self.pack(fill=BOTH, expand=True)
        self.objectif = ttk.StringVar(value="")
        self.theme = ttk.StringVar(value="")
        self.id_oeuvre = ttk.IntVar(value=0)
        self.initFrame()

    def initFrame(self):
        title = Label(self, text="New Casting Menu")
        title.config(font=("Arial", 40))
        title.pack(pady=60)

        container = ttk.Frame(self)
        container.pack(fill=BOTH, expand=YES, pady=20)

        form_container = ttk.Frame(container)
        form_container.pack(side=LEFT, fill=BOTH, expand=YES, pady=20)
        # form entries
        create_form_entry(form_container, "Objectif", self.objectif)
        create_form_entry(form_container, "Theme", self.theme)

        self.oeuvre_treeview = ttk.Treeview(
            container, columns="Producteur", show="headings"
        )
        self.oeuvre_treeview.heading("#1", text="Oeuvre")
        self.oeuvre_treeview.column("#1", width=300, stretch=True)
        self.oeuvre_treeview.pack(side=LEFT, fill=BOTH, expand=YES, padx=20)

        self.populate_oeuvre_treeview()

        create_submit_button(self)
        create_back_button(self)

    def populate_oeuvre_treeview(self):
        from data import oeuvres

        # Clear the Treeview before populating it with new results
        for item in self.oeuvre_treeview.get_children():
            self.oeuvre_treeview.delete(item)

        # Populate the Treeview with the results
        for result in oeuvres.tuples:
            self.oeuvre_treeview.insert(
                "", ttk.END, values=result[1:], iid=result[0]
            )

        def on_treeview_select(event):
            selected_item = self.oeuvre_treeview.selection()[0]
            self.id_oeuvre.set(int(selected_item))

        self.oeuvre_treeview.bind("<<TreeviewSelect>>", on_treeview_select)

    def on_submit(self):
        if self.objectif.get() == "":
            Messagebox.show_error("Enter an objectif", "Error")
            return
        if self.theme.get() == "":
            Messagebox.show_error("Enter a theme", "Error")
            return

        if self.id_oeuvre.get() == 0:
            Messagebox.show_error("Select an oeuvre", "Error")
            return

        sql_args = (
            f" {self.id_oeuvre.get()},"
            f" '{self.objectif.get()}',"
            f" '{self.theme.get()}';"
        )

        DBManager().run_procedure_with_args("AddCasting", sql_args)
        update_data()

        Messagebox.ok("Casting added successfully", "Success")
        self.clear_form()

    def clear_form(self):
        self.objectif.set("")
        self.theme.set("")
        self.id_oeuvre.set(0)
