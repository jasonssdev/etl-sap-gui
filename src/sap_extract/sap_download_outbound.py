import os
import win32com.client
from dotenv import load_dotenv

# Get base path
base_path = os.getcwd()

# Get env path
env_path = os.path.join(base_path, '.env')

# Load environment variables from .env
load_dotenv(env_path)

# Get environment variables
sap_layout = os.getenv("SAP_LAYOUT")
sap_file_path = os.getenv("SAP_FILE_PATH")
trans_outbound = os.getenv("TRANS_OUTBOUND")
file_outbound = os.getenv("FILE_OUTBOUND")

# Get the sales organization (SORG) from environment variables
sorg_ar = os.getenv("SORG_AR")
sorg_br = os.getenv("SORG_BR")
sorg_cl = os.getenv("SORG_CL")
sorg_mx = os.getenv("SORG_MX")



# Function to connect to the active SAP session
def get_active_session():
    try:
        SapGuiAuto = win32com.client.GetObject("SAPGUI")
        if not SapGuiAuto:
            raise Exception("Could not get the SAPGUI object")
        
        application = SapGuiAuto.GetScriptingEngine
        if not application:
            raise Exception("Could not get the SAP scripting engine")
        
        # Assume there is only one active connection
        connection = application.Children(0)
        if not connection:
            raise Exception("Could not get the SAP connection")
        
        session = connection.Children(0)
        if not session:
            raise Exception("Could not get the SAP session")

        return session
    except Exception as e:
        print(f"Error getting the active session: {e}")
        return None

# Function to download outbound report from SAP
def download_outbound_report(session, trans_code, file_path, file_name, layout, sorgs):
    try:
        session.findById("wnd[0]").maximize()
        session.findById("wnd[0]/tbar[0]/okcd").text = trans_code
        session.findById("wnd[0]").sendVKey(0)
        
        session.findById("wnd[0]/usr/btn[5]").press()
        session.findById("wnd[0]/usr/btn[0]").press()

        # Enter values in the cells
        for index, sorg in enumerate(sorgs):
            cell_id = f"wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssub/1/2/tblSAPLALDBSINGLE/ctxt[1,{index}]"
            session.findById(cell_id).text = sorg
        
        session.findById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssub/1/2/tblSAPLALDBSINGLE/ctxt[1,3]").setFocus()
        session.findById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssub/1/2/tblSAPLALDBSINGLE/ctxt[1,3]").caretPosition = 4
        session.findById("wnd[1]/tbar[0]/btn[8]").press()

        session.findById("wnd[0]/usr/ctxt[2]").text = ""
        session.findById("wnd[0]/usr/ctxt[3]").text = ""
        session.findById("wnd[0]/usr/ctxt[3]").setFocus()
        session.findById("wnd[0]/usr/ctxt[3]").caretPosition = 0
        session.findById("wnd[0]/tbar[1]/btn[8]").press()
        session.findById("wnd[0]/tbar[1]/btn[18]").press()
        session.findById("wnd[0]/tbar[1]/btn[33]").press()
        session.findById("wnd[1]/usr/sub/1/cntlD500_CONTAINER/shellcont/shell").currentCellColumn = "TEXT"
        session.findById("wnd[1]/usr/sub/1/cntlD500_CONTAINER/shellcont/shell").clickCurrentCell()
        session.findById("wnd[0]/tbar[1]/btn[45]").press()
        session.findById("wnd[1]/usr/sub/2/sub/2/1/rad[1,0]").select()
        session.findById("wnd[1]/usr/sub/2/sub/2/1/rad[1,0]").setFocus()
        session.findById("wnd[1]/tbar[0]/btn[0]").press()
        session.findById("wnd[1]/usr/ctxt[0]").text = file_path
        session.findById("wnd[1]/usr/ctxt[1]").text = file_name
        session.findById("wnd[1]/usr/ctxt[1]").caretPosition = len(file_name)
        session.findById("wnd[1]/tbar[0]/btn[0]").press()
        session.findById("wnd[1]/tbar[0]/btn[11]").press()
        session.findById("wnd[0]/tbar[0]/btn[15]").press()
        session.findById("wnd[0]/tbar[0]/btn[15]").press()
        session.findById("wnd[0]/tbar[0]/btn[15]").press()
        
        print("Report downloaded successfully")
        
    except Exception as e:
        print(f"Error downloading the report: {e}")

if __name__ == "__main__":
    # Get the active session
    session = get_active_session()

    # Download the report if the session is obtained successfully
    if session:
        sorgs = [sorg_ar, sorg_br, sorg_cl, sorg_mx]
        download_outbound_report(session, trans_outbound, sap_file_path, file_outbound, sap_layout, sorgs)