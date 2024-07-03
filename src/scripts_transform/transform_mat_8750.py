import pandas as pd
import os

base_path = os.getcwd()
print(base_path)

material_moar_path = os.path.join(base_path, 'data', 'raw', 'tbl_material_8750.txt')
print(material_moar_path)

material_8750_processed_path = os.path.join(base_path, 'data', 'processed', 'tbl_material_8750.csv')
print(material_8750_processed_path)

df_material_moar = pd.read_csv(material_moar_path, sep='\t', skiprows=3, encoding='latin1')

unnamed_columns = [col for col in df_material_moar.columns if 'Unnamed:' in col]
df_material_moar.drop(columns=unnamed_columns, inplace=True)
column_titles = df_material_moar.columns.tolist()
new_column_titles = {col: col.strip().replace(' ', '_').replace('-', '_').replace('.','') for col in column_titles}
df_material_moar.rename(columns=new_column_titles, inplace=True)

column_counts = df_material_moar.columns.value_counts()
duplicate_columns = column_counts[column_counts > 1].index

for col in duplicate_columns:
    col_indices = [i for i, x in enumerate(df_material_moar.columns) if x == col]
    for j, index in enumerate(col_indices):
        df_material_moar.columns.values[index] = f"{col}_{j+1}"


df_material_moar['SOrg'] = df_material_moar['SOrg'].fillna(0).astype(int).astype(str).str.strip()
df_material_moar['Plnt'] = df_material_moar['Plnt'].fillna(0).astype(int).astype(str).str.strip()
df_material_moar['Material'] = df_material_moar['Material'].fillna(0).astype(int).astype(str).str.strip()
df_material_moar['Material_number'] = df_material_moar['Material_number'].astype(str).str.strip()
df_material_moar['X_Plant_Material_Status'] = df_material_moar['X_Plant_Material_Status'].fillna(0).astype(int).astype(str).str.strip()
df_material_moar['MS'] = df_material_moar['MS'].fillna(0).astype(int).astype(str).str.strip()
df_material_moar['Gross_weight'] = df_material_moar['Gross_weight'].fillna(0).astype(str).str.strip().str.replace('.', '').str.replace(',', '.').astype(float)
df_material_moar['WUn'] = df_material_moar['WUn'].astype(str).str.strip()
df_material_moar['Spart'] = df_material_moar['Spart'].astype(str).str.strip()
df_material_moar['ValidFrom'] = pd.to_datetime(df_material_moar['ValidFrom'], errors="coerce", format='%d.%m.%Y')
df_material_moar['Minorder_qty'] = df_material_moar['Minorder_qty'].fillna(0).astype(str).str.strip().str.replace('.', '').str.replace(',', '.').astype(float)
df_material_moar['BUn'] = df_material_moar['BUn'].astype(str).str.strip()
df_material_moar['Orig'] = df_material_moar['Orig'].astype(str).str.strip()
df_material_moar['Web'] = df_material_moar['Web'].astype(str).str.strip()
df_material_moar['FM_rel'] = df_material_moar['FM_rel'].astype(str).str.strip()
df_material_moar['Av'] = df_material_moar['Av'].astype(str).str.strip()
df_material_moar['PGr'] = df_material_moar['PGr'].astype(str).str.strip()
df_material_moar['GRT'] = df_material_moar['GRT'].fillna(0).astype(str).str.strip().str.replace('.', '').str.replace(',', '.').astype(float)
df_material_moar['Typ'] = df_material_moar['Typ'].astype(str).str.strip()
df_material_moar['MRPCn'] = df_material_moar['MRPCn'].astype(str).str.strip()
df_material_moar['Minlot_size'] = df_material_moar['Minlot_size'].fillna(0).astype(str).str.strip().str.replace('.', '').str.replace(',', '.').astype(float)
df_material_moar['BUn1'] = df_material_moar['BUn1'].astype(str).str.strip()
df_material_moar['SPT'] = df_material_moar['SPT'].astype(str).str.strip()
df_material_moar['PDT'] = df_material_moar['PDT'].fillna(0).astype(str).str.strip().str.replace('.', '').str.replace(',', '.').astype(float)
df_material_moar['TABCD'] = df_material_moar['TABCD'].astype(str).str.strip()
df_material_moar['XYZ'] = df_material_moar['XYZ'].astype(str).str.strip()
df_material_moar['Pl'] = df_material_moar['Pl'].astype(str).str.strip()
df_material_moar['Safety_Stock'] = df_material_moar['Safety_Stock'].fillna(0).astype(str).str.strip().str.replace('.', '').str.replace(',', '.').astype(float)
df_material_moar['Rounding_val'] = df_material_moar['Rounding_val'].astype(str).str.strip()
df_material_moar['BUn2'] = df_material_moar['BUn2'].astype(str).str.strip()
df_material_moar['Rprofile'] = df_material_moar['Rprofile'].astype(str).str.strip()
df_material_moar['LS'] = df_material_moar['LS'].astype(str).str.strip()
df_material_moar['Min_dely_qty'] = df_material_moar['Min_dely_qty'].fillna(0).astype(str).str.strip().str.replace('.', '').str.replace(',', '.').astype(float)
df_material_moar['BUn3'] = df_material_moar['BUn3'].astype(str).str.strip()
df_material_moar['key_material'] = df_material_moar['SOrg'] + '/' + df_material_moar['Material']
df_material_moar['key_material'] = df_material_moar['key_material'].astype(str).str.strip()

df_material_moar.to_csv(material_8750_processed_path, index=False, encoding='latin1')

