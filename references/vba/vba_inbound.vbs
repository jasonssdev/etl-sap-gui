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
session.findById("wnd[0]/tbar[0]/okcd").text = "/nZSQ01"
session.findById("wnd[0]").sendVKey 0
session.findById("wnd[0]/tbar[1]/btn[19]").press
session.findById("wnd[1]/usr/cntlGRID1/shellcont/shell").currentCellRow = 3
session.findById("wnd[1]/usr/cntlGRID1/shellcont/shell").selectedRows = "3"
session.findById("wnd[1]/tbar[0]/btn[0]").press
session.findById("wnd[0]/usr/ctxt").setFocus
session.findById("wnd[0]/usr/ctxt").caretPosition = 13
session.findById("wnd[0]").sendVKey 4
session.findById("wnd[1]/usr/cntlGRID1/shellcont/shell").currentCellRow = 9
session.findById("wnd[1]/usr/cntlGRID1/shellcont/shell").selectedRows = "9"
session.findById("wnd[1]/tbar[0]/btn[0]").press
session.findById("wnd[1]/tbar[0]/btn[0]").press
session.findById("wnd[0]/tbar[1]/btn[8]").press
session.findById("wnd[0]/usr/ctxt[0]").text = "5241"
session.findById("wnd[0]/usr/ctxt[0]").caretPosition = 4
session.findById("wnd[0]/usr/btn[0]").press
session.findById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssub/1/2/tblSAPLALDBSINGLE/ctxt[1,0]").text = "5241"
session.findById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssub/1/2/tblSAPLALDBSINGLE/ctxt[1,1]").text = "5211"
session.findById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssub/1/2/tblSAPLALDBSINGLE/ctxt[1,2]").text = "5251"
session.findById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssub/1/2/tblSAPLALDBSINGLE/ctxt[1,3]").text = "5221"
session.findById("wnd[1]/tbar[0]/btn[8]").press
session.findById("wnd[0]/usr/ctxt[10]").text = "8650"
session.findById("wnd[0]/usr/ctxt[10]").setFocus
session.findById("wnd[0]/usr/ctxt[10]").caretPosition = 4
session.findById("wnd[0]/usr/btn[7]").press
session.findById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssub/1/2/tblSAPLALDBSINGLE/ctxt[1,0]").text = "8650"
session.findById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssub/1/2/tblSAPLALDBSINGLE/ctxt[1,1]").text = "8750"
session.findById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssub/1/2/tblSAPLALDBSINGLE/ctxt[1,2]").text = "3000"
session.findById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssub/1/2/tblSAPLALDBSINGLE/ctxt[1,3]").text = "8330"
session.findById("wnd[1]/tbar[0]/btn[8]").press
session.findById("wnd[0]/usr/ctxt[4]").text = "15.08.2024"
session.findById("wnd[0]/usr/ctxt[4]").setFocus
session.findById("wnd[0]/usr/ctxt[4]").caretPosition = 10
session.findById("wnd[0]/usr/btn[3]").press
session.findById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssub/1/2/tblSAPLALDBSINGLE/btn[0,0]").setFocus
session.findById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssub/1/2/tblSAPLALDBSINGLE/btn[0,0]").press
session.findById("wnd[2]/usr/cntlOPTION_CONTAINER/shellcont/shell").setCurrentCell 1,"TEXT"
session.findById("wnd[2]/usr/cntlOPTION_CONTAINER/shellcont/shell").selectedRows = "1"
session.findById("wnd[2]/tbar[0]/btn[0]").press
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
session.findById("wnd[1]/usr/ctxt[1]").text = "tbl_inbound.txt"
session.findById("wnd[1]/usr/ctxt[1]").caretPosition = 15
session.findById("wnd[1]/tbar[0]/btn[11]").press
session.findById("wnd[0]/tbar[0]/btn[3]").press
session.findById("wnd[0]/tbar[0]/btn[3]").press
session.findById("wnd[0]/tbar[0]/btn[3]").press
