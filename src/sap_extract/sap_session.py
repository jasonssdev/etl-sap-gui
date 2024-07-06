import win32com.client

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

if __name__ == "__main__":
    session = get_active_session()

    if session:
        print("Active session retrieved successfully.")
    else:
        print("Failed to retrieve active session.")
