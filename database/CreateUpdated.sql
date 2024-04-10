SET DATEFORMAT dmy;

--CREATE DATABASE CASTINGAPP;


USE CASTINGAPP;

DROP TABLE IF EXISTS Artiste_Habitude;
DROP TABLE IF EXISTS Artiste_Sport;
DROP TABLE IF EXISTS Casting_Artiste;
DROP TABLE IF EXISTS Relation;
DROP TABLE IF EXISTS Sponsor;
DROP TABLE IF EXISTS Producteur;
DROP TABLE IF EXISTS Habitude;
DROP TABLE IF EXISTS Sport;
DROP TABLE IF EXISTS Film;
DROP TABLE IF EXISTS Compagnie;
DROP TABLE IF EXISTS Piece;
DROP TABLE IF EXISTS Scene;


DROP TABLE IF EXISTS Casting;


DROP TABLE IF EXISTS Artiste;
DROP TABLE IF EXISTS Oeuvre;

DROP TABLE IF EXISTS Adresse;



CREATE TABLE Oeuvre (
    id INT IDENTITY(1,1) PRIMARY KEY,
    titre VARCHAR(50),
    budget INT,
    date_sortie DATE,
    duree INT,
    origine VARCHAR(50),
    langue VARCHAR(50),
    genre VARCHAR(50),
    CONSTRAINT chk_budget_positive CHECK (budget >= 0),
    CONSTRAINT chk_duree_positive CHECK (duree >= 0),
    CONSTRAINT chk_date_sortie CHECK (date_sortie <= GETDATE()),
    CONSTRAINT chk_date_fin_not_null_oeuvre CHECK (date_sortie IS NOT NULL),
);
CREATE TABLE Adresse(
    id INT IDENTITY(1,1) PRIMARY KEY,
    no_civique INT,
    rue VARCHAR(50),
    ville VARCHAR(50),
    code_postal VARCHAR(50),
    pays VARCHAR(50),
    no_appartement INT,
    CONSTRAINT chk_no_civique CHECK (no_civique >= 0),
    CONSTRAINT uc_no_civique UNIQUE (no_civique),
    CONSTRAINT chk_no_appartement CHECK (no_appartement >= 0),
    CONSTRAINT chk_code_postal_not_null CHECK (code_postal IS NOT NULL),    
);
CREATE TABLE Habitude(
    id INT IDENTITY(1,1) PRIMARY KEY,
    nom VARCHAR(50),
    CONSTRAINT chk_nom_habit CHECK (nom is not null),
);
CREATE TABLE Sport(
    id INT IDENTITY(1,1) PRIMARY KEY,
    nom VARCHAR(50),
    CONSTRAINT chk_nom_sport CHECK (nom is not null),
);
CREATE TABLE Compagnie(
    id INT IDENTITY(1,1) PRIMARY KEY,
    nom VARCHAR(50),
    type_industrie VARCHAR(50),
    id_adresse INT,
    CONSTRAINT fk_compagnie_adresse FOREIGN KEY (id_adresse) REFERENCES Adresse(id),
);
CREATE TABLE Film(
    id_oeuvre INT PRIMARY KEY,
    id_studio INT,
    CONSTRAINT fk_film_oeuvre FOREIGN KEY (id_oeuvre) REFERENCES Oeuvre(id),
    CONSTRAINT fk_film_studio FOREIGN KEY (id_studio) REFERENCES Compagnie(id),
    CONSTRAINT chk_studio_not_null CHECK (id_studio is not null), 
);

CREATE TABLE Piece(
    id_oeuvre INT PRIMARY KEY,
    theatre VARCHAR(50),
    CONSTRAINT fk_piece_oeuvre FOREIGN KEY (id_oeuvre) REFERENCES Oeuvre(id),
    CONSTRAINT chk_theatre CHECK (theatre is not null), 
);
CREATE TABLE Scene(
    id INT IDENTITY(1,1) PRIMARY KEY,
    titre VARCHAR(50) NOT NULL,
    budget INT,
    type VARCHAR(50) NOT NULL,
    id_oeuvre INT,
    CONSTRAINT chk_budget CHECK (budget >= 0),
    CONSTRAINT chk_titre_length CHECK (LEN(titre) <= 50),
    CONSTRAINT chk_type_length CHECK (LEN(type) <= 50),
    CONSTRAINT fk_scene_oeuvre FOREIGN KEY (id_oeuvre) REFERENCES Oeuvre(id)
);

