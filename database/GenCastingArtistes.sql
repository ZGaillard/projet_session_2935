CREATE OR ALTER PROCEDURE GenerateCastingArtistesTuples
    @tupleCount INT
AS
BEGIN
    DROP TABLE IF EXISTS Fonction;
    CREATE TABLE Fonction
    (
        id_f INT IDENTITY(1, 1) PRIMARY KEY,
        fonction NVARCHAR(50) NOT NULL
    );
    INSERT INTO Fonction
    VALUES 
    ('Acteur'), ('Réalisateur'),
    ('Scénariste'), ('Producteur'),
    ('Compositeur'), ('Monteur'),
    ('Directeur de la photographie'), ('Ingénieur du son'),
    ('Costumier'), ('Maquilleur'),
    ('Cascadeur'), ('Doublure'),
    ('Chorégraphe'), ('Photographe'),
    ('Cadreur'), ('Scripte'),
    ('Dresseur'), ('Cantinier'),
    ('Chauffeur'), ('Assistant'),
    ('Stagiaire'), ('Figurant'), 
    ('Doublure voix'), ('Traducteur'), ('Interprète');

    DECLARE @i INT = 1; 
    WHILE @i <= @tupleCount
    BEGIN
        DECLARE @id_artiste INT = (SELECT CAST(RAND() * 98 + 1 AS INT));
        DECLARE @id_oeuvre INT = (SELECT CAST(RAND() * 98 + 1 AS INT));
        DECLARE @id_fonction INT = (SELECT CAST(RAND() * 23 + 1 AS INT));

        IF NOT EXISTS (SELECT * FROM Casting_Artiste WHERE id_artiste = @id_artiste AND id_oeuvre = @id_oeuvre)
        BEGIN
            INSERT INTO Casting_Artiste
            VALUES (
                @id_artiste, @id_oeuvre, 
                (SELECT fonction FROM Fonction WHERE id_f = @id_fonction),
                CAST(RAND() * 1000 AS DECIMAL(10, 2)), 
                DATEADD(DAY, CAST(RAND() * 3650 AS INT), '2010-01-01'),
                DATEADD(DAY, CAST(RAND() * 3650 AS INT), '2020-01-01')
            );
            SET @i = @i + 1;
        END
    END
END

