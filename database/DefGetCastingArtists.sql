CREATE OR ALTER PROCEDURE GetCastingArtists
@id_oeuvre INT
AS
BEGIN
    SELECT a.prenom, a.nom, c.fonction, c.salaire, c.date_debut, c.date_fin
    FROM Artiste a
    JOIN Casting_Artiste c ON a.id = c.id_artiste
    WHERE c.id_oeuvre = @id_oeuvre
END