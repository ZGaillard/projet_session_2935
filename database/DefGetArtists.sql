CREATE OR ALTER PROCEDURE getArtists
AS
BEGIN
    SELECT Artiste.id, Artiste.nom, Artiste.prenom, Artiste.date_naissance, Artiste.salaire_min, Artiste.domaine, Adresse.no_civique, Adresse.rue, Adresse.ville, Adresse.code_postal, Adresse.pays, Adresse.no_appartement
    FROM Artiste
    JOIN Adresse ON Artiste.id_adresse = Adresse.id;
END;
