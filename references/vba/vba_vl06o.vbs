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
session.findById("wnd[0]/tbar[0]/okcd").text = "/nVL06O"
session.findById("wnd[0]").sendVKey 0
session.findById("wnd[0]/usr/btn[5]").press
session.findById("wnd[0]/usr/btn[0]").press
session.findById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssub/1/2/tblSAPLALDBSINGLE/ctxt[1,0]").text = "8650"
session.findById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssub/1/2/tblSAPLALDBSINGLE/ctxt[1,1]").text = "8750"
session.findById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssub/1/2/tblSAPLALDBSINGLE/ctxt[1,2]").text = "3000"
session.findById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssub/1/2/tblSAPLALDBSINGLE/ctxt[1,3]").text = "8300"
session.findById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssub/1/2/tblSAPLALDBSINGLE/ctxt[1,3]").setFocus
session.findById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssub/1/2/tblSAPLALDBSINGLE/ctxt[1,3]").caretPosition = 4
session.findById("wnd[1]/tbar[0]/btn[8]").press
session.findById("wnd[0]/usr/ctxt[2]").text = ""
session.findById("wnd[0]/usr/ctxt[3]").text = ""
session.findById("wnd[0]/usr/ctxt[3]").setFocus
session.findById("wnd[0]/usr/ctxt[3]").caretPosition = 0
session.findById("wnd[0]/tbar[1]/btn[8]").press
session.findById("wnd[0]/tbar[1]/btn[18]").press
session.findById("wnd[0]/tbar[1]/btn[33]").press
session.findById("wnd[1]/usr/sub/1/cntlD500_CONTAINER/shellcont/shell").currentCellColumn = "TEXT"
session.findById("wnd[1]/usr/sub/1/cntlD500_CONTAINER/shellcont/shell").clickCurrentCell
session.findById("wnd[0]/tbar[1]/btn[45]").press
session.findById("wnd[1]/usr/sub/2/sub/2/1/rad[1,0]").select
session.findById("wnd[1]/usr/sub/2/sub/2/1/rad[1,0]").setFocus
session.findById("wnd[1]/tbar[0]/btn[0]").press
session.findById("wnd[1]/usr/ctxt[0]").text = "c:\Users\sepujas\Dev\mat2\data\raw"
session.findById("wnd[1]/usr/ctxt[1]").text = "tbl_vl06o.txt"
session.findById("wnd[1]/usr/ctxt[1]").caretPosition = 13
session.findById("wnd[1]/tbar[0]/btn[0]").press
session.findById("wnd[1]/tbar[0]/btn[11]").press
session.findById("wnd[0]/tbar[0]/btn[15]").press
session.findById("wnd[0]/tbar[0]/btn[15]").press
session.findById("wnd[0]/tbar[0]/btn[15]").press
