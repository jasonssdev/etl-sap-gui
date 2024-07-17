import psutil
import os

# Function to close the SAP Logon application
def close_sap_logon():
    try:
        # Iterate over all running processes
        for proc in psutil.process_iter(['pid', 'name']):
            # Check if the process name is 'saplogon.exe'
            if proc.info['name'] == 'saplogon.exe':
                print(f"Closing SAP Logon (PID: {proc.info['pid']})")
                try:
                    proc.terminate()
                    proc.wait(timeout=5)
                    print("SAP Logon closed successfully")
                except psutil.NoSuchProcess:
                    print(f"No such process: {proc.info['pid']}")
                except psutil.AccessDenied:
                    print(f"Access denied when trying to terminate process: {proc.info['pid']}")
                except psutil.TimeoutExpired:
                    print(f"Timeout expired when trying to terminate process: {proc.info['pid']}")
                except Exception as e:
                    print(f"Unexpected error: {e}")
                return
        
        print("SAP Logon is not running")
    except Exception as e:
        print(f"Error closing SAP Logon: {e}")

# Call the function to close SAP Logon
if __name__ == "__main__":
    close_sap_logon()
