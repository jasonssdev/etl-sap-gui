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


plant_to_sorg = {
    "8750": "8750", "8760": "8750",
    "8330": "8300", "8302": "8300",
    "8650": "8650", "8663": "8650", "8655": "8650", "8658": "8650", "8662": "8650", "8651": "8650",
    "3000": "3000", "3002": "3000", "3010": "3000", "3014": "3000", "3016": "3000", "3018": "3000", "3022": "3000"
}

def get_file_paths(base_path):
    stock_file_path = os.path.join(base_path, 'data', 'raw', 'tbl_stock_mb52.txt')
    stock_processed_path = os.path.join(base_path, 'data', 'processed', 'tbl_stock.csv')
    root_path = os.path.abspath(os.sep)
    sql_data_path = os.path.join(root_path, 'SQLdata', 'data')
    mat_sql_data_path = os.path.join(sql_data_path, 'mat')
    stock_exported_path = os.path.join(mat_sql_data_path, 'tbl_stock.csv')
    stock_uploaded_path = os.path.join(mapped_network_path, 'data', 'tbl_stock.csv')
    return stock_file_path, stock_processed_path, stock_exported_path,stock_uploaded_path

def clean_column_names(df):
    new_column_titles = {col: col.strip().replace(' ', '_').replace('/', '_').replace('-', '_').replace('.', '') for col in df.columns}
    df.rename(columns=new_column_titles, inplace=True)

def transform_columns(df):
    str_columns = ['Material', 'Material_Description', 'SLoc', 'SL', 'Plnt', 'BUn']
    for col in str_columns:
        df[col] = df[col].astype(str).str.strip()

    float_columns = ['Unrestricted', 'Transit_Transf', 'Blocked', 'In_Qual_Insp', 'Restricted_Use', 'Returns', 'Stk_in_Transit']
    for col in float_columns:
        df[col] = pd.to_numeric(df[col].astype(str).str.strip().str.replace('.', '').str.replace(',', '.'), errors='coerce').fillna(0)

def map_plant_to_sorg(plant):
    return plant_to_sorg.get(plant, None)

def transform_stock(stock_file_path, processed_path, exported_path, uploaded_path):
    try:
        df_stock = pd.read_csv(stock_file_path, sep='\t', skiprows=1, encoding='latin1', low_memory=False)

        unnamed_columns = [col for col in df_stock.columns if 'Unnamed:' in col]
        df_stock.drop(columns=unnamed_columns, inplace=True)

        clean_column_names(df_stock)
        transform_columns(df_stock)

        df_stock['Sorg'] = df_stock['Plnt'].map(map_plant_to_sorg)
        df_stock['key_material'] = (df_stock['Sorg'] + '/' + df_stock['Material']).astype(str).str.strip()

        df_stock.to_csv(processed_path, index=False, encoding='latin1', sep='|')
        df_stock.to_csv(exported_path, index=False, encoding='latin1', sep='|')
        df_stock.to_csv(uploaded_path, index=False, encoding='latin1', sep='|')


        return df_stock

    except FileNotFoundError as e:
        print(f"File not found: {e.filename}")
    except pd.errors.ParserError as e:
        print(f"Error parsing file: {e}")
    except Exception as e:
        print(f"Error processing file: {e}")

    return None

if __name__ == "__main__":
    base_path = os.getcwd()
    stock_file_path, stock_processed_path, stock_exported_path, stock_uploaded_path = get_file_paths(base_path)
    transform_stock(stock_file_path, stock_processed_path, stock_exported_path, stock_uploaded_path)

