CREATE OR ALTER PROCEDURE AddPlays @titre VARCHAR(50), @budget INT, @date_sortie DATE, @duree INT, @origine VARCHAR(50), @langue VARCHAR(50), @genre VARCHAR(50), @theatre VARCHAR(50)
AS
BEGIN
INSERT INTO Oeuvre
VALUES (@titre,@budget,@date_sortie,@duree,@origine,@langue,@genre);
DECLARE @id INT;
SET @id = SCOPE_IDENTITY();
INSERT INTO Piece
VALUES(@id, @theatre);
END;