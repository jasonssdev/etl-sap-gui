import os
import time
from datetime import datetime
import pandas as pd
from dotenv import load_dotenv
from sap_extract.sap_open import open_sap_gui
from sap_extract.sap_login import login_to_sap
from sap_extract.sap_session import get_active_session
from sap_extract.sap_download_bo2cs import download_report_zbo2cs
from sap_extract.sap_download_inbound import download_inbound_report
from sap_extract.sap_download_material_moar import download_material_report
from sap_extract.sap_download_mb52 import download_report_mb52
from sap_extract.sap_download_outbound import download_outbound_report
from sap_extract.sap_logout import logout_from_sap
from sap_extract.sap_close import close_sap_logon
from scripts_transform.transform_bo2cs import transform_bo2cs
from scripts_transform.transform_inbound import transform_inbound
# from scripts_transform.transform_mat_3000 import transform_mat_3000
# from scripts_transform.transform_mat_8300 import transform_mat_8300
# from scripts_transform.transform_mat_8650 import transform_mat_8650
# from scripts_transform.transform_mat_8750 import transform_mat_8750
from scripts_transform.transform_outbound import transform_outbound
from scripts_transform.transform_stock import transform_stock
from sqlserver_load.sql_open_conn import open_sql_connection
from sqlserver_load.sql_truncate import execute_sql_truncate
from sqlserver_load.sql_bulk import execute_sql_bulk
from sqlserver_load.sql_close_conn import close_sql_connection
from sqlserver_load.sql_lastrun import update_last_run


