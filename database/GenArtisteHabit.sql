CREATE PROCEDURE GenerateArtisteHabitudeTuples 
    @tupleCount INT
AS
BEGIN
    DECLARE @i INT = 1;

    WHILE @i <= @tupleCount
    BEGIN
        INSERT INTO Artiste_Habitude (id_artiste, id_habitude)
        VALUES (
            CAST(RAND() * 100 AS INT) + 1,  
            CAST(RAND() * 10 AS INT) + 1 
        );

        SET @i = @i + 1;
    END;
END;

EXEC GenerateArtisteHabitudeTuples @tupleCount = 100;