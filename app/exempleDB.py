import pymssql


# Fonction de lecture des données
def read(conn):
    print("Sélection")
    with conn.cursor() as cursor:
        sql_command = "SELECT nom, prenom FROM employe;"
        cursor.execute(sql_command)
        for emp in cursor.fetchall():
            print(emp[0] + " " + emp[1])


# Fonction d'insertion de données
def create(conn):
    print("Insertion")
    with conn.cursor() as cursor:
        sql_command = "INSERT INTO employe (id, nom, prenom) VALUES (12, 'Chaabouni', 'Nader');"
        cursor.execute(sql_command)
        conn.commit()


# Fonction de mise à jour
def update(conn):
    print("Mise à jour")
    with conn.cursor() as cursor:
        sql_command = "UPDATE employe SET nom = nom + %s WHERE id = %s;"
        cursor.execute(sql_command, ("python", 10))
        conn.commit()


# Fonction de suppression
def delete(conn):
    print("Suppression")
    with conn.cursor() as cursor:
        sql_command = "DELETE FROM employe WHERE id = %s;"
        cursor.execute(sql_command, (4,))
        conn.commit()


# Chaîne de connexion
conn_str = {
    'server'    : 'localhost',
    'user'      : 'SA',
    'password'  : 'Password123',
    'database'  : 'BDTest',
    'autocommit': True
}

# Connexion
with pymssql.connect(**conn_str) as conn:
    # Appel des fonctions
    read(conn)
    create(conn)
    update(conn)
    delete(conn)
