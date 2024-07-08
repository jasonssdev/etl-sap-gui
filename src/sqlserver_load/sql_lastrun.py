import os
import pyodbc
from dotenv import load_dotenv
from sqlserver_load.sql_open_conn import open_sql_connection
from sqlserver_load.sql_close_conn import close_sql_connection
from datetime import datetime

def load_environment_variables(env_path):
    """Load environment variables from the .env file."""
    load_dotenv(env_path)
    env_vars = {
        'sql_server': os.getenv("SQL_SERVER"),
        'sql_database': os.getenv("SQL_DATABASE"),
        'sql_username': os.getenv("SQL_USERNAME"),
        'sql_password': os.getenv("SQL_PASSWORD")
    }
    return env_vars

def update_last_run(connection):
    """
    Update the LastRun column with the current datetime.

    Args:
    - connection: SQL Server connection object.
    """
    try:
        cursor = connection.cursor()
        current_time = datetime.now()
        query = "UPDATE tbl_SCM_LastRun SET LastRun = ?"
        cursor.execute(query, current_time)
        connection.commit()
        print("LastRun updated successfully")
    except pyodbc.Error as e:
        print(f"Error updating LastRun: {e}")

def main():
    # Get base path
    base_path = os.getcwd()

    # Get env path
    env_path = os.path.join(base_path, '.env')

    # Load environment variables
    env_vars = load_environment_variables(env_path)

    # Connect to SQL Server
    conn = open_sql_connection(env_vars['sql_server'], env_vars['sql_database'], env_vars['sql_username'], env_vars['sql_password'])

    if conn:
        # Update the LastRun column
        update_last_run(conn)

        # Close the connection
        close_sql_connection(conn)

if __name__ == "__main__":
    main()
