import webbrowser

import tkinter
from tkinter import *

class ParentWindow(Frame):
    def __init__(self, master):                                 ## initialize the window
        Frame.__init__(self)

        self.master = master                                    ## set window parameters
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(700, 400))
        self.master.title('Web Page Generator')
        self.master.config(bg='lightgrey')

        self.varMessage = StringVar()                           ## declare the string variable


        ## display the window content and format it to the left side of the window
        self.lblWelcome = Label(self.master,text='Enter the message to display on the new tab here: ', font=("Arial", 18), fg='black', bg='lightgrey')
        self.lblWelcome.grid(row=0, column=0, padx=10, pady=5, sticky = W)

        self.txtMsg = Entry(self.master,text=self.varMessage, font=("Arial", 18), fg='black', bg='lightblue')
        self.txtMsg.grid(row=1, column=0, padx=10, pady=5, sticky = W)

        self.btnSubmit = Button(self.master, text='Submit', width=10, height=2, command=self.submit)
        self.btnSubmit.grid(row=2, column=0, padx=10, pady=5, sticky = W)

    ## declare the submit button method
    def submit(self):
        txtMsg = self.varMessage.get()

        ## create the html file and open in a new browser tab
        f = open("webPage.html", "w")
        f.write("<html> <body> <h1> {} </h1> </body> </html>".format(txtMsg))
        webbrowser.open_new_tab("webPage.html")

if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
