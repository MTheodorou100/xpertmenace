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

def callback():
    print ("click!")
b=Button(window, text="Basic Speed Test", command=callback)
b.pack()
a=Button(window, text="Bandwidth Management", command=callback)
a.pack()
c=Button(window, text="Device Management", command=callback)
c.pack()
d=Button(window, text="Speed Limiter", command=callback)
d.pack()


window.mainloop()
