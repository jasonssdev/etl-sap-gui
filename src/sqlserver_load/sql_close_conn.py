import os
import pyodbc
from dotenv import load_dotenv
from sqlserver_load.sql_open_conn import open_sql_connection

# Get base path
base_path = os.getcwd()

# Get env path
env_path = os.path.join(base_path, '.env')

# Load environment variables from .env
load_dotenv(env_path)

# Get environment variables for SQL Server connection
sql_server = os.getenv("SQL_SERVER")
sql_database = os.getenv("SQL_DATABASE")
sql_username = os.getenv("SQL_USERNAME")
sql_password = os.getenv("SQL_PASSWORD")

# Function to close SQL Server connection
def close_sql_connection(connection):
    try:
        if connection:
            connection.close()
            print("Connection closed successfully")
    except Exception as e:
        print(f"Error closing SQL connection: {e}")

if __name__ == "__main__":
    conn = open_sql_connection(sql_server, sql_database, sql_username, sql_password)
    if conn:
        # Close the connection
        close_sql_connection(conn)


    
