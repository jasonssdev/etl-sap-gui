import os
import pyodbc
from dotenv import load_dotenv

# Get base path
base_path = os.getcwd()

# Get env path
env_path = os.path.join(base_path, '.env')

# Load environment variables from .env
load_dotenv(env_path)

# Load environment variables from .env
load_dotenv(env_path)

# Get environment variables for SQL Server connection
sql_server = os.getenv("SQL_SERVER")
sql_database = os.getenv("SQL_DATABASE")
sql_username = os.getenv("SQL_USERNAME")
sql_password = os.getenv("SQL_PASSWORD")

# Function to connect to SQL Server
def open_sql_connection(server, database, username, password):
    try:
        connection_str = (
            f"DRIVER={{ODBC Driver 17 for SQL Server}};"
            f"SERVER={server};"
            f"DATABASE={database};"
            f"UID={username};"
            f"PWD={password}"
        )
        connection = pyodbc.connect(connection_str)
        print("Successfully connected to SQL Server")
        return connection
    except Exception as e:
        print(f"Error connecting to SQL Server: {e}")
        return None
    
# Function to close SQL Server connection
def close_sql_connection(connection):
    try:
        if connection:
            connection.close()
            print("Connection closed successfully")
    except Exception as e:
        print(f"Error closing SQL connection: {e}")

# conn = open_sql_connection(sql_server, sql_database, sql_username, sql_password)

