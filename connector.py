import psycopg2
from config import config
import pandas as pd

def get_table(table_name):
    conn = None
    try:
        params = config()
        print("Connecting to the PostgreSQL database...")
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f'SELECT * FROM "{table_name}" LIMIT 0')
        colnames = [desc[0] for desc in cur.description]
        #print(colnames)
        cur.execute(f'SELECT * FROM "{table_name}"')
        df = pd.DataFrame(cur.fetchall(), columns=colnames)
        #print(df)
        cur.close()
        return df
    except (Exception,psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

#if __name__ == '__main__':
    #get_table("Characters_Players")