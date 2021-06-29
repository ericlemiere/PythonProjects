from tkinter import *
import tkinter as tk
from tkinter import messagebox

import Student_Tracking_main
import Student_func


def loadGUI(self):

    # =============== LABELS ===================
    self.lbl_fname = tk.Label(self.master,text="First Name:",bg="#F0F0F0")
    self.lbl_fname.grid(row=0,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
    self.lbl_lname = tk.Label(self.master,text="Last Name:",bg="#F0F0F0")
    self.lbl_lname.grid(row=0,column=2,padx=(27,0),pady=(10,0),sticky=N+W)
    self.lbl_phone = tk.Label(self.master,text="Phone Number:",bg="#F0F0F0")
    self.lbl_phone.grid(row=2,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
    self.lbl_email = tk.Label(self.master,text="Email Address:",bg="#F0F0F0")
    self.lbl_email.grid(row=2,column=2,padx=(27,0),pady=(10,0),sticky=N+W)
    self.lbl_course = tk.Label(self.master, text="Course:",bg="#F0F0F0")
    self.lbl_course.grid(row=4,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
    


    # =============== TEXT BOXES ===================
    self.txt_fname = tk.Entry(self.master, text= "")
    self.txt_fname.grid(row=1, column = 0, rowspan = 1, columnspan = 2, padx=(30,40), pady=(0,0), sticky=N+E+W)
    self.txt_lname = tk.Entry(self.master, text= "")
    self.txt_lname.grid(row=1, column = 2, rowspan = 1, columnspan = 2, padx=(30,40), pady=(0,0), sticky=N+E+W)
    self.txt_phone = tk.Entry(self.master, text= "")
    self.txt_phone.grid(row=3, column = 0, rowspan = 1, columnspan = 2, padx=(30,40), pady=(0,0), sticky=N+E+W)
    self.txt_email = tk.Entry(self.master, text= "")
    self.txt_email.grid(row=3, column = 2, rowspan = 1, columnspan = 2, padx=(30,40), pady=(0,0), sticky=N+E+W)
    self.txt_course = tk.Entry(self.master, text="")
    self.txt_course.grid(row=5, column=0, rowspan = 1, columnspan = 4, padx=(30,40), pady=(0,0), sticky=N+E+W)


    # =============== BUTTONS ===================
    self.btn_add = tk.Button(self.master, width=12, height=2, text="Submit", command=lambda: Student_func.addToList(self))
    self.btn_add.grid(row=6, column=0, padx=(25,0), pady=(35,35), sticky=W)

    self.btn_delete = tk.Button(self.master, width = 12, height = 2, text="Delete", command=lambda: Student_func.deleteStudent(self))
    self.btn_delete.grid(row=7, column=7, padx=(25,0), pady=(45,10), sticky=E)
    
    self.btn_close = tk.Button(self.master, width=12, height=2, text="Close", command=lambda: Student_func.ask_quit(self))
    self.btn_close.grid(row=7, column=8, padx=(25,0), pady=(45,10), sticky=E)
    


    # ===== Define the listbox with a scrollbar =====
    self.scrollbar1 = Scrollbar(self.master, orient=VERTICAL)
    self.lstList1 = Listbox(self.master, exportselection=0, width=55, height=15, yscrollcommand=self.scrollbar1.set)
    self.lstList1.bind('<<ListboxSelect>>', lambda event: Student_func.onSelect(self, event))
    self.scrollbar1.config(command=self.lstList1.yview)
    self.scrollbar1.grid(row=0, column=9, rowspan=7, columnspan=1, padx=(0,0), pady=(0,0), sticky=E)
    self.lstList1.grid(row=0, column=5, rowspan=7, columnspan=4, padx=(25,0), pady=(0,0), sticky=W)    





if __name__ == "__main__":
    pass
