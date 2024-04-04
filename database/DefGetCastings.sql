CREATE OR ALTER PROCEDURE getCastings
AS
BEGIN
    SELECT Oeuvre.id, Oeuvre.titre, Casting.objectif, Casting.theme
    FROM Casting
    JOIN Oeuvre ON Casting.id_oeuvre = Oeuvre.id;
END;