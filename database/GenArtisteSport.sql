CREATE PROCEDURE GenerateArtisteSportTuples
    @tupleCount INT
AS
BEGIN
    DECLARE @i INT = 1;

    WHILE @i <= @tupleCount
    BEGIN
        INSERT INTO Artiste_Sport (id_artiste, id_sport)
        VALUES (
            CAST(RAND() * 100 AS INT) + 1,  
            CAST(RAND() * 10 AS INT) + 1 
        );

        SET @i = @i + 1;
    END;
END;

EXEC GenerateArtisteSportTuples @tupleCount = 100;