import pandas as pd
import os

def get_file_paths(base_path):
    material_mocl_path = os.path.join(base_path, 'data', 'raw', 'tbl_material_8650.txt')
    material_8650_processed_path = os.path.join(base_path, 'data', 'processed', 'tbl_material_8650.csv')
    root_path = os.path.abspath(os.sep)
    sql_data_path = os.path.join(root_path, 'SQLdata', 'data')
    mat_sql_data_path = os.path.join(sql_data_path, 'mat')
    material_8650_exported_path = os.path.join(mat_sql_data_path, 'tbl_material_8650.csv')
    return material_mocl_path, material_8650_processed_path, material_8650_exported_path

def clean_column_names(df):
    new_column_titles = {col: col.strip().replace(' ', '_').replace('-', '_').replace('.', '') for col in df.columns}
    df.rename(columns=new_column_titles, inplace=True)

def resolve_duplicate_columns(df):
    column_counts = df.columns.value_counts()
    duplicate_columns = column_counts[column_counts > 1].index

    for col in duplicate_columns:
        col_indices = [i for i, x in enumerate(df.columns) if x == col]
        for j, index in enumerate(col_indices):
            df.columns.values[index] = f"{col}_{j + 1}"

def transform_columns(df):
    str_columns = [
        'SOrg', 'Plnt', 'Material', 'Material_number', 'X_Plant_Material_Status', 'MS', 'WUn', 'Spart', 
        'BUn', 'Orig', 'Web', 'FM_rel', 'Av', 'PGr', 'Typ', 'MRPCn', 'BUn1', 'SPT', 'TABCD', 'XYZ', 
        'Pl', 'Rounding_val', 'BUn2', 'Rprofile', 'LS', 'BUn3'
    ]
    for col in str_columns:
        df[col] = df[col].astype(str).str.strip()

    numeric_columns = ['SOrg', 'Plnt', 'Material', 'X_Plant_Material_Status', 'MS']
    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0).astype(int).astype(str)

    float_columns = ['Gross_weight', 'Minorder_qty', 'GRT', 'Minlot_size', 'PDT', 'Safety_Stock', 'Min_dely_qty']
    for col in float_columns:
        df[col] = df[col].astype(str).str.replace('.', '').str.replace(',', '.').astype(float)

    date_columns = ['ValidFrom']
    for col in date_columns:
        df[col] = pd.to_datetime(df[col], errors="coerce", format='%d.%m.%Y')

def transform_mat_8650(material_mocl_path, processed_path, exported_path):
    try:
        df_material_mocl = pd.read_csv(material_mocl_path, sep='\t', skiprows=3, encoding='latin1', low_memory=False)

        unnamed_columns = [col for col in df_material_mocl.columns if 'Unnamed:' in col]
        df_material_mocl.drop(columns=unnamed_columns, inplace=True)

        clean_column_names(df_material_mocl)
        resolve_duplicate_columns(df_material_mocl)
        transform_columns(df_material_mocl)

        # Crear nueva columna 'key_material'
        df_material_mocl['key_material'] = (df_material_mocl['SOrg'] + '/' + df_material_mocl['Material']).astype(str).str.strip()

        # Guardar los archivos transformados
        df_material_mocl.to_csv(processed_path, index=False, encoding='latin1')
        df_material_mocl.to_csv(exported_path, index=False, encoding='latin1')

        return df_material_mocl

    except FileNotFoundError as e:
        print(f"File not found: {e.filename}")
    except pd.errors.ParserError as e:
        print(f"Error parsing file: {e}")
    except Exception as e:
        print(f"Error processing file: {e}")

    return None

if __name__ == "__main__":
    base_path = os.getcwd()
    material_mocl_path, material_8650_processed_path, material_8650_exported_path = get_file_paths(base_path)
    transform_mat_8650(material_mocl_path, material_8650_processed_path, material_8650_exported_path)
