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

# SQL command to truncate the table
bulk_materials = """
BULK INSERT dbo.tbl_SCM_materials
FROM 'C:\\Users\\sepujas\\Dev\\mat2\\data\\processed\\tbl_material_8750.csv'
WITH (
    FORMAT = 'CSV',
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '0x0A',
    FIRSTROW = 2,
    CODEPAGE = '1252'
);
"""

# Execute the SQL command
execute_sql_command(conn, bulk_materials)