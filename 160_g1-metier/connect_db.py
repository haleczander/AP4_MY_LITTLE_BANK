import psycopg2
from config import CONFIG


def connect():
    conn = psycopg2.connect(
        dbname=CONFIG["DB_NAME"],
        user=CONFIG["DB_LOGIN"],
        password=CONFIG["DB_PASSWORD"],
        host=CONFIG["DB_HOST"],
        port=CONFIG["DB_PORT"],
    )
    return conn.cursor()
