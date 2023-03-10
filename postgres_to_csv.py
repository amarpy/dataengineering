import psycopg2 as db
import pandas as pd

DB_HOST = "localhost"
DB_NAME = "hrdb"
DB_USER = "postgres"
DB_PASSWORD = "postgres"

def connect_postgres_db():
    try:
        print("Connecting to database server...")
        conn = db.connect(host = DB_HOST, 
                        database = DB_NAME, 
                        user = DB_USER, 
                        password = DB_PASSWORD)
        print("Connection successful.")
        return conn
    except:
        "Connection unsuccessful"

def query_postgres_db():
    try:
        query = "SELECT employee_id, first_name, last_name, job_id FROM employees;"
        df = pd.read_sql_query(query, connect_postgres_db())
        print("Copying data to CSV...")
        df.to_csv("postgresql_output.csv")
        print("Data copied to CSV.")
    except:
        "Data not copied."
    
query_postgres_db()