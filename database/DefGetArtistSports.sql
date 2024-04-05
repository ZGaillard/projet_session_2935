CREATE OR ALTER PROCEDURE getArtistSports
    @artistId INT
AS
    BEGIN
        -- Get the sports of an artist
        SELECT a.nom, a.prenom, s.nom AS sport
        FROM Artiste a
        INNER JOIN Artiste_Sport asp ON a.id = asp.id_artiste
        INNER JOIN Sport s ON asp.id_sport = s.id
        WHERE a.id = @artistId
    END
