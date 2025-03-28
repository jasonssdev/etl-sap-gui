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

# Get environment variables
sap_layout = os.getenv("SAP_LAYOUT")
sap_file_path = os.getenv("SAP_FILE_PATH")
trans_bo = os.getenv("TRANS_BO")
file_bo = os.getenv("FILE_BO")

# Get the sales organization (SORG) from environment variables
sorg_ar = os.getenv("SORG_AR")
sorg_br = os.getenv("SORG_BR")
sorg_cl = os.getenv("SORG_CL")
sorg_mx = os.getenv("SORG_MX")

# Function to execute transaction ZBO2CS and download the report
def download_report_zbo2cs(session, trans_bo ,file_path, file_name, layout, sorgs):
    try:
        session.findById("wnd[0]").maximize()
        session.findById("wnd[0]/tbar[0]/okcd").text = trans_bo
        session.findById("wnd[0]").sendVKey(0)
        session.findById("wnd[0]/usr/btn[0]").press()

        # Enter values in the cells
        for index, sorg in enumerate(sorgs):
            cell_id = f"wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssub/1/2/tblSAPLALDBSINGLE/ctxt[1,{index}]"
            session.findById(cell_id).text = sorg
        
        session.findById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssub/1/2/tblSAPLALDBSINGLE/ctxt[1,3]").setFocus()
        session.findById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssub/1/2/tblSAPLALDBSINGLE/ctxt[1,3]").caretPosition = 4
        session.findById("wnd[1]/tbar[0]/btn[8]").press()

        # Set download options
        session.findById("wnd[0]/usr/chk[0]").selected = True
        session.findById("wnd[0]/usr/chk[0]").setFocus()
        session.findById("wnd[0]").sendVKey(2)
        session.findById("wnd[0]/usr/chk[1]").selected = True
        session.findById("wnd[0]/usr/chk[2]").selected = True
        session.findById("wnd[0]/usr/chk[5]").selected = True
        session.findById("wnd[0]/usr/chk[6]").selected = True
        session.findById("wnd[0]/usr/ctxt[45]").text = layout
        session.findById("wnd[0]/usr/ctxt[45]").setFocus()
        session.findById("wnd[0]/usr/ctxt[45]").caretPosition = len(layout)
        session.findById("wnd[0]/tbar[1]/btn[8]").press()
        session.findById("wnd[0]/shellcont/shell").pressToolbarContextButton("&MB_EXPORT")
        session.findById("wnd[0]/shellcont/shell").selectContextMenuItem("&PC")
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
        sorgs = [sorg_ar, sorg_br, sorg_cl, sorg_mx]
        download_report_zbo2cs(session, trans_bo, sap_file_path, file_bo, sap_layout, sorgs)
