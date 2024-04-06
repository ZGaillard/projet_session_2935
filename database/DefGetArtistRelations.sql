CREATE OR ALTER PROCEDURE getArtistRelations
    @artistId INT
AS
    BEGIN
        -- Get all habits of the artist
        SELECT a.nom, a.prenom, r.type_relation
        FROM Artiste a
        INNER JOIN Relation r ON a.id = r.id_artiste1
        WHERE r.id_artiste2 = @artistId
        UNION
        SELECT a.nom, a.prenom, r.type_relation
        FROM Artiste a
        INNER JOIN Relation r ON a.id = r.id_artiste2
        WHERE r.id_artiste1 = @artistId
    END
