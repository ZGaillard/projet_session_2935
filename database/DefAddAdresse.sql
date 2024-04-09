CREATE OR ALTER PROCEDURE AddAdresse @no_civique INT, @rue VARCHAR(50), @ville VARCHAR(50), @code_postal VARCHAR(50), @pays VARCHAR(50), @no_appartement INT
AS
BEGIN
INSERT INTO Adresse
VALUES (@no_civique,@rue,@ville,@code_postal,@pays,@no_appartement);

SELECT id
FROM Adresse
WHERE no_civique = @no_civique AND rue = @rue AND ville = @ville AND code_postal = @code_postal AND pays = @pays AND no_appartement = @no_appartement;

END;