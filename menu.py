from tkinter import *

def close():
    exit()
window = Tk()
menubar = Menu(window)

filemenu=Menu(menubar, tearoff=0)
settingmenu=Menu(menubar, tearoff=0)
filemenu.add_command(label="Close", command=close)
settingmenu.add_command(label="SpeedTest", command=close)
menubar.add_cascade(label="File", menu=filemenu)
menubar.add_cascade(label="Setting", menu=settingmenu)

window.config(menu=menubar)
window.mainloop()