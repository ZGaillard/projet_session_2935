SET DATEFORMAT dmy;
CREATE DATABASE CASTING
CREATE TABLE oeuvre (
    id INT PRIMARY KEY,
    titre VARCHAR(50),
    budget INT,
    date_sortie DATE,
    duree INT,
    origine VARCHAR(50),
    langue VARCHAR(50),
    genre VARCHAR(50),
);
CREATE TABLE Adresse(
    id INT PRIMARY KEY,
    no_civique INT,
    rue VARCHAR(50),
    ville VARCHAR(50),
    code_postal VARCHAR(50),
    pays VARCHAR(50),
    no_appartement INT,
);
CREATE TABLE habitude(
    id INT PRIMARY KEY,
    nom VARCHAR(50),
);
CREATE TABLE sport(
    id INT PRIMARY KEY,
    nom VARCHAR(50),
);
CREATE TABLE Compagnie(
    id INT PRIMARY KEY,
    nom VARCHAR(50),
    type_industrie VARCHAR(50),
    id_adresse INT,
    CONSTRAINT fk_compagnie_adresse FOREIGN KEY (id_adresse) REFERENCES adresse(id),
);
CREATE TABLE Film(
    id_oeuvre INT PRIMARY KEY,
    id_studio INT,
    CONSTRAINT fk_film_oeuvre FOREIGN KEY (id_oeuvre) REFERENCES oeuvre(id),
    CONSTRAINT fk_film_studio FOREIGN KEY (id_studio) REFERENCES compagnie(id)
);
CREATE TABLE Piece(
    id_oeuvre INT PRIMARY KEY,
    theatre VARCHAR(50),
    CONSTRAINT fk_piece_oeuvre FOREIGN KEY (id_oeuvre) REFERENCES oeuvre(id),
);
CREATE TABLE Scene(
    id INT PRIMARY KEY,
    titre VARCHAR(50),
    budget INT,
    type VARCHAR(50),
    id_oeuvre INT,
    CONSTRAINT fk_scene_oeuvre FOREIGN KEY (id_oeuvre) REFERENCES oeuvre(id),
);
CREATE TABLE Artiste(
    id INT PRIMARY KEY,
    nom VARCHAR(50),
    prenom VARCHAR(50),
    date_naissance DATE,
    salaire_min INT,
    domaine VARCHAR(50),
    id_adresse INT,
    CONSTRAINT fk_artiste_adresse FOREIGN KEY (id_adresse) REFERENCES adresse(id),
);
CREATE TABLE Casting(
    id_oeuvre INT PRIMARY KEY,
    objectif VARCHAR(50),
    theme VARCHAR(50),
    CONSTRAINT fk_casting_oeuvre FOREIGN KEY (id_oeuvre) REFERENCES oeuvre(id),
);

CREATE TABLE Sponsor(
    id_oeuvre INT,
    id_compagnie INT,
    montant INT,
    CONSTRAINT fk_sponsor_oeuvre FOREIGN KEY (id_oeuvre) REFERENCES oeuvre(id),
    CONSTRAINT fk_sponsor_compagnie FOREIGN KEY (id_compagnie) REFERENCES compagnie(id),
    CONSTRAINT pk_sponsor PRIMARY KEY (id_oeuvre, id_compagnie),
);
CREATE TABLE Producteur(
    id_oeuvre INT,
    id_compagnie INT,
    CONSTRAINT fk_producteur_oeuvre FOREIGN KEY (id_oeuvre) REFERENCES oeuvre(id),
    CONSTRAINT fk_producteur_compagnie FOREIGN KEY (id_compagnie) REFERENCES compagnie(id),
    CONSTRAINT pk_producteur PRIMARY KEY (id_oeuvre, id_compagnie),
);
CREATE TABLE Casting_Artiste(
    id_artiste INT,
    id_oeuvre INT,
    fonction VARCHAR(50),
    salaire INT,
    date_debut DATE,
    date_fin DATE,
    CONSTRAINT fk_casting_artiste FOREIGN KEY (id_artiste) REFERENCES artiste(id),
    CONSTRAINT fk_casting_artiste_oeuvre FOREIGN KEY (id_oeuvre) REFERENCES oeuvre(id),
    CONSTRAINT pk_casting_artiste PRIMARY KEY (id_artiste, id_oeuvre),
);

CREATE TABLE relation(
    id_artiste1 INT,
    id_artiste2 INT,
    type_relation VARCHAR(50),
    CONSTRAINT fk_relation_artiste1 FOREIGN KEY (id_artiste1) REFERENCES artiste(id),
    CONSTRAINT fk_relation_artiste2 FOREIGN KEY (id_artiste2) REFERENCES artiste(id),
    CONSTRAINT pk_relation PRIMARY KEY (id_artiste1, id_artiste2),
);
CREATE TABLE artiste_sport(
    id_artiste INT,
    id_sport INT,
    CONSTRAINT fk_artiste_sport FOREIGN KEY (id_artiste) REFERENCES artiste(id),
    CONSTRAINT fk_sport_artiste FOREIGN KEY (id_sport) REFERENCES sport(id),
    CONSTRAINT pk_artiste_sport PRIMARY KEY (id_artiste, id_sport),
);
CREATE TABLE artiste_habitude(
    id_artiste INT,
    id_habtiude INT,
    CONSTRAINT fk_artiste_habitude FOREIGN KEY (id_artiste) REFERENCES artiste(id),
    CONSTRAINT fk_habitude_artiste FOREIGN KEY (id_habitude) REFERENCES habitude(id),
    CONSTRAINT pk_artiste_sport PRIMARY KEY (id_artiste, id_habitude),
);