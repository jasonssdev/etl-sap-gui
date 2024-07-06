import win32com.client
import time

# Function to print information about connections and sessions
def print_sap_connections_info(application):
    try:
        print("Number of active connections:", application.Children.Count)
        for i in range(application.Children.Count):
            connection = application.Children(i)
            print(f"Connection {i}: {connection.Name}")
            print("  Number of sessions:", connection.Children.Count)
            for j in range(connection.Children.Count):
                session = connection.Children(j)
                print(f"  Session {j}: {session.Id}")
    except Exception as e:
        print(f"Error getting connection information: {e}")

# Function to log out from SAP
def logout_from_sap():
    try:
        SapGuiAuto = win32com.client.GetObject("SAPGUI")
        if not SapGuiAuto:
            raise Exception("Could not get SAPGUI object")
        
        application = SapGuiAuto.GetScriptingEngine
        if not application:
            raise Exception("Could not get SAP scripting engine")
        
        # Print connection and session information
        print_sap_connections_info(application)
        
        # Check if there are active connections
        if application.Children.Count == 0:
            raise Exception("No active SAP connections")
        
        # Assume there is only one active connection
        connection = application.Children(0)
        if not connection:
            raise Exception("Could not get SAP connection")

        # Check if there are active sessions in the connection
        if connection.Children.Count == 0:
            raise Exception("No active sessions in the SAP connection")

        session = connection.Children(0)
        if not session:
            raise Exception("Could not get SAP session")

        # Log out the session
        try:
            session.findById("wnd[0]/tbar[0]/okcd").text = "/nex"
            session.findById("wnd[0]/tbar[0]/btn[0]").press()
            print("Logout command sent.")
        except Exception as e:
            print(f"Error sending logout command: {e}")
            raise

        # Wait a moment and confirm logout if necessary
        time.sleep(1)
        try:
            if session.Children.Count > 0:
                session.findById("wnd[1]/usr/btnSPOP-OPTION1").press()
                print("Logout confirmed.")
        except Exception as e:
            print(f"Error confirming logout: {e}")
        
        print("Session logged out successfully")
    except Exception as e:
        print(f"Error logging out of session: {e}")

# Call the function to log out from SAP
if __name__ == "__main__":
    logout_from_sap()
