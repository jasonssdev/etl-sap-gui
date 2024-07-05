import pandas as pd
import os 


base_path = os.getcwd()
print(base_path)

bo2cs_file_path = os.path.join(base_path, 'data', 'raw', 'tbl_bo2cs.txt')
print(bo2cs_file_path)

bo2cs_processed_path = os.path.join(base_path, 'data', 'processed', 'tbl_bo2cs.csv')
print(bo2cs_processed_path)

root_path = os.path.abspath(os.sep)
print(root_path)

sql_data_path = os.path.join(root_path, 'SQLdata', 'data')
print(sql_data_path)

mat_sql_data_path = os.path.join(sql_data_path, 'mat')
print(mat_sql_data_path)

bo2cs_exported_path = os.path.join(mat_sql_data_path, 'tbl_bo2cs.csv')
print(bo2cs_exported_path)

df_bo2cs = pd.read_csv(bo2cs_file_path, sep='\t', skiprows=3, encoding='latin1')

unnamed_columns = [col for col in df_bo2cs.columns if 'Unnamed:' in col]
df_bo2cs.drop(columns=unnamed_columns, inplace=True)
column_titles = df_bo2cs.columns.tolist()
new_column_titles = {col: col.strip().replace(' ', '_').replace('-','_').replace('.','') for col in column_titles}
df_bo2cs.rename(columns=new_column_titles, inplace=True)

df_bo2cs['SOrg'] = df_bo2cs['SOrg'].fillna(0).astype(int).astype(str).str.strip()
df_bo2cs['SaTy'] = df_bo2cs['SaTy'].astype(str).str.strip()
df_bo2cs['Sales_Doc'] = df_bo2cs['Sales_Doc'].fillna(0).astype(int).astype(str).str.strip()
df_bo2cs['Sold_to'] = df_bo2cs['Sold_to'].astype(str).str.strip()
df_bo2cs['Name_1'] = df_bo2cs['Name_1'].astype(str).str.strip()
df_bo2cs['CustLoy'] = df_bo2cs['CustLoy'].astype(str).str.strip()
df_bo2cs['FocCust'] = df_bo2cs['FocCust'].astype(str).str.strip()
df_bo2cs['Territory'] = df_bo2cs['Territory'].astype(str).str.strip()
df_bo2cs['Created_on'] = pd.to_datetime(df_bo2cs['Created_on'], errors="coerce", format='%d.%m.%Y')
df_bo2cs['Typ'] = df_bo2cs['Typ'].astype(str).str.strip()
df_bo2cs['Material'] = df_bo2cs['Material'].fillna(0).astype(int).astype(str).str.strip()
df_bo2cs['Item_Description'] = df_bo2cs['Item_Description'].astype(str).str.strip()
df_bo2cs['Order_Qty'] = df_bo2cs['Order_Qty'].astype(str).str.strip().str.replace('.', '').str.replace(',', '.').astype(float)
df_bo2cs['Corrqty'] = df_bo2cs['Corrqty'].astype(str).str.strip().str.replace('.', '').str.replace(',', '.').astype(float)
df_bo2cs['ConfirmQty'] = df_bo2cs['ConfirmQty'].astype(str).str.strip().str.replace('.', '').str.replace(',', '.').astype(float)
df_bo2cs['SU'] = df_bo2cs['SU'].astype(str).str.strip()
df_bo2cs['BO_value'] = df_bo2cs['BO_value'].astype(str).str.strip()
df_bo2cs['Curr'] = df_bo2cs['Curr'].astype(str).str.strip()
df_bo2cs['InitReqDt'] = pd.to_datetime(df_bo2cs['InitReqDt'], errors="coerce", format='%d.%m.%Y')
df_bo2cs['promised'] = pd.to_datetime(df_bo2cs['promised'], errors="coerce", format='%d.%m.%Y')
df_bo2cs['MatAvDt'] = pd.to_datetime(df_bo2cs['MatAvDt'], errors="coerce", format='%d.%m.%Y')
df_bo2cs['DlvDate'] = pd.to_datetime(df_bo2cs['DlvDate'], errors="coerce", format='%d.%m.%Y')
df_bo2cs['DS'] = df_bo2cs['DS'].astype(str).str.strip()
df_bo2cs['DB'] = df_bo2cs['DB'].astype(str).str.strip()
df_bo2cs['BOstatus'] = df_bo2cs['BOstatus'].astype(str).str.strip()
df_bo2cs['BO'] = df_bo2cs['BO'].astype(str).str.strip()
df_bo2cs['BO_status_changed'] = pd.to_datetime(df_bo2cs['BO_status_changed'], errors="coerce", format='%d.%m.%Y')
df_bo2cs['GM'] = df_bo2cs['GM'].astype(str).str.strip()
df_bo2cs['unc'] = df_bo2cs['unc'].astype(str).str.strip()
df_bo2cs['Description'] = df_bo2cs['Description'].astype(str).str.strip()
df_bo2cs['SC'] == df_bo2cs['Item_Description'].astype(str).str.strip()
df_bo2cs['Route'] = df_bo2cs['Route'].astype(str).str.strip()
df_bo2cs['Reqdlvdt'] = pd.to_datetime(df_bo2cs['Reqdlvdt'], errors="coerce", format='%d.%m.%Y')

df_bo2cs['key_material'] = df_bo2cs['SOrg'] + '/' + df_bo2cs['Material']
df_bo2cs['key_material'] = df_bo2cs['key_material'].astype(str).str.strip()

df_bo2cs.to_csv(bo2cs_processed_path, index=False, encoding='latin1')
df_bo2cs.to_csv(bo2cs_exported_path, index=False, encoding='latin1')


