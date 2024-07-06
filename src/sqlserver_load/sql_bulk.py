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
        'bulk_material_moar': os.getenv('SQL_BULK_MATERIAL_MOAR'),
        'bulk_material_mocl': os.getenv('SQL_BULK_MATERIAL_MOCL'),
        'bulk_material_mobr': os.getenv('SQL_BULK_MATERIAL_MOBR'),
        'bulk_material_momx': os.getenv('SQL_BULK_MATERIAL_MOMX'),
        'bulk_stock': os.getenv('SQL_BULK_STOCK'),
        'bulk_bo2cs': os.getenv('SQL_BULK_BO2CS'),
        'bulk_inbound': os.getenv('SQL_BULK_INBOUND'),
        'bulk_outbound': os.getenv('SQL_BULK_OUTBOUND')
    }
    return env_vars

def execute_sql_bulk(connection, sql_command):
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

    # List of SQL commands to bulk the tables
    bulk_commands = [
        env_vars['bulk_material_moar'],
        env_vars['bulk_material_mocl'],
        env_vars['bulk_material_mobr'],
        env_vars['bulk_material_momx'],
        env_vars['bulk_stock'],
        env_vars['bulk_bo2cs'],
        env_vars['bulk_inbound'],
        env_vars['bulk_outbound']
    ]

    # Execute the SQL commands
    for command in bulk_commands:
        execute_sql_bulk(conn, command)

    if conn:
        # Close the connection
        close_sql_connection(conn)

if __name__ == "__main__":
    main()