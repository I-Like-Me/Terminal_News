import psycopg2
from config import config
import pandas as pd


def connect_table(table_name):
    conn = None
    try:
        params = config()
        print("Connecting to the PostgreSQL database...")
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f'SELECT * FROM "{table_name}" LIMIT 0')
        colnames = [desc[0] for desc in cur.description]
        cur.execute(f'SELECT * FROM "{table_name}"')
        df = pd.DataFrame(cur.fetchall(), columns=colnames)
        cur.close()
        return df
    except (Exception,psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


def connect_columns(table_name, *cols):
    conn = None
    str_cols = ""
    for col in cols:
        str_cols = str_cols + col + ", "
    cols = str_cols[:-2]
    try:
        params = config()
        print("Connecting to the PostgreSQL database...")
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f'SELECT {cols} FROM "{table_name}" LIMIT 0')
        colnames = [desc[0] for desc in cur.description]
        cur.execute(f'SELECT {cols}  FROM "{table_name}"')
        df = pd.DataFrame(cur.fetchall(), columns=colnames)
        cur.close()
        return df
    except (Exception,psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')    

#if __name__ == '__main__':
    #connect_columns("Characters_Players", "name", "origin")