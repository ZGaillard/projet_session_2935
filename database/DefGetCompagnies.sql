CREATE OR ALTER PROCEDURE getCompagnies
AS
BEGIN
    SELECT * FROM Compagnie JOIN Adresse ON Compagnie.id_adresse = Adresse.id
END;