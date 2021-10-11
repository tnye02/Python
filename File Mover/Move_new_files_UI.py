import shutil
import os.path
from datetime import date
import datetime
import pathlib
import time
import tkinter
from tkinter import *
from tkinter import filedialog

# define the window

class ParentWindow(Frame):
    def __init__ (self, master, *args, **kwargs):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width=False, height=True)
        self.master.geometry('{}x{}'.format(600, 250))
        self.master.title('File Mover')
        self.master.config(bg='black')

        self.source = StringVar()
        self.dest = StringVar()
        
    #Main Header
        self.labelMain = Label(self.master,text='File Mover', font=("Helvetica", 25), fg='white', bg='black')
        self.labelMain.grid(row=0, columnspan=2, padx=(150,0), pady=(15,0))
    #Source Button
        self.btnSrc = Button(self.master, text="Source", width=10, height=2, command=self.getSource)
        self.btnSrc.grid(row=1, column=0, padx=(15,0), pady=(15,0))
    #Source display window
        self.txtSrc = Label(self.master, text='', font=("Helvetica", 12), fg='black', bg='white', width=30, height=2)
        self.txtSrc.grid(row=1, column=1, padx=(5,0), pady=(15,0))
    #Destination Button
        self.btnDest = Button(self.master, text="Destination", width=10, height=2, command=self.getDest)
        self.btnDest.grid(row=2, column=0, padx=(15,0), pady=(15,0))
    #Destination display window
        self.txtDest = Label(self.master,text='', font=("Helvetica", 12), fg='black', bg='white', width=30, height=2)
        self.txtDest.grid(row=2, column=1, padx=(5,0), pady=(15,0))
    #Move button
        self.btnMove = Button(self.master, text="Move Files", width=10, height=2, command=self.move)
        self.btnMove.grid(row=3, columnspan=1, padx=(100,0), pady=(15,0))
    #Cancel button
        self.btnCancel = Button(self.master, text="Close", width=10, height=2, command=self.cancel)
        self.btnCancel.grid(row=3, columnspan=2, padx=(15,0), pady=(15,0))

    def getSource(self):
        self.source = filedialog.askdirectory()
        self.txtSrc.config(text='{}'.format(self.source))
        print(self.source)

    def getDest(self):
        self.dest = filedialog.askdirectory()
        self.txtDest.config(text='{}'.format(self.dest))
        print(self.dest)

    def move(self):
        src = self.source
        dst = self.dest
        files_list = os.listdir(src)

        for i in files_list:
            modTime = time.time() - os.path.getmtime(src+'/'+i)
            if modTime < 60*60*24 :
                shutil.move(src+'/'+i, dst)

    def cancel(self):
        self.master.destroy()



if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
