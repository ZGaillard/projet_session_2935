CREATE OR ALTER PROCEDURE AddArtist @nom VARCHAR(50), @prenom VARCHAR(50), @date_naissance DATE, @salaire_min INT, @domaine VARCHAR(50), @no_civique INT, @rue VARCHAR(50), @ville VARCHAR(50), @code_postal VARCHAR(50), @pays VARCHAR(50), @no_appartement INT
AS
BEGIN
INSERT INTO Adresse
VALUES (@no_civique, @rue, @ville, @code_postal, @pays, @no_appartement);
DECLARE @id INT;
SET @id = SCOPE_IDENTITY();
INSERT INTO Artiste
VALUES (@nom,@prenom,@date_naissance,@salaire_min,@domaine,@id);
END;