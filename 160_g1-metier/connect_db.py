import psycopg2 
from config import CONFIG

def connect():
    conn = psycopg2.connect(
        dbname="mylittlebank",
        user="metier",
        password="",
        host=CONFIG["DB_HOST"],
        port="5432"
    )
    return conn.cursor()
