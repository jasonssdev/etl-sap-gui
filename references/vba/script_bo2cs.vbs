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
session.findById("wnd[0]/tbar[0]/okcd").text = "/nZBO2CS"
session.findById("wnd[0]").sendVKey 0
session.findById("wnd[0]/usr/btn[0]").press
session.findById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssub/1/2/tblSAPLALDBSINGLE/ctxt[1,0]").text = "8750"
session.findById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssub/1/2/tblSAPLALDBSINGLE/ctxt[1,1]").text = "8300"
session.findById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssub/1/2/tblSAPLALDBSINGLE/ctxt[1,2]").text = "8650"
session.findById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssub/1/2/tblSAPLALDBSINGLE/ctxt[1,3]").text = "3000"
session.findById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssub/1/2/tblSAPLALDBSINGLE/ctxt[1,3]").setFocus
session.findById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssub/1/2/tblSAPLALDBSINGLE/ctxt[1,3]").caretPosition = 4
session.findById("wnd[1]/tbar[0]/btn[8]").press
session.findById("wnd[0]/usr/chk[0]").selected = true
session.findById("wnd[0]/usr/chk[0]").setFocus
session.findById("wnd[0]").sendVKey 2
session.findById("wnd[0]/usr/chk[1]").selected = true
session.findById("wnd[0]/usr/chk[2]").selected = true
session.findById("wnd[0]/usr/chk[5]").selected = true
session.findById("wnd[0]/usr/chk[6]").selected = true
session.findById("wnd[0]/usr/ctxt[45]").text = "W2LOG_MAT"
session.findById("wnd[0]/usr/ctxt[45]").setFocus
session.findById("wnd[0]/usr/ctxt[45]").caretPosition = 9
session.findById("wnd[0]/tbar[1]/btn[8]").press
session.findById("wnd[0]/shellcont/shell").pressToolbarContextButton "&MB_EXPORT"
session.findById("wnd[0]/shellcont/shell").selectContextMenuItem "&PC"
session.findById("wnd[1]/usr/sub/2/sub/2/1/rad[1,0]").select
session.findById("wnd[1]/usr/sub/2/sub/2/1/rad[1,0]").setFocus
session.findById("wnd[1]/tbar[0]/btn[0]").press
session.findById("wnd[1]/usr/ctxt[0]").text = "C:\Users\sepujas\Documents\dev-projects\mat2\files\"
session.findById("wnd[1]/usr/ctxt[1]").text = "source_bo2cs.txt"
session.findById("wnd[1]/usr/ctxt[1]").caretPosition = 16
session.findById("wnd[1]/tbar[0]/btn[11]").press
session.findById("wnd[0]/tbar[0]/btn[15]").press
session.findById("wnd[0]/tbar[0]/btn[15]").press
