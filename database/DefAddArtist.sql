CREATE OR ALTER PROCEDURE AddArtist @id INT, @nom VARCHAR(50), @prenom VARCHAR(50), @date_naissance DATE, @salaire_min INT, @domaine VARCHAR(50), @id_adresse INT
AS
BEGIN
INSERT INTO Artiste
VALUES (@id,@nom,@prenom,@date_naissance,@salaire_min,@domaine,@id_adresse);
END;