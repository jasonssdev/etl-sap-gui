import os
from dotenv import load_dotenv
import win32com.client

# Get base path
base_path = os.getcwd()

# Get env path
env_path = os.path.join(base_path, '.env')

# Load environment variables from .env
load_dotenv(env_path)

# get environment variables from .env
username = os.getenv("SAP_USERNAME")
password = os.getenv("SAP_PASSWORD")
client = os.getenv("SAP_CLIENT")
language = os.getenv("SAP_LANGUAGE")
sap_gui_environment = os.getenv("SAP_GUI_ENVIRONMENT")

# SAP Login function
def login_to_sap(username, password, client, language, sap_gui_environment):
    try:
        SapGuiAuto = win32com.client.GetObject("SAPGUI")
        application = SapGuiAuto.GetScriptingEngine
        connection = application.OpenConnection(sap_gui_environment, True)
        session = connection.Children(0)
        session.findById("wnd[0]/usr/txtRSYST-MANDT").text = client
        session.findById("wnd[0]/usr/txtRSYST-BNAME").text = username
        session.findById("wnd[0]/usr/pwdRSYST-BCODE").text = password
        session.findById("wnd[0]/usr/txtRSYST-LANGU").text = language
        session.findById("wnd[0]/tbar[0]/btn[0]").press()
        print("Login successful")
        return session
    except Exception as e:
        print(f"Login error: {e}")
    return None

# Login and verification
session = login_to_sap(username, password, client, language, sap_gui_environment)

if session:
    print("Session started successfully.")
else:
    print("Failed to start session.")
