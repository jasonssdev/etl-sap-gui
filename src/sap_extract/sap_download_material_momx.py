import os
import win32com.client
from dotenv import load_dotenv
import time


# Get base path
base_path = os.getcwd()

# Get env path
env_path = os.path.join(base_path, '.env')

# Load environment variables from .env
load_dotenv(env_path)

# Get environment variables
sap_file_path = os.getenv("SAP_FILE_PATH")
sap_layout = os.getenv("SAP_LAYOUT")
trans_matmx = os.getenv("TRANS_MATMX")
file_matmx = os.getenv("FILE_MATMX")
sorg_mx = os.getenv("SORG_MX")
plant_mx1 = os.getenv("PLANT_MX1")

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

# Function to download material report from SAP
def download_material_report(session, trans_code, file_path, file_name, layout, sorg, plant):
    try:
        print("Maximizing window...")
        session.findById("wnd[0]").maximize()
        
        print("Entering transaction code...")
        session.findById("wnd[0]/tbar[0]/okcd").text = trans_code
        session.findById("wnd[0]").sendVKey(0)
        
        print("Pressing toolbar button...")
        session.findById("wnd[0]/tbar[1]/btn[19]").press()
        
        print("Selecting row in grid...")
        session.findById("wnd[1]/usr/cntlGRID1/shellcont/shell").selectedRows = "0"
        session.findById("wnd[1]/tbar[0]/btn[0]").press()
        
        print("Setting focus and sending VKey...")
        session.findById("wnd[0]/usr/ctxt").setFocus()
        session.findById("wnd[0]/usr/ctxt").caretPosition = 0
        session.findById("wnd[0]").sendVKey(4)
        
        print("Setting first visible row and selecting row in grid...")
        session.findById("wnd[1]/usr/cntlGRID1/shellcont/shell").firstVisibleRow = 24
        session.findById("wnd[1]/usr/cntlGRID1/shellcont/shell").currentCellRow = 42
        session.findById("wnd[1]/usr/cntlGRID1/shellcont/shell").selectedRows = "42"
        session.findById("wnd[1]/tbar[0]/btn[0]").press()
        session.findById("wnd[1]/tbar[0]/btn[0]").press()
        
        print("Pressing toolbar button...")
        session.findById("wnd[0]/tbar[1]/btn[8]").press()
        
        print("Entering plant and layout information...")
        session.findById("wnd[0]/usr/ctxt[6]").text = sorg
        session.findById("wnd[0]/usr/ctxt[8]").text = plant
        session.findById("wnd[0]/usr/ctxt[40]").text = layout
        session.findById("wnd[0]/usr/ctxt[40]").setFocus()
        session.findById("wnd[0]/usr/ctxt[40]").caretPosition = len(layout)
        session.findById("wnd[0]/tbar[1]/btn[8]").press()
        session.findById("wnd[0]/tbar[1]/btn[45]").press()
        
        print("Selecting radio button and pressing button...")
        session.findById("wnd[1]/usr/sub/2/sub/2/1/rad[1,0]").select()
        session.findById("wnd[1]/usr/sub/2/sub/2/1/rad[1,0]").setFocus()
        session.findById("wnd[1]/tbar[0]/btn[0]").press()
        
        print("Entering file path and name...")
        session.findById("wnd[1]/usr/ctxt[0]").text = file_path
        session.findById("wnd[1]/usr/ctxt[1]").text = file_name
        session.findById("wnd[1]/usr/ctxt[1]").caretPosition = len(file_name)
        session.findById("wnd[1]/tbar[0]/btn[11]").press()
        
        # Close the SAP windows
        for _ in range(3):
            session.findById("wnd[0]/tbar[0]/btn[3]").press()
        
        print("Report downloaded successfully")
        
    except Exception as e:
        print(f"Error downloading the report: {e}")


session = get_active_session()

if session:
    download_material_report(session, trans_matmx, sap_file_path, file_matmx, sap_layout, sorg_mx, plant_mx1)

