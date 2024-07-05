import pandas as pd
import os

base_path = os.getcwd()
print(base_path)

material_mobr_path = os.path.join(base_path, 'data', 'raw', 'tbl_material_8300.txt')
print(material_mobr_path)

material_8300_processed_path = os.path.join(base_path, 'data', 'processed', 'tbl_material_8300.csv')
print(material_8300_processed_path)

root_path = os.path.abspath(os.sep)
print(root_path)

sql_data_path = os.path.join(root_path, 'SQLdata', 'data')
print(sql_data_path)

mat_sql_data_path = os.path.join(sql_data_path, 'mat')
print(mat_sql_data_path)

material_8300_exported_path = os.path.join(mat_sql_data_path, 'tbl_material_8300.csv')
print(material_8300_exported_path)

df_material_mobr = pd.read_csv(material_mobr_path, sep='\t', skiprows=3, encoding='latin1')

unnamed_columns = [col for col in df_material_mobr.columns if 'Unnamed:' in col]
df_material_mobr.drop(columns=unnamed_columns, inplace=True)
column_titles = df_material_mobr.columns.tolist()
new_column_titles = {col: col.strip().replace(' ', '_').replace('-', '_').replace('.','') for col in column_titles}
df_material_mobr.rename(columns=new_column_titles, inplace=True)

column_counts = df_material_mobr.columns.value_counts()
duplicate_columns = column_counts[column_counts > 1].index

for col in duplicate_columns:
    col_indices = [i for i, x in enumerate(df_material_mobr.columns) if x == col]
    for j, index in enumerate(col_indices):
        df_material_mobr.columns.values[index] = f"{col}_{j+1}"


df_material_mobr['SOrg'] = df_material_mobr['SOrg'].fillna(0).astype(int).astype(str).str.strip()
df_material_mobr['Plnt'] = df_material_mobr['Plnt'].fillna(0).astype(int).astype(str).str.strip()
df_material_mobr['Material'] = df_material_mobr['Material'].fillna(0).astype(int).astype(str).str.strip()
df_material_mobr['Material_number'] = df_material_mobr['Material_number'].astype(str).str.strip()
df_material_mobr['X_Plant_Material_Status'] = df_material_mobr['X_Plant_Material_Status'].fillna(0).astype(int).astype(str).str.strip()
df_material_mobr['MS'] = df_material_mobr['MS'].fillna(0).astype(int).astype(str).str.strip()
df_material_mobr['Gross_weight'] = df_material_mobr['Gross_weight'].fillna(0).astype(str).str.strip().str.replace('.', '').str.replace(',', '.').astype(float)
df_material_mobr['WUn'] = df_material_mobr['WUn'].astype(str).str.strip()
df_material_mobr['Spart'] = df_material_mobr['Spart'].astype(str).str.strip()
df_material_mobr['ValidFrom'] = pd.to_datetime(df_material_mobr['ValidFrom'], errors="coerce", format='%d.%m.%Y')
df_material_mobr['Minorder_qty'] = df_material_mobr['Minorder_qty'].fillna(0).astype(str).str.strip().str.replace('.', '').str.replace(',', '.').astype(float)
df_material_mobr['BUn'] = df_material_mobr['BUn'].astype(str).str.strip()
df_material_mobr['Orig'] = df_material_mobr['Orig'].astype(str).str.strip()
df_material_mobr['Web'] = df_material_mobr['Web'].astype(str).str.strip()
df_material_mobr['FM_rel'] = df_material_mobr['FM_rel'].astype(str).str.strip()
df_material_mobr['Av'] = df_material_mobr['Av'].astype(str).str.strip()
df_material_mobr['PGr'] = df_material_mobr['PGr'].astype(str).str.strip()
df_material_mobr['GRT'] = df_material_mobr['GRT'].fillna(0).astype(str).str.strip().str.replace('.', '').str.replace(',', '.').astype(float)
df_material_mobr['Typ'] = df_material_mobr['Typ'].astype(str).str.strip()
df_material_mobr['MRPCn'] = df_material_mobr['MRPCn'].astype(str).str.strip()
df_material_mobr['Minlot_size'] = df_material_mobr['Minlot_size'].fillna(0).astype(str).str.strip().str.replace('.', '').str.replace(',', '.').astype(float)
df_material_mobr['BUn1'] = df_material_mobr['BUn1'].astype(str).str.strip()
df_material_mobr['SPT'] = df_material_mobr['SPT'].astype(str).str.strip()
df_material_mobr['PDT'] = df_material_mobr['PDT'].fillna(0).astype(str).str.strip().str.replace('.', '').str.replace(',', '.').astype(float)
df_material_mobr['TABCD'] = df_material_mobr['TABCD'].astype(str).str.strip()
df_material_mobr['XYZ'] = df_material_mobr['XYZ'].astype(str).str.strip()
df_material_mobr['Pl'] = df_material_mobr['Pl'].astype(str).str.strip()
df_material_mobr['Safety_Stock'] = df_material_mobr['Safety_Stock'].fillna(0).astype(str).str.strip().str.replace('.', '').str.replace(',', '.').astype(float)
df_material_mobr['Rounding_val'] = df_material_mobr['Rounding_val'].astype(str).str.strip()
df_material_mobr['BUn2'] = df_material_mobr['BUn2'].astype(str).str.strip()
df_material_mobr['Rprofile'] = df_material_mobr['Rprofile'].astype(str).str.strip()
df_material_mobr['LS'] = df_material_mobr['LS'].astype(str).str.strip()
df_material_mobr['Min_dely_qty'] = df_material_mobr['Min_dely_qty'].fillna(0).astype(str).str.strip().str.replace('.', '').str.replace(',', '.').astype(float)
df_material_mobr['BUn3'] = df_material_mobr['BUn3'].astype(str).str.strip()
df_material_mobr['key_material'] = df_material_mobr['SOrg'] + '/' + df_material_mobr['Material']
df_material_mobr['key_material'] = df_material_mobr['key_material'].astype(str).str.strip()

df_material_mobr.to_csv(material_8300_processed_path, index=False, encoding='latin1')
df_material_mobr.to_csv(material_8300_exported_path, index=False, encoding='latin1')


