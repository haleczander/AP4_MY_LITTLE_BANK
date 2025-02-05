import psycopg2  # type: ignore

# Connexion to DB
def connect():
    conn = psycopg2.connect(
        dbname="mabase",
        user="monutilisateur",
        password="monmotdepasse",
        host="localhost",
        port="5432"
    )
    return conn.cursor()