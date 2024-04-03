CREATE OR ALTER PROCEDURE GenerateArtisteHabitudeTuples
    @tupleCount INT
AS
BEGIN
    DECLARE @i INT = 1;

    WHILE @i <= @tupleCount
    BEGIN
        DECLARE @val1 INT = CAST(RAND() * 100 AS INT) + 1;
        DECLARE @val2 INT = CAST(RAND() * 10 AS INT) + 1;
        IF NOT EXISTS (SELECT * FROM Artiste_Habitude WHERE id_artiste = @val1 AND id_habitude = @val2)
        BEGIN
            INSERT INTO Artiste_Habitude (id_artiste, id_habitude)
            VALUES (
                @val1,  
                @val2 
            );
            SET @i = @i + 1;
        END;    
    END;
END;

--DROP PROCEDURE GenerateArtisteHabitudeTuples;
