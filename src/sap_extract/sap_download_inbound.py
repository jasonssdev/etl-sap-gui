import os
import win32com.client
from dotenv import load_dotenv
from datetime import datetime

# Get base path
base_path = os.getcwd()

# Get env path
env_path = os.path.join(base_path, '.env')

# Load environment variables from .env
load_dotenv(env_path)

# Get environment variables
sap_layout = os.getenv("SAP_LAYOUT")
sap_file_path = os.getenv("SAP_FILE_PATH")
trans_inbound = os.getenv("TRANS_INBOUND")
file_inbound = os.getenv("FILE_INBOUND")

# Get the sales organization (SORG) from environment variables
sorg_ar = os.getenv("SORG_AR")
sorg_br = os.getenv("SORG_BR")
sorg_cl = os.getenv("SORG_CL")
sorg_mx = os.getenv("SORG_MX")

# Get the company code from environment variables
code_ar = os.getenv("CODE_AR")
code_br = os.getenv("CODE_BR")
code_cl = os.getenv("CODE_CL")
code_mx = os.getenv("CODE_MX")

# Get today's date in the desired format
date = datetime.today().strftime('%d.%m.%Y')

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

# Function to download inbound report from SAP
def download_inbound_report(session, trans_code, file_path, file_name, layout, sorgs, company_codes, date):
    try:
        print("Maximizing window...")
        session.findById("wnd[0]").maximize()
        
        print("Entering transaction code...")
        session.findById("wnd[0]/tbar[0]/okcd").text = trans_code
        session.findById("wnd[0]").sendVKey(0)
        
        print("Pressing button 19...")
        session.findById("wnd[0]/tbar[1]/btn[19]").press()
        
        print("Selecting and pressing first row...")
        session.findById("wnd[1]/usr/cntlGRID1/shellcont/shell").currentCellRow = 3
        session.findById("wnd[1]/usr/cntlGRID1/shellcont/shell").selectedRows = "3"
        session.findById("wnd[1]/tbar[0]/btn[0]").press()
        
        print("Setting focus and sending key 4...")
        session.findById("wnd[0]/usr/ctxt").setFocus()
        session.findById("wnd[0]/usr/ctxt").caretPosition = 13
        session.findById("wnd[0]").sendVKey(4)
        
        print("Selecting and pressing row 9...")
        session.findById("wnd[1]/usr/cntlGRID1/shellcont/shell").currentCellRow = 9
        session.findById("wnd[1]/usr/cntlGRID1/shellcont/shell").selectedRows = "9"
        session.findById("wnd[1]/tbar[0]/btn[0]").press()
        session.findById("wnd[1]/tbar[0]/btn[0]").press()
        
        print("Pressing button 8...")
        session.findById("wnd[0]/tbar[1]/btn[8]").press()
        
        print("Entering and pressing company code...")
        session.findById("wnd[0]/usr/ctxt[0]").text = company_codes[0]
        session.findById("wnd[0]/usr/ctxt[0]").caretPosition = 4
        session.findById("wnd[0]/usr/btn[0]").press()
        
        # Enter company codes in the cells
        print("Entering company codes in cells...")
        cells = [
            "wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssub/1/2/tblSAPLALDBSINGLE/ctxt[1,0]",
            "wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssub/1/2/tblSAPLALDBSINGLE/ctxt[1,1]",
            "wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssub/1/2/tblSAPLALDBSINGLE/ctxt[1,2]",
            "wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssub/1/2/tblSAPLALDBSINGLE/ctxt[1,3]"
        ]
        for cell, value in zip(cells, company_codes):
            session.findById(cell).text = value
        
        print("Pressing button 8 again...")
        session.findById("wnd[1]/tbar[0]/btn[8]").press()
        
        print("Entering sales organizations...")
        session.findById("wnd[0]/usr/ctxt[10]").text = sorg_ar
        session.findById("wnd[0]/usr/ctxt[10]").setFocus()
        session.findById("wnd[0]/usr/ctxt[10]").caretPosition = 4
        session.findById("wnd[0]/usr/btn[7]").press()
        
        for cell, value in zip(cells, sorgs):
            session.findById(cell).text = value
        
        print("Pressing button 8 once more...")
        session.findById("wnd[1]/tbar[0]/btn[8]").press()
        
        print("Entering date and pressing buttons...")
        session.findById("wnd[0]/usr/ctxt[4]").text = date
        session.findById("wnd[0]/usr/ctxt[4]").setFocus()
        session.findById("wnd[0]/usr/ctxt[4]").caretPosition = 10
        session.findById("wnd[0]/usr/btn[3]").press()
        
        session.findById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssub/1/2/tblSAPLALDBSINGLE/btn[0,0]").setFocus()
        session.findById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssub/1/2/tblSAPLALDBSINGLE/btn[0,0]").press()
        
        session.findById("wnd[2]/usr/cntlOPTION_CONTAINER/shellcont/shell").setCurrentCell(1, "TEXT")
        session.findById("wnd[2]/usr/cntlOPTION_CONTAINER/shellcont/shell").selectedRows = "1"
        session.findById("wnd[2]/tbar[0]/btn[0]").press()
        
        print("Pressing button 8 after date...")
        session.findById("wnd[1]/tbar[0]/btn[8]").press()
        
        print("Entering layout...")
        session.findById("wnd[0]/usr/ctxt[16]").text = layout
        session.findById("wnd[0]/usr/ctxt[16]").setFocus()
        session.findById("wnd[0]/usr/ctxt[16]").caretPosition = 9
        session.findById("wnd[0]/tbar[1]/btn[8]").press()
        
        print("Exporting data...")
        session.findById("wnd[0]/tbar[1]/btn[45]").press()
        session.findById("wnd[1]/usr/sub/2/sub/2/1/rad[1,0]").select()
        session.findById("wnd[1]/usr/sub/2/sub/2/1/rad[1,0]").setFocus()
        session.findById("wnd[1]/tbar[0]/btn[0]").press()
        
        session.findById("wnd[1]/usr/ctxt[0]").text = file_path
        session.findById("wnd[1]/usr/ctxt[1]").text = file_name
        session.findById("wnd[1]/usr/ctxt[1]").caretPosition = len(file_name)
        session.findById("wnd[1]/tbar[0]/btn[11]").press()
        
        # Close the SAP windows
        print("Closing SAP windows...")
        for _ in range(3):
            session.findById("wnd[0]/tbar[0]/btn[3]").press()
        
        print("Report downloaded successfully")
        
    except Exception as e:
        print(f"Error downloading the report: {e}")

# Get the active session
session = get_active_session()

# Download the report if the session is obtained successfully
if session:
    sorgs = [sorg_ar, sorg_br, sorg_cl, sorg_mx]
    company_codes = [code_ar, code_br, code_cl, code_mx]
    download_inbound_report(session, trans_inbound, sap_file_path, file_inbound, sap_layout, sorgs, company_codes, date)
