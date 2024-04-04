CREATE OR ALTER PROCEDURE getArtistHabits
    @artistId INT
AS
    BEGIN
        -- Get all habits of the artist
        SELECT a.nom, a.prenom, h.nom AS Habitude
        FROM Artiste a
        INNER JOIN Artiste_Habitude ah ON a.id = ah.id_artiste
        INNER JOIN Habitude h ON ah.id_habitude = h.id
        WHERE a.id = @artistId
    END
