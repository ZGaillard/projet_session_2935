CREATE OR ALTER PROCEDURE addCasting
    @id_oeuvre INT,
    @objectif VARCHAR(50),
    @theme VARCHAR(50)
AS
BEGIN
    INSERT INTO Casting (id_oeuvre, objectif, theme)
    VALUES (@id_oeuvre, @objectif, @theme)
END