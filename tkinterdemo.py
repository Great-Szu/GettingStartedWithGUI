import tkinter

print(tkinter.TkVersion)
print(tkinter.TclVersion)

mainWindow = tkinter.Tk()
mainWindow.title("Hello")
mainWindow.geometry('640x480+8+8')
mainWindow.mainloop()