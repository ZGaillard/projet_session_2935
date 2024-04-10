CREATE OR ALTER PROCEDURE AddMovies
    @titre VARCHAR(50),
    @budget INT,
    @date_sortie DATE,
    @duree INT,
    @origine VARCHAR(50),
    @langue VARCHAR(50),
    @genre VARCHAR(50),
    @id_producteur INT
AS
BEGIN

INSERT INTO Oeuvre
VALUES (@titre,@budget,@date_sortie,@duree,@origine,@langue,@genre);

DECLARE @id INT;
SELECT @id = id FROM Oeuvre WHERE titre = @titre;

INSERT INTO Film
VALUES(@id, @id_producteur);

SELECT @id; -- return the id of the new movie for casting creation
END;
