import os
import pyodbc
from dotenv import load_dotenv

def load_env_variables():
    """Load environment variables from the .env file."""
    base_path = os.getcwd()
    env_path = os.path.join(base_path, '.env')
    load_dotenv(env_path)
    return {
        'sql_server': os.getenv("SQL_SERVER"),
        'sql_database': os.getenv("SQL_DATABASE"),
        'sql_username': os.getenv("SQL_USERNAME"),
        'sql_password': os.getenv("SQL_PASSWORD")
    }

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

if __name__ == "__main__":
    env_vars = load_env_variables()
    conn = open_sql_connection(env_vars['sql_server'], env_vars['sql_database'], env_vars['sql_username'], env_vars['sql_password'])
