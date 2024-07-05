import pandas as pd
import os

plant_to_sorg = {
    "8750": "8750", "8760": "8750",
    "8330": "8300", "8302": "8300",
    "8650": "8650", "8663": "8650", "8655": "8650", "8658": "8650", "8662": "8650", "8651": "8650",
    "3000": "3000", "3002": "3000", "3010": "3000", "3014": "3000", "3016": "3000", "3018": "3000", "3022": "3000"
}

base_path = os.getcwd()
print(base_path)

stock_file_path = os.path.join(base_path, 'data', 'raw', 'tbl_stock_mb52.txt')
print(stock_file_path)

stock_processed_path = os.path.join(base_path, 'data', 'processed', 'tbl_stock.csv')
print(stock_processed_path)

root_path = os.path.abspath(os.sep)
print(root_path)

sql_data_path = os.path.join(root_path, 'SQLdata', 'data')
print(sql_data_path)

mat_sql_data_path = os.path.join(sql_data_path, 'mat')
print(mat_sql_data_path)

stock_exported_path = os.path.join(mat_sql_data_path, 'tbl_stock.csv')
print(stock_exported_path)

df_stock = pd.read_csv(stock_file_path, sep='\t', skiprows=1, encoding='latin1')


unnamed_columns = [col for col in df_stock.columns if 'Unnamed:' in col]
df_stock.drop(columns=unnamed_columns, inplace=True)
column_titles = df_stock.columns.tolist()
new_column_titles = {col: col.strip().replace(' ', '_').replace('/','_').replace('-','_').replace('.','') for col in column_titles}
df_stock.rename(columns=new_column_titles, inplace=True)

df_stock['Material'] = df_stock['Material'].fillna(0).astype(int).astype(str).str.strip()
df_stock['Material_Description'] = df_stock['Material_Description'].astype(str).str.strip()
df_stock['SLoc'] = df_stock['SLoc'].fillna(0).astype(int).astype(str).str.strip()
df_stock['SL'] = df_stock['SL'].astype(str).str.strip()
df_stock['Plnt'] = df_stock['Plnt'].fillna(0).astype(int).astype(str).str.strip()
df_stock['BUn'] = df_stock['BUn'].astype(str).str.strip()
df_stock['Unrestricted'] = df_stock['Unrestricted'].astype(str).str.strip().str.replace('.', '').str.replace(',', '.').astype(float)
df_stock['Transit_Transf'] = df_stock['Transit_Transf'].astype(str).str.strip().str.replace('.', '').str.replace(',', '.').astype(float)
df_stock['Blocked'] = df_stock['Blocked'].astype(str).str.strip().str.replace('.', '').str.replace(',', '.').astype(float)
df_stock['In_Qual_Insp'] = df_stock['In_Qual_Insp'].astype(str).str.strip().str.replace('.', '').str.replace(',', '.').astype(float)
df_stock['Restricted_Use'] = df_stock['Restricted_Use'].astype(str).str.strip().str.replace('.', '').str.replace(',', '.').astype(float)
df_stock['Returns'] = df_stock['Returns'].astype(str).str.strip().str.replace('.', '').str.replace(',', '.').astype(float)
df_stock['Stk_in_Transit'] = df_stock['Stk_in_Transit'].astype(str).str.strip().str.replace('.', '').str.replace(',', '.').astype(float)
df_stock['Unrestricted'] = pd.to_numeric(df_stock['Unrestricted'], errors='coerce')

def map_plant_to_sorg(plant):
    return plant_to_sorg.get(plant, None)
df_stock['Sorg'] = df_stock['Plnt'].map(map_plant_to_sorg)

df_stock['key_material'] = df_stock['Sorg'] + '/' + df_stock['Material']
df_stock['key_material'] = df_stock['key_material'].astype(str).str.strip()

df_stock.to_csv(stock_processed_path, index=False, encoding='latin1')
df_stock.to_csv(stock_exported_path, index=False, encoding='latin1')
