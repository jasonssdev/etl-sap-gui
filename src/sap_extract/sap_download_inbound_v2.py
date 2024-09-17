import sys
import os
from datetime import datetime
from dotenv import load_dotenv
import win32com.client

# Agregar el directorio base al PYTHONPATH
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_path)

from sap_extract.sap_session import get_active_session

# Cargar variables de entorno
env_path = os.path.join(base_path, '.env')
load_dotenv(env_path)

# Obtener variables de entorno
sap_layout = os.getenv("SAP_LAYOUT")
sap_file_path = os.getenv("SAP_FILE_PATH")
trans_inbound = os.getenv("TRANS_INBOUND")
file_inbound = os.getenv("FILE_INBOUND")

# Obtener datos de las organizaciones de ventas y códigos de compañía
sorg_ar = os.getenv("SORG_AR")
sorg_br = os.getenv("SORG_BR")
sorg_cl = os.getenv("SORG_CL")
sorg_mx = os.getenv("SORG_MX")

code_ar = os.getenv("CODE_AR")
code_br = os.getenv("CODE_BR")
code_cl = os.getenv("CODE_CL")
code_mx = os.getenv("CODE_MX")

# Obtener plantas
plant_ar1 = os.getenv("PLANT_AR1")
plant_br1 = os.getenv("PLANT_BR1")
plant_cl1 = os.getenv("PLANT_CL1")
plant_mx1 = os.getenv("PLANT_MX1")

# Obtener la fecha de hoy en el formato deseado
date = datetime.today().strftime('%d.%m.%Y')

def download_inbound_report(session, trans_code, file_path, file_name, layout, plants, company_codes, date):
    try:
        session.findById("wnd[0]").maximize()
        session.findById("wnd[0]/tbar[0]/okcd").text = trans_code
        session.findById("wnd[0]").sendVKey(0)
        
        session.findById("wnd[0]/tbar[1]/btn[19]").press()
        
        session.findById("wnd[1]/usr/cntlGRID1/shellcont/shell").currentCellRow = 3
        session.findById("wnd[1]/usr/cntlGRID1/shellcont/shell").selectedRows = "3"
        session.findById("wnd[1]/tbar[0]/btn[0]").press()

        session.findById("wnd[0]/usr/ctxt").setFocus()
        session.findById("wnd[0]/usr/ctxt").caretPosition = 13
        session.findById("wnd[0]").sendVKey(4)

        session.findById("wnd[1]/usr/cntlGRID1/shellcont/shell").currentCellRow = 9
        session.findById("wnd[1]/usr/cntlGRID1/shellcont/shell").selectedRows = "9"
        session.findById("wnd[1]/tbar[0]/btn[0]").press()
        session.findById("wnd[1]/tbar[0]/btn[0]").press()

        session.findById("wnd[0]/tbar[1]/btn[8]").press()

        session.findById("wnd[0]/usr/ctxt[0]").text = company_codes[0]
        session.findById("wnd[0]/usr/ctxt[0]").caretPosition = 4
        session.findById("wnd[0]/usr/btn[0]").press()

        cells = [
            "wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssub/1/2/tblSAPLALDBSINGLE/ctxt[1,0]",
            "wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssub/1/2/tblSAPLALDBSINGLE/ctxt[1,1]",
            "wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssub/1/2/tblSAPLALDBSINGLE/ctxt[1,2]",
            "wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssub/1/2/tblSAPLALDBSINGLE/ctxt[1,3]"
        ]
        for cell, value in zip(cells, company_codes):
            session.findById(cell).text = value
            print(value)


        session.findById("wnd[1]/tbar[0]/btn[8]").press()

        session.findById("wnd[0]/usr/ctxt[10]").text = plants[0]
        session.findById("wnd[0]/usr/ctxt[10]").setFocus()
        session.findById("wnd[0]/usr/ctxt[10]").caretPosition = 4
        session.findById("wnd[0]/usr/btn[7]").press()

        for cell, value in zip(cells, plants):
            session.findById(cell).text = value
            print(value)

        session.findById("wnd[1]/tbar[0]/btn[8]").press()

        session.findById("wnd[0]/usr/ctxt[4]").text = date
        session.findById("wnd[0]/usr/ctxt[4]").setFocus()
        session.findById("wnd[0]/usr/ctxt[4]").caretPosition = 10
        session.findById("wnd[0]/usr/btn[3]").press()

        session.findById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssub/1/2/tblSAPLALDBSINGLE/btn[0,0]").setFocus()
        session.findById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssub/1/2/tblSAPLALDBSINGLE/btn[0,0]").press()

        session.findById("wnd[2]/usr/cntlOPTION_CONTAINER/shellcont/shell").setCurrentCell(1, "TEXT")
        session.findById("wnd[2]/usr/cntlOPTION_CONTAINER/shellcont/shell").selectedRows = "1"
        session.findById("wnd[2]/tbar[0]/btn[0]").press()

        session.findById("wnd[1]/tbar[0]/btn[8]").press()

        session.findById("wnd[0]/usr/ctxt[16]").text = layout
        session.findById("wnd[0]/usr/ctxt[16]").setFocus()
        session.findById("wnd[0]/usr/ctxt[16]").caretPosition = 9
        session.findById("wnd[0]/tbar[1]/btn[8]").press()

        session.findById("wnd[0]/tbar[1]/btn[45]").press()
        session.findById("wnd[1]/usr/sub/2/sub/2/1/rad[1,0]").select()
        session.findById("wnd[1]/usr/sub/2/sub/2/1/rad[1,0]").setFocus()
        session.findById("wnd[1]/tbar[0]/btn[0]").press()

        session.findById("wnd[1]/usr/ctxt[0]").text = file_path
        session.findById("wnd[1]/usr/ctxt[1]").text = file_name
        session.findById("wnd[1]/usr/ctxt[1]").caretPosition = len(file_name)
        session.findById("wnd[1]/tbar[0]/btn[11]").press()

        for _ in range(3):
            session.findById("wnd[0]/tbar[0]/btn[3]").press()

        print("Report downloaded successfully")

    except Exception as e:
        print(f"Error downloading the report: {e}")

if __name__ == "__main__":
    session = get_active_session()
    if session:
        plants = [plant_ar1, plant_br1, plant_cl1, plant_mx1]
        company_codes = [code_ar, code_br, code_cl, code_mx]
        download_inbound_report(session, trans_inbound, sap_file_path, file_inbound, sap_layout, plants, company_codes, date)
