CREATE OR ALTER PROCEDURE getMovies
AS
BEGIN
    SELECT Oeuvre.titre, Oeuvre.budget, Oeuvre.date_sortie, Oeuvre.duree, Oeuvre.origine, Oeuvre.langue, Oeuvre.genre, Compagnie.nom AS nom_studio
    FROM Oeuvre
    JOIN Film ON Oeuvre.id = Film.id_oeuvre
    JOIN Compagnie ON Film.id_studio = Compagnie.id;
END;