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
session.findById("wnd[1]/usr/cntlGRID1/shellcont/shell").selectedRows = "0"
session.findById("wnd[1]/tbar[0]/btn[0]").press
session.findById("wnd[0]/usr/ctxt").setFocus
session.findById("wnd[0]/usr/ctxt").caretPosition = 0
session.findById("wnd[0]").sendVKey 4
session.findById("wnd[1]/usr/cntlGRID1/shellcont/shell").currentCellRow = 42
session.findById("wnd[1]/usr/cntlGRID1/shellcont/shell").firstVisibleRow = 24
session.findById("wnd[1]/usr/cntlGRID1/shellcont/shell").selectedRows = "42"
session.findById("wnd[1]/tbar[0]/btn[0]").press
session.findById("wnd[1]/tbar[0]/btn[0]").press
session.findById("wnd[0]/tbar[1]/btn[8]").press
session.findById("wnd[0]/usr/ctxt[6]").text = "8650"
session.findById("wnd[0]/usr/ctxt[8]").text = "8650"
session.findById("wnd[0]/usr/ctxt[40]").text = "W2LOG_MAT"
session.findById("wnd[0]/usr/ctxt[40]").setFocus
session.findById("wnd[0]/usr/ctxt[40]").caretPosition = 9
session.findById("wnd[0]/tbar[1]/btn[8]").press
session.findById("wnd[0]/tbar[1]/btn[45]").press
session.findById("wnd[1]/usr/sub/2/sub/2/1/rad[1,0]").select
session.findById("wnd[1]/usr/sub/2/sub/2/1/rad[1,0]").setFocus
session.findById("wnd[1]/tbar[0]/btn[0]").press
session.findById("wnd[1]/usr/ctxt[0]").text = "c:\Users\sepujas\Dev\mat2\data\raw"
session.findById("wnd[1]/usr/ctxt[1]").text = "tbl_material_mocl.txt"
session.findById("wnd[1]/usr/ctxt[1]").caretPosition = 21
session.findById("wnd[1]/tbar[0]/btn[11]").press
session.findById("wnd[0]/tbar[0]/btn[3]").press
session.findById("wnd[0]/tbar[0]/btn[3]").press
session.findById("wnd[0]/tbar[0]/btn[3]").press
