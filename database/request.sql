--Simple requests

--1)Voir toutes les oeuvres qui ont un budget de plus de 20 000 000
SELECT * FROM Oeuvre WHERE budget > 20000000;

--2)Voir le titre de tous les films qui sont sortis après 2010 des États-Unis
SELECT Oeuvre.titre, Oeuvre.origine, Oeuvre.date_sortie
FROM Oeuvre
JOIN Film ON Oeuvre.id = Film.id_oeuvre
WHERE date_sortie >= '2010-01-01' AND origine = 'USA';

--3)Voir les pièces de théâtre qui sont des drames
SELECT Oeuvre.titre, Oeuvre.genre
FROM Oeuvre
JOIN Piece ON Oeuvre.id = Piece.id_oeuvre
WHERE genre = 'Drame';

--4)Voir le montant du sponsor qui contribue le plus
SELECT MAX(Sponsor.montant) as montant_max
FROM Compagnie
JOIN Sponsor ON Compagnie.id = Sponsor.id_compagnie

--5)Voir tous le nom et le prénom de tous gens qui auditionnent pour être un upporting actor
select Artiste.nom, Artiste.prenom, Casting_Artiste.fonction
from Casting_Artiste
JOIN Artiste ON Casting_Artiste.id_artiste = Artiste.id
WHERE fonction = 'Supporting Actor'

--Complex requests

--6)Voir le nom et le prénom de l'artiste qui a auditionné pour le rôle de lead actress dans le l'oeuvre Zodiac
SELECT Casting_artiste_noms.prenom, Casting_artiste_noms.nom, Oeuvre.titre
from (select Artiste.nom, Artiste.prenom, Casting_Artiste.fonction, Casting_Artiste.id_oeuvre
from Casting_Artiste
JOIN Artiste ON Casting_Artiste.id_artiste = Artiste.id) AS Casting_artiste_noms
JOIN Oeuvre ON Casting_artiste_noms.id_oeuvre = Oeuvre.id
WHERE titre = 'Zodiac';

--7)Voir le nom et le prénom de tous les artistes qui sont rivals
Select Artiste.prenom, Artiste.nom, Rival.prenom as prenom_rival, Rival.nom as nom_rival, Rival.type_relation, Artiste.id as id_1, Rival.id as id_2
FROM
    (Select Artiste.prenom, Artiste.nom, Artiste.id, Relation.id_artiste1,Relation.type_relation
    FROM Artiste
    JOIN Relation ON Artiste.id = Relation.id_artiste2
    ) AS Rival
JOIN Artiste ON Rival.id_artiste1 = Artiste.id
WHERE type_relation = 'Rivals';

--8)Voir le budget moyen d'une pièce de théâtre selon le genre
SELECT Oeuvre.genre, AVG(Oeuvre.budget) as avg_budget
FROM Oeuvre
JOIN Piece ON Oeuvre.id = Piece.id_oeuvre
GROUP BY genre;

--9)Voir le profil de tous les artistes dont les auditions ont terminé après la date courante
SELECT *
from (select Artiste.nom, Artiste.prenom, Artiste.date_naissance, Artiste.salaire_min, Artiste.domaine, Casting_Artiste.date_fin
from Casting_Artiste
JOIN Artiste ON Casting_Artiste.id_artiste = Artiste.id) AS Cast
WHERE date_fin > GETDATE();

--10)Voir tout les titres de films avec un budget total pour les scènes qui ne dépasse pas 100 000
SELECT Oeuvre.titre, SUM(Scene.budget) as budget_total_scenes
FROM Scene
JOIN Oeuvre ON Scene.id_oeuvre = Oeuvre.id
GROUP BY Oeuvre.titre
HAVING SUM(Scene.budget) <= 100000;