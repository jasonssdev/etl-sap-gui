import os
import pyodbc
from dotenv import load_dotenv
from sql_connection import open_sql_connection 

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

# Connect to SQL Server
conn = open_sql_connection(sql_server, sql_database, sql_username, sql_password)

# Function to execute a SQL command
def execute_sql_command(connection, sql_command):
    try:
        cursor = connection.cursor()
        cursor.execute(sql_command)
        connection.commit()
        print("SQL command executed successfully")
    except Exception as e:
        print(f"Error executing SQL command: {e}")

# SQL command to truncate the table
truncate_table_material = os.getenv("SQL_TRUNCATE_MATERIALS")
truncate_table_stock = os.getenv("SQL_TRUNCATE_STOCK")
truncate_table_bo2cs = os.getenv("SQL_TRUNCATE_BO2CS")
truncate_table_outbound = os.getenv("SQL_TRUNCATE_OUTBOUND")
truncate_table_inbound = os.getenv("SQL_TRUNCATE_INBOUND")

# Execute the SQL command
execute_sql_command(conn, truncate_table_material)
execute_sql_command(conn, truncate_table_stock)
execute_sql_command(conn, truncate_table_bo2cs)
execute_sql_command(conn, truncate_table_outbound)
execute_sql_command(conn, truncate_table_inbound)
