import os
import pyodbc
from dotenv import load_dotenv
from sql_connection import open_sql_connection, close_sql_connection

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

# SQL command to bulk the table
bulk_material_moar = os.getenv('SQL_BULK_MATERIAL_MOAR')
bulk_material_mocl = os.getenv('SQL_BULK_MATERIAL_MOCL')
bulk_material_mobr = os.getenv('SQL_BULK_MATERIAL_MOBR')
bulk_material_momx = os.getenv('SQL_BULK_MATERIAL_MOMX')
bulk_stock = os.getenv('SQL_BULK_STOCK')
bulk_bo2cs = os.getenv('SQL_BULK_BO2CS')
bulk_inbound = os.getenv('SQL_BULK_INBOUND')
bulk_outbound = os.getenv('SQL_BULK_OUTBOUND')

# Execute the SQL command
execute_sql_command(conn, bulk_material_moar)
execute_sql_command(conn, bulk_material_mocl)
execute_sql_command(conn, bulk_material_mobr)
execute_sql_command(conn, bulk_material_momx)
execute_sql_command(conn, bulk_stock)
execute_sql_command(conn, bulk_bo2cs)
execute_sql_command(conn, bulk_inbound)
execute_sql_command(conn, bulk_outbound)