def load_environment_variables(env_path):
    """Load environment variables from the .env file."""
    load_dotenv(env_path)
    env_vars = {
        # SAP
        'SAP_USERNAME': os.getenv("SAP_USERNAME"),
        'SAP_PASSWORD': os.getenv("SAP_PASSWORD"),
        'SAP_CLIENT': os.getenv("SAP_CLIENT"),
        'SAP_LANGUAGE': os.getenv("SAP_LANGUAGE"),
        'SAP_GUI_PATH': os.getenv("SAP_GUI_PATH"),
        'SAP_GUI_ENVIRONMENT_E11': os.getenv("SAP_GUI_ENVIRONMENT_E11"),
        'SAP_GUI_ENVIRONMENT': os.getenv("SAP_GUI_ENVIRONMENT"),

        # Download
        'SAP_FILE_PATH': os.getenv("SAP_FILE_PATH"),
        'SAP_LAYOUT': os.getenv("SAP_LAYOUT"),

        # Server Path
        'SERVER_PATH' : os.getenv("SERVER_PATH"),
        'MAPPED_SERVER_PATH': os.getenv("MAPPED_SERVER_PATH"),

        # SQL Server
        'SQL_SERVER': os.getenv("SQL_SERVER"),
        'SQL_DATABASE': os.getenv("SQL_DATABASE"),
        'SQL_USERNAME': os.getenv("SQL_USERNAME"),
        'SQL_PASSWORD': os.getenv("SQL_PASSWORD"),

        # Plants
        'PLANT_AR1': os.getenv("PLANT_AR1"),
        'PLANT_AR2': os.getenv("PLANT_AR2"),
        'PLANT_BR1': os.getenv("PLANT_BR1"),
        'PLANT_BR2': os.getenv("PLANT_BR2"),
        'PLANT_CL1': os.getenv("PLANT_CL1"),
        'PLANT_CL2': os.getenv("PLANT_CL2"),
        'PLANT_CL3': os.getenv("PLANT_CL3"),
        'PLANT_CL4': os.getenv("PLANT_CL4"),
        'PLANT_CL5': os.getenv("PLANT_CL5"),
        'PLANT_CL6': os.getenv("PLANT_CL6"),
        'PLANT_MX1': os.getenv("PLANT_MX1"),
        'PLANT_MX2': os.getenv("PLANT_MX2"),
        'PLANT_MX3': os.getenv("PLANT_MX3"),
        'PLANT_MX4': os.getenv("PLANT_MX4"),
        'PLANT_MX5': os.getenv("PLANT_MX5"),
        'PLANT_MX6': os.getenv("PLANT_MX6"),
        'PLANT_MX7': os.getenv("PLANT_MX7"),

        #Plant Range
        'PLANT_AR_START':os.getenv("PLANT_AR_START"),
        'PLANT_AR_END':os.getenv("PLANT_AR_END"),
        'PLANT_BR_START':os.getenv("PLANT_BR_START"),
        'PLANT_BR_END':os.getenv("PLANT_BR_END"),
        'PLANT_CL_START':os.getenv("PLANT_CL_START"),
        'PLANT_CL_END':os.getenv("PLANT_CL_END"),
        'PLANT_MX_START':os.getenv("PLANT_MX_START"),
        'PLANT_MX_END':os.getenv("PLANT_MX_END"),

        # Sorg
        'SORG_AR': os.getenv("SORG_AR"),
        'SORG_BR': os.getenv("SORG_BR"),
        'SORG_CL': os.getenv("SORG_CL"),
        'SORG_MX': os.getenv("SORG_MX"),

        # Company code
        'CODE_AR': os.getenv("CODE_AR"),
        'CODE_BR': os.getenv("CODE_BR"),
        'CODE_CL': os.getenv("CODE_CL"),
        'CODE_MX': os.getenv("CODE_MX"),

        # MB52 download
        'TRANS_STOCK': os.getenv("TRANS_STOCK"),
        'FILE_STOCK': os.getenv("FILE_STOCK"),

        # MB52 upload
        'TABLE_STOCK': os.getenv("TABLE_STOCK"),

        # ZBO2CS download
        'TRANS_BO': os.getenv("TRANS_BO"),
        'FILE_BO': os.getenv("FILE_BO"),

        # ZBO2CS upload
        'TABLE_BO': os.getenv("TABLE_BO"),

        # VL06O download
        'TRANS_OUTBOUND': os.getenv("TRANS_OUTBOUND"),
        'FILE_OUTBOUND': os.getenv("FILE_OUTBOUND"),

        # VL06O upload
        'TABLE_OUTBOUND': os.getenv("TABLE_OUTBOUND"),

        # Q01_inbound download
        'TRANS_INBOUND': os.getenv("TRANS_INBOUND"),
        'FILE_INBOUND': os.getenv("FILE_INBOUND"),

        # Q01_inbound upload
        'TABLE_INBOUND': os.getenv("TABLE_INBOUND"),

        # Q01_material_8650 download
        'TRANS_MATCL': os.getenv("TRANS_MATCL"),
        'FILE_MATCL': os.getenv("FILE_MATCL"),

        # Q01_material_8650 upload
        'TABLE_MATCL': os.getenv("TABLE_MATCL"),

        # Q01_material_8750 download
        'TRANS_MATAR': os.getenv("TRANS_MATAR"),
        'FILE_MATAR': os.getenv("FILE_MATAR"),

        # Q01_material_8750 upload
        'TABLE_MATAR': os.getenv("TABLE_MATAR"),

        # Q01_material_3000 download
        'TRANS_MATMX': os.getenv("TRANS_MATMX"),
        'FILE_MATMX': os.getenv("FILE_MATMX"),

        # Q01_material_3000 upload
        'TABLE_MATMX': os.getenv("TABLE_MATMX"),

        # Q01_material_8300 download
        'TRANS_MATBR': os.getenv("TRANS_MATBR"),
        'FILE_MATBR': os.getenv("FILE_MATBR"),

        # Q01_material_8300 upload
        'TABLE_MATBR': os.getenv("TABLE_MATBR"),

        # SQL Truncate commands
        'SQL_TRUNCATE_MATERIALS': os.getenv("SQL_TRUNCATE_MATERIALS"),
        'SQL_TRUNCATE_STOCK': os.getenv("SQL_TRUNCATE_STOCK"),
        'SQL_TRUNCATE_BO2CS': os.getenv("SQL_TRUNCATE_BO2CS"),
        'SQL_TRUNCATE_OUTBOUND': os.getenv("SQL_TRUNCATE_OUTBOUND"),
        'SQL_TRUNCATE_INBOUND': os.getenv("SQL_TRUNCATE_INBOUND"),

        # SQL Bulk commands
        'SQL_BULK_MATERIAL_MOAR': os.getenv("SQL_BULK_MATERIAL_MOAR"),
        'SQL_BULK_MATERIAL_MOCL': os.getenv("SQL_BULK_MATERIAL_MOCL"),
        'SQL_BULK_MATERIAL_MOBR': os.getenv("SQL_BULK_MATERIAL_MOBR"),
        'SQL_BULK_MATERIAL_MOMX': os.getenv("SQL_BULK_MATERIAL_MOMX"),
        'SQL_BULK_STOCK': os.getenv("SQL_BULK_STOCK"),
        'SQL_BULK_BO2CS': os.getenv("SQL_BULK_BO2CS"),
        'SQL_BULK_INBOUND': os.getenv("SQL_BULK_INBOUND"),
        'SQL_BULK_OUTBOUND': os.getenv("SQL_BULK_OUTBOUND")
    }
    return env_vars

