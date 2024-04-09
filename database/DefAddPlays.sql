CREATE OR ALTER PROCEDURE AddPlays
    @titre VARCHAR(50),
    @budget INT,
    @date_sortie DATE,
    @duree INT,
    @origine VARCHAR(50),
    @langue VARCHAR(50),
    @genre VARCHAR(50),
    @theatre VARCHAR(50)
AS
BEGIN
INSERT INTO Oeuvre
VALUES (@titre,@budget,@date_sortie,@duree,@origine,@langue,@genre);

DECLARE @id_oeuvre INT;
SELECT @id_oeuvre = id FROM Oeuvre WHERE titre = @titre;

INSERT INTO Piece
VALUES(@id_oeuvre, @theatre);
END;