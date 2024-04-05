CREATE OR ALTER PROCEDURE getPlays
AS
BEGIN
    SELECT Oeuvre.id, Oeuvre.titre, Oeuvre.budget, Oeuvre.date_sortie, Oeuvre.duree, Oeuvre.origine, Oeuvre.langue, Oeuvre.genre, Piece.theatre
    FROM Oeuvre
    JOIN Piece ON Oeuvre.id = Piece.id_oeuvre
END;
