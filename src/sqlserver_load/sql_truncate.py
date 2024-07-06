import os
import pyodbc
from dotenv import load_dotenv
from sqlserver_load.sql_open_conn import open_sql_connection
from sqlserver_load.sql_close_conn import close_sql_connection


def load_environment_variables(env_path):
    """Load environment variables from the .env file."""
    load_dotenv(env_path)
    env_vars = {
        'sql_server': os.getenv("SQL_SERVER"),
        'sql_database': os.getenv("SQL_DATABASE"),
        'sql_username': os.getenv("SQL_USERNAME"),
        'sql_password': os.getenv("SQL_PASSWORD"),
        'truncate_table_materials': os.getenv("SQL_TRUNCATE_MATERIALS"),
        'truncate_table_stock': os.getenv("SQL_TRUNCATE_STOCK"),
        'truncate_table_bo2cs': os.getenv("SQL_TRUNCATE_BO2CS"),
        'truncate_table_outbound': os.getenv("SQL_TRUNCATE_OUTBOUND"),
        'truncate_table_inbound': os.getenv("SQL_TRUNCATE_INBOUND")
    }
    return env_vars

def execute_sql_truncate(connection, sql_command):
    """
    Execute a SQL command on the given connection.
    
    Args:
    - connection: SQL Server connection object.
    - sql_command (str): SQL command to execute.
    """
    try:
        cursor = connection.cursor()
        cursor.execute(sql_command)
        connection.commit()
        print("SQL command executed successfully")
    except pyodbc.Error as e:
        print(f"Error executing SQL command: {e}")

def main():
    # Get base path
    base_path = os.getcwd()

    # Get env path
    env_path = os.path.join(base_path, '.env')

    # Load environment variables
    env_vars = load_environment_variables(env_path)

    # Connect to SQL Server
    conn = open_sql_connection(env_vars['sql_server'], env_vars['sql_database'], env_vars['sql_username'], env_vars['sql_password'])

    # List of SQL commands to truncate tables
    truncate_commands = [
        env_vars['truncate_table_materials'],
        env_vars['truncate_table_stock'],
        env_vars['truncate_table_bo2cs'],
        env_vars['truncate_table_outbound'],
        env_vars['truncate_table_inbound']
    ]

    # Execute the SQL commands
    for command in truncate_commands:
        execute_sql_truncate(conn, command)

    if conn:
        # Close the connection
        close_sql_connection(conn)
        
if __name__ == "__main__":
    main()
