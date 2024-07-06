import pandas as pd
import os

def get_file_paths(base_path):
    bo2cs_file_path = os.path.join(base_path, 'data', 'raw', 'tbl_bo2cs.txt')
    bo2cs_processed_path = os.path.join(base_path, 'data', 'processed', 'tbl_bo2cs.csv')
    root_path = os.path.abspath(os.sep)
    sql_data_path = os.path.join(root_path, 'SQLdata', 'data')
    mat_sql_data_path = os.path.join(sql_data_path, 'mat')
    bo2cs_exported_path = os.path.join(mat_sql_data_path, 'tbl_bo2cs.csv')
    return bo2cs_file_path, bo2cs_processed_path, bo2cs_exported_path

def clean_column_names(df):
    new_column_titles = {col: col.strip().replace(' ', '_').replace('-', '_').replace('.', '') for col in df.columns}
    df.rename(columns=new_column_titles, inplace=True)

def transform_columns(df):
    str_columns = [
        'SOrg', 'SaTy', 'Sales_Doc', 'Sold_to', 'Name_1', 'CustLoy', 'FocCust', 'Territory',
        'Typ', 'Material', 'Item_Description', 'SU', 'BO_value', 'Curr', 'DS', 'DB', 'BOstatus',
        'BO', 'GM', 'unc', 'Description', 'SC', 'Route'
    ]
    for col in str_columns:
        df[col] = df[col].astype(str).str.strip()

    numeric_columns = ['SOrg', 'Sales_Doc', 'Material']
    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0).astype(int).astype(str)

    date_columns = [
        'On', 'InitReqDt', 'promised', 'MatAvDt', 'DlvDate', 'BOstat_changed', 'Reqdlvdt'
    ]
    for col in date_columns:
        df[col] = pd.to_datetime(df[col], errors="coerce", format='%d.%m.%Y')

    float_columns = ['Order_Qty', 'Corrqty', 'ConfirmQty']
    for col in float_columns:
        df[col] = df[col].astype(str).str.replace('.', '').str.replace(',', '.').astype(float)

def transform_bo2cs(bo2cs_file_path, bo2cs_processed_path, bo2cs_exported_path):
    try:
        df_bo2cs = pd.read_csv(bo2cs_file_path, sep='\t', skiprows=3, encoding='latin1')

        # Eliminar columnas sin nombre
        unnamed_columns = [col for col in df_bo2cs.columns if 'Unnamed:' in col]
        df_bo2cs.drop(columns=unnamed_columns, inplace=True)

        clean_column_names(df_bo2cs)
        transform_columns(df_bo2cs)

        # Crear nueva columna 'key_material'
        df_bo2cs['key_material'] = (df_bo2cs['SOrg'] + '/' + df_bo2cs['Material']).astype(str).str.strip()

        # Guardar los archivos transformados
        df_bo2cs.to_csv(bo2cs_processed_path, index=False, encoding='latin1')
        df_bo2cs.to_csv(bo2cs_exported_path, index=False, encoding='latin1')

        return df_bo2cs

    except FileNotFoundError as e:
        print(f"File not found: {e.filename}")
    except pd.errors.ParserError as e:
        print(f"Error parsing file: {e}")
    except Exception as e:
        print(f"Error processing file: {e}")

    return None

if __name__ == "__main__":
    base_path = os.getcwd()
    bo2cs_file_path, bo2cs_processed_path, bo2cs_exported_path = get_file_paths(base_path)
    transform_bo2cs(bo2cs_file_path, bo2cs_processed_path, bo2cs_exported_path)



