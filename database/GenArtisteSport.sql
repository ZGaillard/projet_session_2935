CREATE PROCEDURE GenerateArtisteSportTuples
    @tupleCount INT
AS
BEGIN
    DECLARE @i INT = 1;

    WHILE @i <= @tupleCount
    BEGIN
        DECLARE @val1 INT = CAST(RAND() * 100 AS INT) + 1;
        DECLARE @val2 INT = CAST(RAND() * 10 AS INT) + 1;
        IF NOT EXISTS (SELECT * FROM Artiste_Sport WHERE id_artiste = @val1 AND id_sport = @val2)
        BEGIN
            INSERT INTO Artiste_Sport (id_artiste, id_sport)
            VALUES (
                @val1,  
                @val2 
            );
        END;   

        SET @i = @i + 1;
    END;
END;





--DROP PROCEDURE GenerateArtisteSportTuples;