import pyodbc  # ce module doit être importé quand on souhaite se connecter à un serveur de BD en python


# lire des données
def read(conn):
    print("select")
    conn.execute("set transaction isolation level read uncommitted;")
    curseur = conn.cursor()
    sqlCommand = "select nom, prenom from employe;"
    curseur.execute(sqlCommand)
    for emp in curseur.fetchall():
        print(emp[0] + " " + emp[1])
    curseur.close()


# insérer des données
def create(conn):
    print("insert")
    curseur = conn.cursor()
    sqlcommand = "insert into employe (id,nom, prenom) values (12,'Chaabouni','Nader') ;"
    curseur.execute(sqlcommand)
    conn.commit()
    curseur.close()


# mise à jour
def update(conn):
    print("update")
    curseur = conn.cursor()

    # les 2 "?" Représente une valeur à fournir durant l'exécution
    sqlCommand = "update employe set nom=nom+? where id=?;"
    # ces 2 "?" Seront remplacés par les valeurs pthon et 10
    curseur.execute(sqlCommand, ("python", 10))
    conn.commit()
    curseur.close()


def delete(conn):
    print("delete")
    curseur = conn.cursor()
    sqlCommand = "delete from employe where id=?;"
    curseur.execute(sqlCommand, (4))
    conn.commit()
    curseur.close()


# programme principal

###chaine de connexion
conn_str = (
    "Driver=ODBC Driver 17 for SQL Server;"
    "Server=localhost;"
    "Database=master;"
    "Encrypt=yes;"
    "TrustServerCertificate=yes;"
    "Trusted_Connection=yes;"
)

###connexion
cnxn = pyodbc.connect(conn_str)

###appel des fonctions
read(cnxn)
create(cnxn)
update(cnxn)
delete(cnxn)

###fermer la connexion
cnxn.close()
