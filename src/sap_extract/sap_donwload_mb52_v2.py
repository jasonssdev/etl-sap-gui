import sys
import os
from dotenv import load_dotenv

# base path
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

# Define the plant ranges
plant_ranges = [
    ("8650", "8699"),
    ("8302", "8349"),
    ("3000", "3099"),
    ("8750", "8799")
]

# Function to execute transaction MB52 and download the report
def download_report_mb52(session, trans_stock, file_path, file_name, layout, plant_ranges):
    try:
        session.findById("wnd[0]").maximize()
        session.findById("wnd[0]/tbar[0]/okcd").text = trans_stock
        session.findById("wnd[0]").sendVKey(0)
        session.findById("wnd[0]/usr/btn[1]").press()

        # Select the "Interval" tab (this simulates the VBA command)
        session.findById("wnd[1]/usr/tabsTAB_STRIP/tabpINTL").select()

        # Enter plant ranges
        for i, (start_plant, end_plant) in enumerate(plant_ranges):
            session.findById(f"wnd[1]/usr/tabsTAB_STRIP/tabpINTL/ssub/1/2/tblSAPLALDBINTERVAL/ctxt[1,{i}]").text = start_plant
            session.findById(f"wnd[1]/usr/tabsTAB_STRIP/tabpINTL/ssub/1/2/tblSAPLALDBINTERVAL/ctxt[2,{i}]").text = end_plant

        # Press the "Execute" button
        session.findById("wnd[1]/tbar[0]/btn[8]").press()

        # Set layout and download the report
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
        download_report_mb52(session, trans_stock, sap_file_path, file_stock, sap_layout, plant_ranges)