def get_file_paths(base_path):
    root_path = os.path.abspath(os.sep)
    sql_data_path = os.path.join(root_path, 'SQLdata', 'data')
    mat_sql_data_path = os.path.join(sql_data_path, 'mat')
    mapped_network_path = os.getenv("MAPPED_SERVER_PATH")

    file_paths = {
        "bo2cs": {
            "raw": os.path.join(base_path, 'data', 'raw', 'tbl_bo2cs.txt'),
            "processed": os.path.join(base_path, 'data', 'processed', 'tbl_bo2cs.csv'),
            "exported": os.path.join(mat_sql_data_path, 'tbl_bo2cs.csv'),
            "uploaded": os.path.join(mapped_network_path, 'data', 'tbl_bo2cs.csv')      
        },
        "inbound": {
            "raw": os.path.join(base_path, 'data', 'raw', 'tbl_inbound.txt'),
            "processed": os.path.join(base_path, 'data', 'processed', 'tbl_inbound.csv'),
            "exported": os.path.join(mat_sql_data_path, 'tbl_inbound.csv'),
            "uploaded": os.path.join(mapped_network_path, 'data', 'tbl_inbound.csv')   
        },
        "material_3000": {
            "raw": os.path.join(base_path, 'data', 'raw', 'tbl_material_3000.txt'),
            "processed": os.path.join(base_path, 'data', 'processed', 'tbl_material_3000.csv'),
            "exported": os.path.join(mat_sql_data_path, 'tbl_material_3000.csv'),
            "uploaded": os.path.join(mapped_network_path, 'data', 'tbl_material_3000.csv') 
        },
        "material_8300": {
            "raw": os.path.join(base_path, 'data', 'raw', 'tbl_material_8300.txt'),
            "processed": os.path.join(base_path, 'data', 'processed', 'tbl_material_8300.csv'),
            "exported": os.path.join(mat_sql_data_path, 'tbl_material_8300.csv'),
            "uploaded": os.path.join(mapped_network_path, 'data', 'tbl_material_8300.csv') 
        },
        "material_8650": {
            "raw": os.path.join(base_path, 'data', 'raw', 'tbl_material_8650.txt'),
            "processed": os.path.join(base_path, 'data', 'processed', 'tbl_material_8650.csv'),
            "exported": os.path.join(mat_sql_data_path, 'tbl_material_8650.csv'),
            "uploaded": os.path.join(mapped_network_path, 'data', 'tbl_material_8650.csv') 
        },
        "material_8750": {
            "raw": os.path.join(base_path, 'data', 'raw', 'tbl_material_8750.txt'),
            "processed": os.path.join(base_path, 'data', 'processed', 'tbl_material_8750.csv'),
            "exported": os.path.join(mat_sql_data_path, 'tbl_material_8750.csv'),
            "uploaded": os.path.join(mapped_network_path, 'data', 'tbl_material_8750.csv') 
        },
        "outbound": {
            "raw": os.path.join(base_path, 'data', 'raw', 'tbl_vl06o.txt'),
            "processed": os.path.join(base_path, 'data', 'processed', 'tbl_outbound.csv'),
            "exported": os.path.join(mat_sql_data_path, 'tbl_outbound.csv'),
            "uploaded": os.path.join(mapped_network_path, 'data', 'tbl_outbound.csv') 
        },
        "stock": {
            "raw": os.path.join(base_path, 'data', 'raw', 'tbl_stock_mb52.txt'),
            "processed": os.path.join(base_path, 'data', 'processed', 'tbl_stock.csv'),
            "exported": os.path.join(mat_sql_data_path, 'tbl_stock.csv'),
            "uploaded": os.path.join(mapped_network_path, 'data', 'tbl_stock.csv') 
        }
    }

    return file_paths

