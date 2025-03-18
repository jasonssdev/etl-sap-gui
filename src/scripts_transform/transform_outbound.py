import pandas as pd
import os
from dotenv import load_dotenv

# Get base path
base_path = os.getcwd()

# Get env path
env_path = os.path.join(base_path, '.env')

# Load environment variables from .env
load_dotenv(env_path)

#get variables from .env
mapped_network_path = os.getenv("MAPPED_SERVER_PATH")

def get_file_paths(base_path):
    outbound_file_path = os.path.join(base_path, 'data', 'raw', 'tbl_vl06o.txt')
    outbound_processed_path = os.path.join(base_path, 'data', 'processed', 'tbl_outbound.csv')
    root_path = os.path.abspath(os.sep)
    sql_data_path = os.path.join(root_path, 'SQLdata', 'data')
    mat_sql_data_path = os.path.join(sql_data_path, 'mat')
    outbound_exported_path = os.path.join(mat_sql_data_path, 'tbl_outbound.csv')
    outbound_uploaded_path = os.path.join(mapped_network_path, 'data', 'tbl_outbound.csv')
    return outbound_file_path, outbound_processed_path, outbound_exported_path, outbound_uploaded_path

def clean_column_names(df):
    new_column_titles = {col: col.strip().replace(' ', '_').replace('-', '_').replace('.', '') for col in df.columns}
    df.rename(columns=new_column_titles, inplace=True)

def transform_columns(df):
    str_columns = [
        'SOrg', 'Material', 'Item_Description', 'SU', 'GM', 'Route',
        'Name_of_Sold_to_Party', 'Pur_Doc'
    ]
    for col in str_columns:
        df[col] = df[col].astype(str).str.strip()

    int_columns = ['Delivery', 'Item', 'Sold_to']
    for col in int_columns:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0).astype(int).astype(str)

    float_columns = ['DlvQty', 'Batch', 'OPS', 'PickingSts', 'WM', 'SpStck_No']
    for col in float_columns:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0).astype(float)

    date_columns = ['TrpPlanDt']
    for col in date_columns:
        df[col] = pd.to_datetime(df[col], errors="coerce", format='%d.%m.%Y')

def transform_outbound(outbound_file_path, processed_path, exported_path, uploaded_path):
    try:
        df_outbound = pd.read_csv(outbound_file_path, sep='\t', skiprows=1, encoding='latin1', low_memory=False)
        unnamed_columns = [col for col in df_outbound.columns if 'Unnamed:' in col]
        df_outbound.drop(columns=unnamed_columns, inplace=True)

        clean_column_names(df_outbound)
        transform_columns(df_outbound)

        # Crear nueva columna 'key_material'
        df_outbound['key_material'] = (df_outbound['SOrg'] + '/' + df_outbound['Material']).astype(str).str.strip()

        # Guardar los archivos transformados
        df_outbound.to_csv(processed_path, index=False, encoding='latin1', sep='|')
        df_outbound.to_csv(exported_path, index=False, encoding='latin1', sep='|')
        df_outbound.to_csv(uploaded_path, index=False, encoding='latin1', sep='|')


        return df_outbound

    except FileNotFoundError as e:
        print(f"File not found: {e.filename}")
    except pd.errors.ParserError as e:
        print(f"Error parsing file: {e}")
    except Exception as e:
        print(f"Error processing file: {e}")

    return None

if __name__ == "__main__":
    base_path = os.getcwd()
    outbound_file_path, outbound_processed_path, outbound_exported_path, outbound_uploaded_path = get_file_paths(base_path)
    transform_outbound(outbound_file_path, outbound_processed_path, outbound_exported_path, outbound_uploaded_path)
