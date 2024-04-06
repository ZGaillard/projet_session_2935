from DBManager import DBManager


class Data:
    def __init__(self, tuples, column_names):
        self.tuples = tuples
        self.column_names = column_names

    def get_tuples(self):
        return self.tuples

    def get_column_names(self):
        return self.column_names

    def insert(self, data_tuple):
        self.tuples.append(data_tuple)

    def delete(self, data_tuple):
        self.tuples.remove(data_tuple)

    def update(self, data_tuple):
        index = self.tuples.index(data_tuple)
        self.tuples[index] = data_tuple


# Data objects
movies = Data(
    DBManager().run_procedure("getMovies"),
    [
        "Titre",
        "Budget",
        "Date de Sortie",
        "Durée",
        "Origine",
        "Langue",
        "Genre",
        "Nom du Studio",
    ],
)


theater_plays = Data(
    DBManager().run_procedure("getPlays"),
    [
        "Titre",
        "Budget",
        "Date de Sortie",
        "Durée",
        "Origine",
        "Langue",
        "Genre",
        "Nom du théâtre",
    ],
)


artists = Data(
    DBManager().run_procedure("getArtists"),
    [
        "Nom",
        "Prénom",
        "Date de Naissance",
        "Salaire Min",
        "Domaine",
        "No Civique",
        "Rue",
        "Ville",
        "Code Postal",
        "Pays",
        "No Appartement",
    ],
)

castings = Data(
    DBManager().run_procedure("getCastings"),
    ["Titre de l'Oeuvre", "Objectif", "Thème"]
)

compagnies = Data(
    DBManager().run_procedure("getCompagnies"),
    [
        "Nom",
        "Type Industrie",
        "No Civique",
        "Rue",
        "Ville",
        "Code Postal",
        "Pays",
        "No Appartement",
    ],
)