def main():
    base_path = os.getcwd()
    env_path = os.path.join(base_path, '.env')
    env_vars = load_environment_variables(env_path)
    
    # OPEN -> (00:01:02)
    is_sap_open = open_sap_gui(env_vars['SAP_GUI_PATH'])
    time.sleep(60)
    if is_sap_open:
        is_logged_in = login_to_sap(env_vars['SAP_USERNAME'], env_vars['SAP_PASSWORD'], env_vars['SAP_CLIENT'], env_vars['SAP_LANGUAGE'], env_vars['SAP_GUI_ENVIRONMENT'])
        if is_logged_in:
            # Get the active session
            session = get_active_session()
            # Download the report if the session is obtained successfully
            if session:
                sorgs = [env_vars['SORG_AR'], env_vars['SORG_BR'], env_vars['SORG_CL'], env_vars['SORG_MX']]
                company_codes = [env_vars['CODE_AR'], env_vars['CODE_BR'], env_vars['CODE_CL'], env_vars['CODE_MX']]
                date = datetime.today().strftime('%d.%m.%Y')
                plants = [env_vars['PLANT_AR1'], env_vars['PLANT_AR2'], env_vars['PLANT_BR1'], env_vars['PLANT_BR2'], env_vars['PLANT_CL1'], env_vars['PLANT_CL2'], env_vars['PLANT_CL3'], env_vars['PLANT_CL4'], env_vars['PLANT_CL5'], env_vars['PLANT_CL6'], env_vars['PLANT_MX1'], env_vars['PLANT_MX2'], env_vars['PLANT_MX3'], env_vars['PLANT_MX4'], env_vars['PLANT_MX5'], env_vars['PLANT_MX6'], env_vars['PLANT_MX7']]
                plant_ranges = [(os.getenv("PLANT_AR_START"), os.getenv("PLANT_AR_END")), (os.getenv("PLANT_BR_START"), os.getenv("PLANT_BR_END")), (os.getenv("PLANT_CL_START"), os.getenv("PLANT_CL_END")), (os.getenv("PLANT_MX_START"), os.getenv("PLANT_MX_END"))]
                # reports download 1 - EXTRACT -> (00:01:18)
                download_report_zbo2cs(session, env_vars['TRANS_BO'],env_vars['SAP_FILE_PATH'], env_vars['FILE_BO'], env_vars['SAP_LAYOUT'], sorgs)
                download_inbound_report(session, env_vars['TRANS_INBOUND'], env_vars['SAP_FILE_PATH'], env_vars['FILE_INBOUND'], env_vars['SAP_LAYOUT'], plants, company_codes, date)
                download_report_mb52(session, env_vars['TRANS_STOCK'], env_vars['SAP_FILE_PATH'], env_vars['FILE_STOCK'], env_vars['SAP_LAYOUT'], plant_ranges)
                download_outbound_report(session, env_vars['TRANS_OUTBOUND'],env_vars['SAP_FILE_PATH'], env_vars['FILE_OUTBOUND'], env_vars['SAP_LAYOUT'], plants)
                # reports download 2 - EXTRACT -> (00:07:35)
                # download_material_report(session, env_vars['TRANS_MATAR'], env_vars['SAP_FILE_PATH'], env_vars['FILE_MATAR'], env_vars['SAP_LAYOUT'], env_vars['SORG_AR'], env_vars['PLANT_AR1'])
                # download_material_report(session, env_vars['TRANS_MATBR'], env_vars['SAP_FILE_PATH'], env_vars['FILE_MATBR'], env_vars['SAP_LAYOUT'], env_vars['SORG_BR'], env_vars['PLANT_BR1'])
                # download_material_report(session, env_vars['TRANS_MATCL'], env_vars['SAP_FILE_PATH'], env_vars['FILE_MATCL'], env_vars['SAP_LAYOUT'], env_vars['SORG_CL'], env_vars['PLANT_CL1'])
                # download_material_report(session, env_vars['TRANS_MATMX'], env_vars['SAP_FILE_PATH'], env_vars['FILE_MATMX'], env_vars['SAP_LAYOUT'], env_vars['SORG_MX'], env_vars['PLANT_MX1'])
            logout_from_sap()
        time.sleep(30)
        close_sap_logon()
    # TRANSFORM -> (00:00:10)
    paths = get_file_paths(base_path)
    bo2cs_paths = paths["bo2cs"]
    transform_bo2cs(bo2cs_paths["raw"], bo2cs_paths["processed"], bo2cs_paths["exported"], bo2cs_paths["uploaded"])
    inbound_paths = paths["inbound"]
    transform_inbound(inbound_paths["raw"], inbound_paths["processed"], inbound_paths["exported"], inbound_paths["uploaded"])
    # material_3000_paths = paths["material_3000"]
    # transform_mat_3000(material_3000_paths["raw"], material_3000_paths["processed"], material_3000_paths["exported"],  material_3000_paths["uploaded"])
    # material_8300_paths = paths["material_8300"]
    # transform_mat_8300(material_8300_paths["raw"], material_8300_paths["processed"], material_8300_paths["exported"],  material_8300_paths["uploaded"])
    # material_8650_paths = paths["material_8650"]
    # transform_mat_8650(material_8650_paths["raw"], material_8650_paths["processed"], material_8650_paths["exported"],  material_8650_paths["uploaded"])
    # material_8750_paths = paths["material_8750"]
    # transform_mat_8750(material_8750_paths["raw"], material_8750_paths["processed"], material_8750_paths["exported"],  material_8750_paths["uploaded"])
    outbound_paths = paths["outbound"]
    transform_outbound(outbound_paths["raw"], outbound_paths["processed"], outbound_paths["exported"], outbound_paths["uploaded"])
    stock_paths = paths["stock"]
    transform_stock(stock_paths["raw"], stock_paths["processed"], stock_paths["exported"], stock_paths["uploaded"])
    time.sleep(30)
    print('data transformation phase was completed')
    # LOAD -> (00:00:10)
    conn = open_sql_connection(env_vars['SQL_SERVER'], env_vars['SQL_DATABASE'], env_vars['SQL_USERNAME'], env_vars['SQL_PASSWORD'])
    if conn:
        truncate_commands = [
            env_vars['SQL_TRUNCATE_STOCK'],
            env_vars['SQL_TRUNCATE_BO2CS'],
            env_vars['SQL_TRUNCATE_OUTBOUND'],
            env_vars['SQL_TRUNCATE_INBOUND'],
            env_vars['SQL_TRUNCATE_MATERIALS']
        ]

        # Execute the SQL commands
        for command in truncate_commands:
            execute_sql_truncate(conn, command)

        # List of SQL commands to bulk the tables
        bulk_commands = [
            env_vars['SQL_BULK_MATERIAL_MOAR'],
            env_vars['SQL_BULK_MATERIAL_MOCL'],
            env_vars['SQL_BULK_MATERIAL_MOBR'],
            env_vars['SQL_BULK_MATERIAL_MOMX'],
            env_vars['SQL_BULK_STOCK'],
            env_vars['SQL_BULK_BO2CS'],
            env_vars['SQL_BULK_INBOUND'],
            env_vars['SQL_BULK_OUTBOUND']
        ]

        # Execute the SQL commands
        for command in bulk_commands:
            execute_sql_bulk(conn, command)

        update_last_run(conn)
    
    close_sql_connection(conn)

if __name__ == "__main__":
    main()