import pandas as pd
import os

base_path = os.getcwd()
print(base_path)

material_momx_path = os.path.join(base_path, 'data', 'raw', 'tbl_material_3000.txt')
print(material_momx_path)

material_3000_processed_path = os.path.join(base_path, 'data', 'processed', 'tbl_material_3000.csv')
print(material_3000_processed_path)

root_path = os.path.abspath(os.sep)
print(root_path)

sql_data_path = os.path.join(root_path, 'SQLdata', 'data')
print(sql_data_path)

mat_sql_data_path = os.path.join(sql_data_path, 'mat')
print(mat_sql_data_path)

material_3000_exported_path = os.path.join(mat_sql_data_path, 'tbl_material_3000.csv')
print(material_3000_exported_path)

df_material_momx = pd.read_csv(material_momx_path, sep='\t', skiprows=3, encoding='latin1')

unnamed_columns = [col for col in df_material_momx.columns if 'Unnamed:' in col]
df_material_momx.drop(columns=unnamed_columns, inplace=True)
column_titles = df_material_momx.columns.tolist()
new_column_titles = {col: col.strip().replace(' ', '_').replace('-', '_').replace('.','') for col in column_titles}
df_material_momx.rename(columns=new_column_titles, inplace=True)

column_counts = df_material_momx.columns.value_counts()
duplicate_columns = column_counts[column_counts > 1].index

for col in duplicate_columns:
    col_indices = [i for i, x in enumerate(df_material_momx.columns) if x == col]
    for j, index in enumerate(col_indices):
        df_material_momx.columns.values[index] = f"{col}_{j+1}"


df_material_momx['SOrg'] = df_material_momx['SOrg'].fillna(0).astype(int).astype(str).str.strip()
df_material_momx['Plnt'] = df_material_momx['Plnt'].fillna(0).astype(int).astype(str).str.strip()
df_material_momx['Material'] = df_material_momx['Material'].fillna(0).astype(int).astype(str).str.strip()
df_material_momx['Material_number'] = df_material_momx['Material_number'].astype(str).str.strip()
df_material_momx['X_Plant_Material_Status'] = df_material_momx['X_Plant_Material_Status'].fillna(0).astype(int).astype(str).str.strip()
df_material_momx['MS'] = df_material_momx['MS'].fillna(0).astype(int).astype(str).str.strip()
df_material_momx['Gross_weight'] = df_material_momx['Gross_weight'].fillna(0).astype(str).str.strip().str.replace('.', '').str.replace(',', '.').astype(float)
df_material_momx['WUn'] = df_material_momx['WUn'].astype(str).str.strip()
df_material_momx['Spart'] = df_material_momx['Spart'].astype(str).str.strip()
df_material_momx['ValidFrom'] = pd.to_datetime(df_material_momx['ValidFrom'], errors="coerce", format='%d.%m.%Y')
df_material_momx['Minorder_qty'] = df_material_momx['Minorder_qty'].fillna(0).astype(str).str.strip().str.replace('.', '').str.replace(',', '.').astype(float)
df_material_momx['BUn'] = df_material_momx['BUn'].astype(str).str.strip()
df_material_momx['Orig'] = df_material_momx['Orig'].astype(str).str.strip()
df_material_momx['Web'] = df_material_momx['Web'].astype(str).str.strip()
df_material_momx['FM_rel'] = df_material_momx['FM_rel'].astype(str).str.strip()
df_material_momx['Av'] = df_material_momx['Av'].astype(str).str.strip()
df_material_momx['PGr'] = df_material_momx['PGr'].astype(str).str.strip()
df_material_momx['GRT'] = df_material_momx['GRT'].fillna(0).astype(str).str.strip().str.replace('.', '').str.replace(',', '.').astype(float)
df_material_momx['Typ'] = df_material_momx['Typ'].astype(str).str.strip()
df_material_momx['MRPCn'] = df_material_momx['MRPCn'].astype(str).str.strip()
df_material_momx['Minlot_size'] = df_material_momx['Minlot_size'].fillna(0).astype(str).str.strip().str.replace('.', '').str.replace(',', '.').astype(float)
df_material_momx['BUn1'] = df_material_momx['BUn1'].astype(str).str.strip()
df_material_momx['SPT'] = df_material_momx['SPT'].astype(str).str.strip()
df_material_momx['PDT'] = df_material_momx['PDT'].fillna(0).astype(str).str.strip().str.replace('.', '').str.replace(',', '.').astype(float)
df_material_momx['TABCD'] = df_material_momx['TABCD'].astype(str).str.strip()
df_material_momx['XYZ'] = df_material_momx['XYZ'].astype(str).str.strip()
df_material_momx['Pl'] = df_material_momx['Pl'].astype(str).str.strip()
df_material_momx['Safety_Stock'] = df_material_momx['Safety_Stock'].fillna(0).astype(str).str.strip().str.replace('.', '').str.replace(',', '.').astype(float)
df_material_momx['Rounding_val'] = df_material_momx['Rounding_val'].astype(str).str.strip()
df_material_momx['BUn2'] = df_material_momx['BUn2'].astype(str).str.strip()
df_material_momx['Rprofile'] = df_material_momx['Rprofile'].astype(str).str.strip()
df_material_momx['LS'] = df_material_momx['LS'].astype(str).str.strip()
df_material_momx['Min_dely_qty'] = df_material_momx['Min_dely_qty'].fillna(0).astype(str).str.strip().str.replace('.', '').str.replace(',', '.').astype(float)
df_material_momx['BUn3'] = df_material_momx['BUn3'].astype(str).str.strip()
df_material_momx['key_material'] = df_material_momx['SOrg'] + '/' + df_material_momx['Material']
df_material_momx['key_material'] = df_material_momx['key_material'].astype(str).str.strip()

df_material_momx.to_csv(material_3000_processed_path, index=False, encoding='latin1')
df_material_momx.to_csv(material_3000_exported_path, index=False, encoding='latin1')


