import subprocess
import os
from dotenv import load_dotenv

# Get base path
base_path = os.getcwd()
print(base_path)

# Get env path
env_path = os.path.join(base_path, '.env')

# Load environment variables from .env
load_dotenv(env_path)

# Get SAP_GUI path from .env
sap_gui_path = os.getenv("SAP_GUI_PATH")

# SAP GUI Open
def open_sap_gui(sap_gui_path):
    try:
        if not os.path.exists(sap_gui_path):
            raise FileNotFoundError(f"SAP GUI not found in path: {sap_gui_path}")
        
        subprocess.Popen([sap_gui_path])
        print("SAP GUI loading...")
        return True
    except Exception as e:
        print(f"SAP GUI error: {e}")


# Comprobación para evitar la ejecución al importar
if __name__ == "__main__":
    open_sap_gui(sap_gui_path)
