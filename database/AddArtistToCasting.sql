CREATE OR ALTER PROCEDURE AddArtistToCasting @id_artist INT, @id_casting INT, @fonction VARCHAR(50), @salaire INT, @date_debut DATE, @date_fin DATE
AS
BEGIN
INSERT INTO Casting_Artiste
(id_artiste, id_oeuvre, fonction, salaire, date_debut, date_fin)
VALUES (@id_artist, @id_casting, @fonction, @salaire, @date_debut, @date_fin);
END;