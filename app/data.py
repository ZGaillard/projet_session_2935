from app.DBManager import DBManager


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

#Oeuvre.titre, Oeuvre.budget, Oeuvre.date_sortie, Oeuvre.duree, Oeuvre.origine, Oeuvre.langue, Oeuvre.genre, Compagnie.nom AS nom_studio
# Data objects
movies = Data(
    DBManager().run_function("GetMovies"),
    ["titre", "budget", "date_sortie", "duree", "origine", "langue", "genre", "nom_studio"]
)


theater_plays = Data(
    DBManager().read("Piece", "*"),
    ["id_piece", "id_theater"]
)

