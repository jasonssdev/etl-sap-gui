import pandas as pd
import os

base_path = os.getcwd()
print(base_path)

material_mocl_path = os.path.join(base_path, 'data', 'raw', 'tbl_material_8650.txt')
print(material_mocl_path)

material_8650_processed_path = os.path.join(base_path, 'data', 'processed', 'tbl_material_8650.csv')
print(material_8650_processed_path)

root_path = os.path.abspath(os.sep)
print(root_path)

sql_data_path = os.path.join(root_path, 'SQLdata', 'data')
print(sql_data_path)

mat_sql_data_path = os.path.join(sql_data_path, 'mat')
print(mat_sql_data_path)

material_8650_exported_path = os.path.join(mat_sql_data_path, 'tbl_material_8650.csv')
print(material_8650_exported_path)

df_material_mocl = pd.read_csv(material_mocl_path, sep='\t', skiprows=3, encoding='latin1')

unnamed_columns = [col for col in df_material_mocl.columns if 'Unnamed:' in col]
df_material_mocl.drop(columns=unnamed_columns, inplace=True)
column_titles = df_material_mocl.columns.tolist()
new_column_titles = {col: col.strip().replace(' ', '_').replace('-', '_').replace('.','') for col in column_titles}
df_material_mocl.rename(columns=new_column_titles, inplace=True)

column_counts = df_material_mocl.columns.value_counts()
duplicate_columns = column_counts[column_counts > 1].index

for col in duplicate_columns:
    col_indices = [i for i, x in enumerate(df_material_mocl.columns) if x == col]
    for j, index in enumerate(col_indices):
        df_material_mocl.columns.values[index] = f"{col}_{j+1}"


df_material_mocl['SOrg'] = df_material_mocl['SOrg'].fillna(0).astype(int).astype(str).str.strip()
df_material_mocl['Plnt'] = df_material_mocl['Plnt'].fillna(0).astype(int).astype(str).str.strip()
df_material_mocl['Material'] = df_material_mocl['Material'].fillna(0).astype(int).astype(str).str.strip()
df_material_mocl['Material_number'] = df_material_mocl['Material_number'].astype(str).str.strip()
df_material_mocl['X_Plant_Material_Status'] = df_material_mocl['X_Plant_Material_Status'].fillna(0).astype(int).astype(str).str.strip()
df_material_mocl['MS'] = df_material_mocl['MS'].fillna(0).astype(int).astype(str).str.strip()
df_material_mocl['Gross_weight'] = df_material_mocl['Gross_weight'].fillna(0).astype(str).str.strip().str.replace('.', '').str.replace(',', '.').astype(float)
df_material_mocl['WUn'] = df_material_mocl['WUn'].astype(str).str.strip()
df_material_mocl['Spart'] = df_material_mocl['Spart'].astype(str).str.strip()
df_material_mocl['ValidFrom'] = pd.to_datetime(df_material_mocl['ValidFrom'], errors="coerce", format='%d.%m.%Y')
df_material_mocl['Minorder_qty'] = df_material_mocl['Minorder_qty'].fillna(0).astype(str).str.strip().str.replace('.', '').str.replace(',', '.').astype(float)
df_material_mocl['BUn'] = df_material_mocl['BUn'].astype(str).str.strip()
df_material_mocl['Orig'] = df_material_mocl['Orig'].astype(str).str.strip()
df_material_mocl['Web'] = df_material_mocl['Web'].astype(str).str.strip()
df_material_mocl['FM_rel'] = df_material_mocl['FM_rel'].astype(str).str.strip()
df_material_mocl['Av'] = df_material_mocl['Av'].astype(str).str.strip()
df_material_mocl['PGr'] = df_material_mocl['PGr'].astype(str).str.strip()
df_material_mocl['GRT'] = df_material_mocl['GRT'].fillna(0).astype(str).str.strip().str.replace('.', '').str.replace(',', '.').astype(float)
df_material_mocl['Typ'] = df_material_mocl['Typ'].astype(str).str.strip()
df_material_mocl['MRPCn'] = df_material_mocl['MRPCn'].astype(str).str.strip()
df_material_mocl['Minlot_size'] = df_material_mocl['Minlot_size'].fillna(0).astype(str).str.strip().str.replace('.', '').str.replace(',', '.').astype(float)
df_material_mocl['BUn1'] = df_material_mocl['BUn1'].astype(str).str.strip()
df_material_mocl['SPT'] = df_material_mocl['SPT'].astype(str).str.strip()
df_material_mocl['PDT'] = df_material_mocl['PDT'].fillna(0).astype(str).str.strip().str.replace('.', '').str.replace(',', '.').astype(float)
df_material_mocl['TABCD'] = df_material_mocl['TABCD'].astype(str).str.strip()
df_material_mocl['XYZ'] = df_material_mocl['XYZ'].astype(str).str.strip()
df_material_mocl['Pl'] = df_material_mocl['Pl'].astype(str).str.strip()
df_material_mocl['Safety_Stock'] = df_material_mocl['Safety_Stock'].fillna(0).astype(str).str.strip().str.replace('.', '').str.replace(',', '.').astype(float)
df_material_mocl['Rounding_val'] = df_material_mocl['Rounding_val'].astype(str).str.strip()
df_material_mocl['BUn2'] = df_material_mocl['BUn2'].astype(str).str.strip()
df_material_mocl['Rprofile'] = df_material_mocl['Rprofile'].astype(str).str.strip()
df_material_mocl['LS'] = df_material_mocl['LS'].astype(str).str.strip()
df_material_mocl['Min_dely_qty'] = df_material_mocl['Min_dely_qty'].fillna(0).astype(str).str.strip().str.replace('.', '').str.replace(',', '.').astype(float)
df_material_mocl['BUn3'] = df_material_mocl['BUn3'].astype(str).str.strip()
df_material_mocl['key_material'] = df_material_mocl['SOrg'] + '/' + df_material_mocl['Material']
df_material_mocl['key_material'] = df_material_mocl['key_material'].astype(str).str.strip()

df_material_mocl.to_csv(material_8650_processed_path, index=False, encoding='latin1')
df_material_mocl.to_csv(material_8650_exported_path, index=False, encoding='latin1')


