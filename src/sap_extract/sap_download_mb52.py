import sys
import os
from dotenv import load_dotenv

# Agregar el directorio base al PYTHONPATH
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_path)

from sap_extract.sap_session import get_active_session

# Get base path
base_path = os.getcwd()

# Get env path
env_path = os.path.join(base_path, '.env')

# Load environment variables from .env
load_dotenv(env_path)
# Get the environment variables
sap_layout = os.getenv("SAP_LAYOUT")
sap_file_path = os.getenv("SAP_FILE_PATH")
trans_stock = os.getenv("TRANS_STOCK")
file_stock = os.getenv("FILE_STOCK")

# Get the plants from environment variables
plants = [
    os.getenv("PLANT_AR1"),
    os.getenv("PLANT_AR2"),
    os.getenv("PLANT_BR1"),
    os.getenv("PLANT_BR2"),
    os.getenv("PLANT_CL1"),
    os.getenv("PLANT_CL2"),
    os.getenv("PLANT_CL3"),
    os.getenv("PLANT_CL4"),
    os.getenv("PLANT_CL5"),
    os.getenv("PLANT_CL6"),
    os.getenv("PLANT_MX1"),
    os.getenv("PLANT_MX2"),
    os.getenv("PLANT_MX3"),
    os.getenv("PLANT_MX4"),
    os.getenv("PLANT_MX5"),
    os.getenv("PLANT_MX6"),
    os.getenv("PLANT_MX7")
]

# Function to execute transaction MB52 and download the report
def download_report_mb52(session, trans_stock, file_path, file_name, layout, plants):
    try:
        session.findById("wnd[0]").maximize()
        session.findById("wnd[0]/tbar[0]/okcd").text = trans_stock
        session.findById("wnd[0]").sendVKey(0)
        session.findById("wnd[0]/usr/btn[1]").press()

        # Enter values in the cells with scrolling
        cell_index = 0
        for plant in plants:
            cell_id = f"wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssub/1/2/tblSAPLALDBSINGLE/ctxt[1,{cell_index}]"
            session.findById(cell_id).text = plant
            cell_index += 1
            if cell_index > 7:  # If cell index exceeds 7, scroll down and reset index
                session.findById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssub/1/2/tblSAPLALDBSINGLE").verticalScrollbar.position += 1
                cell_index = 0
        
        session.findById("wnd[1]/tbar[0]/btn[8]").press()

        # Set download options
        session.findById("wnd[0]/usr/chk[3]").selected = True
        session.findById("wnd[0]/usr/ctxt[16]").text = layout
        session.findById("wnd[0]/usr/ctxt[16]").setFocus()
        session.findById("wnd[0]/usr/ctxt[16]").caretPosition = len(layout)
        session.findById("wnd[0]/tbar[1]/btn[8]").press()
        session.findById("wnd[0]/tbar[1]/btn[45]").press()
        session.findById("wnd[1]/usr/sub/2/sub/2/1/rad[1,0]").select()
        session.findById("wnd[1]/usr/sub/2/sub/2/1/rad[1,0]").setFocus()
        session.findById("wnd[1]/tbar[0]/btn[0]").press()

        # Specify file path and name
        session.findById("wnd[1]/usr/ctxt[0]").text = file_path
        session.findById("wnd[1]/usr/ctxt[1]").text = file_name
        session.findById("wnd[1]/usr/ctxt[1]").caretPosition = len(file_name)
        session.findById("wnd[1]/tbar[0]/btn[11]").press()

        # Handle the overwrite confirmation message if it appears
        try:
            session.findById("wnd[2]/usr/btnSPOP-OPTION1").press()
        except:
            pass  # If the confirmation window does not appear, simply continue

        print("Report downloaded successfully")
    except Exception as e:
        print(f"Error downloading the report: {e}")

if __name__ == "__main__":
    # Get the active session
    session = get_active_session()

    # Download the report if the session is obtained successfully
    if session:
        download_report_mb52(session, trans_stock, sap_file_path, file_stock, sap_layout, plants)


