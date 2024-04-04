# projet_session
 
Ce projet a pour but de créer une application graphique permettant de gérer une base de données de films.
Le projet est réalisé en Python avec l'interface graphique Tkinter. Ainsi que ttkbootstrap pour le style moderne 
des widgets. La base de données est gérée avec SQL-Server et le module pymssql.

## Installation
```bash
pip install tkinter
pip install ttkbootstrap
pip install pymssql
```

Je vous conseille d'utiliser PyCharm pour lancer le projet et vous connecter à la base de données.
Personnellement, j'utilise Azure Data Studio pour gérer la base de données et PyCharm pour le code.


**Faites une nouvelle branche lorsque vous travaillez sur le code.**

## Liste des tâches
### Application :
- [ ] Installer les modules nécessaires et faire fonctionner le code de base (connexion à la base de données)
- [ ] Créer les fenêtres pour ajouter des éléments à la base de données (`newElemMenu.py`)
  -- [ ] Films
  -- [ ] Pièces de théâtre
  -- [ ] Artistes
  -- [ ] Casting
Cette tâche parait simple, mais c'est assez complexe en fait, car il faut gérer le fait que
les données sont stockées dans plusieurs tables. Par exemple, pour ajouter un film, il faut
ajouter un tuple dans la table Film, mais aussi dans la table Œuvre. Je vous conseille de
faire des procédures puis utiliser `DBManager.run_procedure()` ou `DBManager.run_procedure_with_args()`
Il faut aussi lancer la définition de la procédure avec `DBManager.run_file()` dans `main.py`



### Base de données :
- [ ] Normaliser la base de données
  -- [ ] Faire la liste des dépendances fonctionnelles pour chaque table
  -- [ ] Expliquer pourquoi chaque table est en 1NF, 2NF, 3NF (Si ce n'est pas le cas, la normaliser en 3NF) et m'avertir pour le modifier dans le code
  -- [ ] Créer un fichier SQL pour 10 requêtes complexes
  -- [ ] Améliorer la création des tables (ajouter des contraintes, des triggers, etc.)
  -- [ ] Créer des procédures, fonctions, triggers, curseurs, views, etc. (Le but est de montrer à la prof qu'on sait utiliser ces outils)
  -- [ ] Arranger le modèle entité-association et relationnel qu'on a remi à la mi-session si nécessaire

### Rapport :
- [] Je m'en occupe, faites juste m'envoyer ce que vous avez fait pour que je puisse l'ajouter au rapport le plus tôt possible
