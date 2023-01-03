import psycopg2
from config import config
import pandas as pd

def get_players():
    conn = None
    try:
        params = config()
        print("Connecting to the PostgreSQL database...")
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute('SELECT * FROM "Characters_Players"')
        print('number of players: ', cur.rowcount)
        row = cur.fetchone()
        
        while row is not None:
            print(row)
            row = cur.fetchone()

        cur.close()
    except (Exception,psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

if __name__ == '__main__':
    get_players()