CREATE OR ALTER PROCEDURE AddAdresse @id INT, @no_civique INT, @rue VARCHAR(50), @ville VARCHAR(50), @code_postal VARCHAR(50), @pays VARCHAR(50), @no_appartement INT
AS
BEGIN
INSERT INTO Adresse
VALUES (@id,@no_civique,@rue,@ville,@code_postal,@pays,@no_appartement);
END;