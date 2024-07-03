import pandas as pd
import os 

base_path = os.getcwd()
print(base_path)

outbound_file_path = os.path.join(base_path, 'data', 'raw', 'tbl_vl06o.txt')
print(outbound_file_path)

outbound_processed_path = os.path.join(base_path, 'data', 'processed', 'tbl_outbound.csv')
print(outbound_processed_path)

df_outbound = pd.read_csv(outbound_file_path, sep='\t', skiprows=3, encoding='latin1')

unnamed_columns = [col for col in df_outbound.columns if 'Unnamed:' in col]
df_outbound.drop(columns=unnamed_columns, inplace=True)
column_titles = df_outbound.columns.tolist()
new_column_titles = {col: col.strip().replace(' ', '_').replace('-','_').replace('.','') for col in column_titles}
df_outbound.rename(columns=new_column_titles, inplace=True)

df_outbound['SOrg'] = df_outbound['SOrg'].fillna(0).astype(int).astype(str).str.strip()
df_outbound['Delivery'] = df_outbound['Delivery'].fillna(0).astype(str).str.strip().str.replace('.', '').str.replace(',', '.').astype(int)
df_outbound['Item'] = df_outbound['Item'].fillna(0).astype(str).str.strip().str.replace('.', '').str.replace(',', '.').astype(int)
df_outbound['Material'] = df_outbound['Material'].fillna(0).astype(int).astype(str).str.strip()
df_outbound['Item_Description'] = df_outbound['Item_Description'].astype(str).str.strip()
df_outbound['DlvQty'] = df_outbound['DlvQty'].fillna(0).astype(str).str.strip().astype(float)
df_outbound['SU'] = df_outbound['SU'].astype(str).str.strip()
df_outbound['Batch'] = df_outbound['Batch'].fillna(0).astype(str).str.strip().astype(float)
df_outbound['OPS'] = df_outbound['OPS'].fillna(0).astype(str).str.strip().astype(float)
df_outbound['PickingSts'] = df_outbound['PickingSts'].fillna(0).astype(str).str.strip().astype(float)
df_outbound['WM'] = df_outbound['WM'].fillna(0).astype(str).str.strip().astype(float)
df_outbound['GM'] = df_outbound['GM'].astype(str).str.strip()
df_outbound['Route'] = df_outbound['Route'].astype(str).str.strip()
df_outbound['SpStck_No'] = df_outbound['SpStck_No'].fillna(0).astype(str).str.strip().astype(float)
df_outbound['Sold_to'] = df_outbound['Sold_to'].fillna(0).astype(int).astype(str).str.strip()
df_outbound['Name_of_Sold_to_Party'] = df_outbound['Name_of_Sold_to_Party'].astype(str).str.strip()
df_outbound['Pur_Doc'] = df_outbound['Pur_Doc'].fillna(0).astype(int).astype(str)
df_outbound['TrpPlanDt'] = pd.to_datetime(df_outbound['TrpPlanDt'], errors="coerce", format='%d.%m.%Y')

df_outbound['key_material'] = df_outbound['SOrg'] + '/' + df_outbound['Material']
df_outbound['key_material'] = df_outbound['key_material'].astype(str).str.strip()

df_outbound.to_csv(outbound_processed_path, index=False, encoding='latin1')