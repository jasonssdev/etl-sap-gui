import pandas as pd
import os 

base_path = os.getcwd()
print(base_path)

inbound_file_path = os.path.join(base_path, 'data', 'raw', 'tbl_inbound.txt')
print(inbound_file_path)

inbound_processed_path = os.path.join(base_path, 'data', 'processed', 'tbl_inbound.csv')
print(inbound_processed_path)

root_path = os.path.abspath(os.sep)
print(root_path)

sql_data_path = os.path.join(root_path, 'SQLdata', 'data')
print(sql_data_path)

mat_sql_data_path = os.path.join(sql_data_path, 'mat')
print(mat_sql_data_path)

inbound_exported_path = os.path.join(mat_sql_data_path, 'tbl_inbound.csv')
print(inbound_exported_path)

df_inbound = pd.read_csv(inbound_file_path, sep='\t', skiprows=3, encoding='latin1')

unnamed_columns = [col for col in df_inbound.columns if 'Unnamed:' in col]
df_inbound.drop(columns=unnamed_columns, inplace=True)
column_titles = df_inbound.columns.tolist()
new_column_titles = {col: col.strip().replace(' ', '_').replace('-','_').replace('.','') for col in column_titles}
df_inbound.rename(columns=new_column_titles, inplace=True)

column_counts = df_inbound.columns.value_counts()
duplicate_columns = column_counts[column_counts > 1].index

for col in duplicate_columns:
    col_indices = [i for i, x in enumerate(df_inbound.columns) if x == col]
    for j, index in enumerate(col_indices):
        df_inbound.columns.values[index] = f"{col}_{j+1}"

df_inbound['Doc_No'] = df_inbound['Doc_No'].fillna(0).astype(int).astype(str)
df_inbound['Shipment'] = df_inbound['Shipment'].fillna(0).astype(int).astype(str).str.strip()
df_inbound['PurchDoc'] = df_inbound['PurchDoc'].fillna(0).astype(int).astype(str).str.strip()
df_inbound['Item_1'] = df_inbound['Item_1'].fillna(0).astype(int).astype(str).str.strip()
df_inbound['Material'] = df_inbound['Material'].fillna(0).astype(int).astype(str).str.strip()
df_inbound['Material_Description'] = df_inbound['Material_Description'].astype(str).str.strip()
df_inbound['Plnt'] = df_inbound['Plnt'].fillna(0).astype(int).astype(str)
df_inbound['SLoc'] = df_inbound['SLoc'].fillna(0).astype(int).astype(str)
df_inbound['PO_Quantity'] = df_inbound['PO_Quantity'].astype(str).str.strip().str.replace('.', '').str.replace(',', '.').astype(float)
df_inbound['OUn'] = df_inbound['OUn'].astype(str).str.strip()
df_inbound['OUn1'] = df_inbound['OUn1'].astype(str).str.strip()
df_inbound['Item_2'] = df_inbound['Item_2'].fillna(0).astype(int).astype(str)
df_inbound['Delivery'] = df_inbound['Delivery'].fillna(0).astype(int).astype(str)
df_inbound['Reference'] = df_inbound['Reference'].astype(str).str.strip()
df_inbound['Plnt'] = df_inbound['Plnt'].fillna(0).astype(int).astype(str)
df_inbound['Supplier'] = df_inbound['Supplier'].astype(str).str.strip()
df_inbound['POrg'] = df_inbound['POrg'].fillna(0).astype(int).astype(str)
df_inbound['PGr'] = df_inbound['PGr'].astype(str).str.strip()
df_inbound['Vendor'] = df_inbound['Vendor'].astype(str).str.strip()
df_inbound['ShPt'] = df_inbound['ShPt'].fillna(0).astype(int).astype(str)
df_inbound['DelivDate'] = pd.to_datetime(df_inbound['DelivDate'], errors="coerce", format='%d.%m.%Y')
df_inbound['Doc_Date'] = pd.to_datetime(df_inbound['Doc_Date'], errors="coerce", format='%d.%m.%Y')
df_inbound['Ext_Order_Pos'] = df_inbound['Ext_Order_Pos'].fillna(0).astype(int).astype(str)
df_inbound['Ext_Order_Number'] = df_inbound['Ext_Order_Number'].fillna(0).astype(int).astype(str)
df_inbound['SupplVndr'] = df_inbound['SupplVndr'].astype(str).str.strip()
df_inbound['TrackingNo'] = df_inbound['TrackingNo'].astype(str).str.strip()
df_inbound['Reservation'] = df_inbound['Reservation'].fillna(0).astype(int).astype(str).str.strip()
df_inbound['Reservation_item'] = df_inbound['Reservation_item'].fillna(0).astype(int).astype(str)
df_inbound['Reservation_order_date'] = pd.to_datetime(df_inbound['Reservation_order_date'], errors="coerce", format='%d.%m.%Y')
df_inbound['Diffdays'] = df_inbound['Diffdays'].astype(str).str.strip().astype(float)

df_inbound['key_material'] = df_inbound['POrg'] + '/' + df_inbound['Material']
df_inbound['key_material'] = df_inbound['key_material'].astype(str).str.strip()

df_inbound.to_csv(inbound_processed_path, index=False, encoding='latin1')
df_inbound.to_csv(inbound_exported_path, index=False, encoding='latin1')