CREATE TABLE Artiste(
    id INT IDENTITY(1,1) PRIMARY KEY,
    nom VARCHAR(50) NOT NULL,
    prenom VARCHAR(50) NOT NULL,
    date_naissance DATE NOT NULL,
    salaire_min INT,
    domaine VARCHAR(50),
    id_adresse INT,
    CONSTRAINT fk_artiste_adresse FOREIGN KEY (id_adresse) REFERENCES Adresse(id),
    CONSTRAINT chk_salaire_artist CHECK (salaire_min >= 0),
    CONSTRAINT chk_nom_length CHECK (LEN(nom) <= 50),
    CONSTRAINT chk_prenom_length CHECK (LEN(prenom) <= 50)
);
CREATE TABLE Casting(
    id_oeuvre INT PRIMARY KEY,
    objectif VARCHAR(50),
    theme VARCHAR(50),
    CONSTRAINT fk_casting_oeuvre FOREIGN KEY (id_oeuvre) REFERENCES Oeuvre(id), 
    CONSTRAINT chk_objectif_not_null CHECK (objectif IS NOT NULL),
    CONSTRAINT chk_theme_not_null CHECK (theme IS NOT NULL),
    CONSTRAINT chk_objectif_length CHECK (LEN(objectif) <= 50),
    CONSTRAINT chk_theme_length CHECK (LEN(theme) <= 50),
);

CREATE TABLE Sponsor(
    id_oeuvre INT,
    id_compagnie INT,
    montant INT,
    CONSTRAINT fk_sponsor_oeuvre FOREIGN KEY (id_oeuvre) REFERENCES Oeuvre(id),
    CONSTRAINT fk_sponsor_compagnie FOREIGN KEY (id_compagnie) REFERENCES Compagnie(id),
    CONSTRAINT pk_sponsor PRIMARY KEY (id_oeuvre, id_compagnie),
    CONSTRAINT chk_montant CHECK (montant >= 0),
);
CREATE TABLE Producteur(
    id_oeuvre INT,
    id_compagnie INT,
    CONSTRAINT fk_producteur_oeuvre FOREIGN KEY (id_oeuvre) REFERENCES Oeuvre(id),
    CONSTRAINT fk_producteur_compagnie FOREIGN KEY (id_compagnie) REFERENCES Compagnie(id),
    CONSTRAINT pk_producteur PRIMARY KEY (id_oeuvre, id_compagnie), 
);
CREATE TABLE Casting_Artiste(
    id_artiste INT,
    id_oeuvre INT,
    fonction VARCHAR(50),
    salaire INT,
    date_debut DATE,
    date_fin DATE,
    CONSTRAINT fk_casting_artiste FOREIGN KEY (id_artiste) REFERENCES Artiste(id),
    CONSTRAINT fk_casting_artiste_oeuvre FOREIGN KEY (id_oeuvre) REFERENCES Oeuvre(id),
    CONSTRAINT pk_casting_artiste PRIMARY KEY (id_artiste, id_oeuvre),
    CONSTRAINT chk_date CHECK (date_debut <= date_fin),
    CONSTRAINT chk_salaire_casting_artist CHECK (salaire >= 0),
    CONSTRAINT chk_fonction CHECK (fonction is not null),
    CONSTRAINT chk_date_debut_not_null CHECK (date_debut IS NOT NULL),
    CONSTRAINT chk_date_fin_not_null_casting_artist CHECK (date_fin IS NOT NULL),
);
CREATE TABLE Relation(
    id_artiste1 INT,
    id_artiste2 INT,
    type_relation VARCHAR(50),
    CONSTRAINT fk_relation_artiste1 FOREIGN KEY (id_artiste1) REFERENCES Artiste(id),
    CONSTRAINT fk_relation_artiste2 FOREIGN KEY (id_artiste2) REFERENCES Artiste(id),
    CONSTRAINT pk_relation PRIMARY KEY (id_artiste1, id_artiste2),
    CONSTRAINT chk_type_relation_not_null CHECK (type_relation IS NOT NULL),
    CONSTRAINT chk_type_relation_length CHECK (LEN(type_relation) <= 50),
);
CREATE TABLE Artiste_Sport(
    id_artiste INT,
    id_sport INT,
    CONSTRAINT fk_artiste_sport FOREIGN KEY (id_artiste) REFERENCES Artiste(id),
    CONSTRAINT fk_sport_artiste FOREIGN KEY (id_sport) REFERENCES Sport(id),
    CONSTRAINT pk_artiste_sport PRIMARY KEY (id_artiste, id_sport),
);
CREATE TABLE Artiste_Habitude(
    id_artiste INT,
    id_habitude INT,
    CONSTRAINT fk_artiste_habitude FOREIGN KEY (id_artiste) REFERENCES Artiste(id),
    CONSTRAINT fk_habitude_artiste FOREIGN KEY (id_habitude) REFERENCES Habitude(id),
    CONSTRAINT pk_artiste_habitude PRIMARY KEY (id_artiste, id_habitude),
);