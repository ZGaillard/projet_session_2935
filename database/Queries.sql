USE CASTINGAPP;
GO

CREATE OR ALTER PROCEDURE getMovies
AS
BEGIN
    SELECT Oeuvre.titre, Oeuvre.budget, Oeuvre.date_sortie, Oeuvre.duree, Oeuvre.origine, Oeuvre.langue, Oeuvre.genre, Compagnie.nom AS nom_studio
    FROM Oeuvre
    JOIN Film ON Oeuvre.id = Film.id_oeuvre
    JOIN Compagnie ON Film.id_studio = Compagnie.id;
END;

GO

CREATE OR ALTER PROCEDURE getPlays
AS
BEGIN
    SELECT Oeuvre.titre, Oeuvre.budget, Oeuvre.date_sortie, Oeuvre.duree, Oeuvre.origine, Oeuvre.langue, Oeuvre.genre, Piece.theatre
    FROM Oeuvre
    JOIN Piece ON Oeuvre.id = Piece.id_oeuvre
END;

GO


-- Artiste(id, nom, prenom, date_naissance, salaire_min, domaine, id_adresse)
-- Adresse(id, no_civique, rue, ville, code_postal, pays, no_appartement)
CREATE OR ALTER PROCEDURE getArtists
AS
BEGIN
    SELECT Artiste.nom, Artiste.prenom, Artiste.date_naissance, Artiste.salaire_min, Artiste.domaine, Adresse.no_civique, Adresse.rue, Adresse.ville, Adresse.code_postal, Adresse.pays, Adresse.no_appartement
    FROM Artiste
    JOIN Adresse ON Artiste.id_adresse = Adresse.id;
END;

GO

CREATE OR ALTER PROCEDURE getActors
AS
BEGIN
    SELECT Artiste.nom, Artiste.prenom, Artiste.date_naissance, Artiste.salaire_min, Artiste.domaine, Adresse.no_civique, Adresse.rue, Adresse.ville, Adresse.code_postal, Adresse.pays, Adresse.no_appartement
    FROM Artiste
    JOIN Adresse ON Artiste.id_adresse = Adresse.id
    WHERE Artiste.domaine = 'Acteur';
END;

GO

-- Casting(id_oeuvre, objectif, theme)
-- Oeuvre(id, titre, budget, date_sortie, duree, origine, langue, genre)
CREATE OR ALTER PROCEDURE getCastings
AS
BEGIN
    SELECT Oeuvre.titre, Casting.objectif, Casting.theme
    FROM Casting
    JOIN Oeuvre ON Casting.id_oeuvre = Oeuvre.id;
END;