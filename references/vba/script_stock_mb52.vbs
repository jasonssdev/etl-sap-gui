If Not IsObject(application) Then
   Set SapGuiAuto  = GetObject("SAPGUI")
   Set application = SapGuiAuto.GetScriptingEngine
End If
If Not IsObject(connection) Then
   Set connection = application.Children(0)
End If
If Not IsObject(session) Then
   Set session    = connection.Children(0)
End If
If IsObject(WScript) Then
   WScript.ConnectObject session,     "on"
   WScript.ConnectObject application, "on"
End If
session.findById("wnd[0]").maximize
session.findById("wnd[0]/tbar[0]/okcd").text = "/nMB52"
session.findById("wnd[0]").sendVKey 0
session.findById("wnd[0]/usr/btn[1]").press
session.findById("wnd[1]/usr/tabsTAB_STRIP/tabpINTL").select
session.findById("wnd[1]/usr/tabsTAB_STRIP/tabpINTL/ssub/1/2/tblSAPLALDBINTERVAL/ctxt[1,0]").text = "8650"
session.findById("wnd[1]/usr/tabsTAB_STRIP/tabpINTL/ssub/1/2/tblSAPLALDBINTERVAL/ctxt[1,1]").text = "8302"
session.findById("wnd[1]/usr/tabsTAB_STRIP/tabpINTL/ssub/1/2/tblSAPLALDBINTERVAL/ctxt[1,2]").text = "3000"
session.findById("wnd[1]/usr/tabsTAB_STRIP/tabpINTL/ssub/1/2/tblSAPLALDBINTERVAL/ctxt[1,3]").text = "8750"
session.findById("wnd[1]/usr/tabsTAB_STRIP/tabpINTL/ssub/1/2/tblSAPLALDBINTERVAL/ctxt[2,0]").text = "8699"
session.findById("wnd[1]/usr/tabsTAB_STRIP/tabpINTL/ssub/1/2/tblSAPLALDBINTERVAL/ctxt[2,1]").text = "8349"
session.findById("wnd[1]/usr/tabsTAB_STRIP/tabpINTL/ssub/1/2/tblSAPLALDBINTERVAL/ctxt[2,2]").text = "3099"
session.findById("wnd[1]/usr/tabsTAB_STRIP/tabpINTL/ssub/1/2/tblSAPLALDBINTERVAL/ctxt[2,3]").text = "8799"
session.findById("wnd[1]/usr/tabsTAB_STRIP/tabpINTL/ssub/1/2/tblSAPLALDBINTERVAL/ctxt[2,3]").setFocus
session.findById("wnd[1]/usr/tabsTAB_STRIP/tabpINTL/ssub/1/2/tblSAPLALDBINTERVAL/ctxt[2,3]").caretPosition = 4
session.findById("wnd[1]/tbar[0]/btn[0]").press
session.findById("wnd[1]/tbar[0]/btn[0]").press
session.findById("wnd[1]/tbar[0]/btn[8]").press
session.findById("wnd[0]/usr/ctxt[16]").text = "W2LOG_MAT"
session.findById("wnd[0]/usr/ctxt[16]").setFocus
session.findById("wnd[0]/usr/ctxt[16]").caretPosition = 9
session.findById("wnd[0]/tbar[1]/btn[8]").press
session.findById("wnd[0]/tbar[1]/btn[45]").press
session.findById("wnd[1]/usr/sub/2/sub/2/1/rad[1,0]").select
session.findById("wnd[1]/usr/sub/2/sub/2/1/rad[1,0]").setFocus
session.findById("wnd[1]/tbar[0]/btn[0]").press
session.findById("wnd[1]/usr/ctxt[0]").text = "c:\Users\sepujas\Dev\mat\data\raw"
session.findById("wnd[1]/usr/ctxt[1]").text = "tbl_stock_mb52.txt"
session.findById("wnd[1]/usr/ctxt[0]").setFocus
session.findById("wnd[1]/usr/ctxt[0]").caretPosition = 33
session.findById("wnd[1]/tbar[0]/btn[11]").press
session.findById("wnd[0]/tbar[0]/btn[3]").press
session.findById("wnd[0]/tbar[0]/btn[3]").press
