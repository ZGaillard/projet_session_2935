CREATE OR ALTER PROCEDURE AddMovies
    @titre VARCHAR(50),
    @budget INT,
    @date_sortie DATE,
    @duree INT,
    @origine VARCHAR(50),
    @langue VARCHAR(50),
    @genre VARCHAR(50),
    @id_producteur INT,
    @objectif_casting VARCHAR(50),
    @theme_casting VARCHAR(50)
AS
BEGIN

INSERT INTO Oeuvre
VALUES (@titre,@budget,@date_sortie,@duree,@origine,@langue,@genre);

DECLARE @id INT;
SELECT @id = id FROM Oeuvre WHERE titre = @titre;

INSERT INTO Film
VALUES(@id, @id_producteur);

INSERT INTO Casting
VALUES(@id, @objectif_casting, @theme_casting);

END;
