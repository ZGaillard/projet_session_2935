CREATE OR ALTER PROCEDURE AddPlays @id INT, @titre VARCHAR(50), @budget INT, @date_sortie DATE, @duree INT, @origine VARCHAR(50), @langue VARCHAR(50), @genre VARCHAR(50), @theatre VARCHAR(50)
AS
BEGIN
INSERT INTO Oeuvre
VALUES (@id,@titre,@budget,@date_sortie,@duree,@origine,@langue,@genre);
INSERT INTO Piece
VALUES(@id, @theatre);
END;