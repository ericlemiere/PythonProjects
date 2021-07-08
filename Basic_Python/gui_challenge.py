import tkinter as tk
from tkinter import *
import tkinter.filedialog as fd
import os


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)


        self.master = master
        self.master.minsize(450,200)
        self.master.maxsize(450,500)
    
        self.master.title("Check files")
        self.master.configure(bg="lightgray")


        # BUTTONS
        self.btn1 = tk.Button(self.master, width=12, height=2, text="Browse...", highlightbackground="lightgray",
                              command=lambda: Browse(self))
        self.btn1.grid(row=1, column=0, padx=(15,0),pady=(40,0))

        self.btn2 = tk.Button(self.master, width=12, height=2, text="Browse...", highlightbackground="lightgray")
        self.btn2.grid(row=3, column=0, padx=(15,0), pady=(10,0))

        self.btnCFF = tk.Button(self.master, width=12, height=3, text="Check for files...", highlightbackground="lightgray")
        self.btnCFF.grid(row=5, column=0, padx=(15,0), pady=(10,0))

        self.btnClose = tk.Button(self.master, width=12, height=3, text="Close Program", highlightbackground="lightgray",
                                  command=lambda: CloseWindow(self))
        self.btnClose.grid(row=5, column=6, padx=(0,0), pady=(10,0), sticky=E)

        # TEXT BOXES
        self.text1 = tk.Text(self.master, width=30, height=1, font="helvetica")
        self.text1.grid(row=1, column=1, columnspan=6, padx=(15,0),pady=(40,0))

        self.text2 = tk.Text(self.master, width=30, height=1, font="helvetica")
        self.text2.grid(row=3, column=1, columnspan=6, padx=(15,0),pady=(10,0))





def Browse(self):
    thisDir = fd.askdirectory()
    UpdateBox(self,thisDir)


def UpdateBox(self,thisDir):
    print(thisDir)
    self.text1.insert(END, thisDir)
    



def CloseWindow(self):
    self.master.destroy()
    os._exit(0)






if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
