import pandas as pd
import os

def get_file_paths(base_path):
    inbound_file_path = os.path.join(base_path, 'data', 'raw', 'tbl_inbound.txt')
    inbound_processed_path = os.path.join(base_path, 'data', 'processed', 'tbl_inbound.csv')
    root_path = os.path.abspath(os.sep)
    sql_data_path = os.path.join(root_path, 'SQLdata', 'data')
    mat_sql_data_path = os.path.join(sql_data_path, 'mat')
    inbound_exported_path = os.path.join(mat_sql_data_path, 'tbl_inbound.csv')
    return inbound_file_path, inbound_processed_path, inbound_exported_path

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
        'Doc_No', 'Shipment', 'PurchDoc', 'Item_1', 'Material', 'Material_Description',
        'Plnt', 'SLoc', 'OUn', 'OUn1', 'Item_2', 'Delivery', 'Reference', 'Supplier', 'POrg',
        'PGr', 'Vendor', 'ShPt', 'Ext_Order_Pos', 'Ext_Order_Number', 'SupplVndr', 'TrackingNo',
        'Reservation', 'Reservation_item'
    ]
    for col in str_columns:
        df[col] = df[col].astype(str).str.strip()

    numeric_columns = ['POrg', 'Doc_No', 'Plnt', 'SLoc', 'Material', 'ShPt', 'Delivery', 'Reference', 'Vendor', 'Shipment', 'PurchDoc', 'Reservation']
    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0).astype(int).astype(str)

    df['PO_Quantity'] = df['PO_Quantity'].astype(str).str.replace('.', '').str.replace(',', '.').astype(float)

    date_columns = ['DelivDate', 'Doc_Date', 'Reservation_order_date']
    for col in date_columns:
        df[col] = pd.to_datetime(df[col], errors="coerce", format='%d.%m.%Y')

    df['Diffdays'] = df['Diffdays'].astype(str).str.strip().astype(float)

def transform_inbound(inbound_file_path, inbound_processed_path, inbound_exported_path):
    try:
        df_inbound = pd.read_csv(inbound_file_path, sep='\t', skiprows=3, encoding='latin1')

        # Eliminar columnas sin nombre
        unnamed_columns = [col for col in df_inbound.columns if 'Unnamed:' in col]
        df_inbound.drop(columns=unnamed_columns, inplace=True)

        clean_column_names(df_inbound)
        resolve_duplicate_columns(df_inbound)
        transform_columns(df_inbound)

        # Crear nueva columna 'key_material'
        df_inbound['key_material'] = (df_inbound['POrg'] + '/' + df_inbound['Material']).astype(str).str.strip()

        # Guardar los archivos transformados
        df_inbound.to_csv(inbound_processed_path, index=False, encoding='latin1')
        df_inbound.to_csv(inbound_exported_path, index=False, encoding='latin1')

        return df_inbound

    except Exception as e:
        print(f"Error processing file: {e}")
        return None

if __name__ == "__main__":
    base_path = os.getcwd()
    inbound_file_path, inbound_processed_path, inbound_exported_path = get_file_paths(base_path)
    transform_inbound(inbound_file_path, inbound_processed_path, inbound_exported_path)
