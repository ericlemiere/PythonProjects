from tkinter import *
from tkinter import messagebox
import tkinter as tk
import os
import sqlite3

import Student_Tracking_gui
import Student_Tracking_main




def createDB(self):
    conn = sqlite3.connect('Student_Tracking.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not exists tbl_student( \
                    ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                    FirstName TEXT, \
                    LastName TEXT, \
                    PhoneNumber TEXT, \
                    Email TEXT, \
                    CurrentCourse TEXT \
                    ;")
        conn.commit()
    conn.close()
    
                    
    
    


#def deleteStudent(self):




def addToList(self):
    fname = self.txt_fname.get().strip().title()
    lname = self.txt_lname.get()
    phone = self.txt_phone.get()
    email = self.txt_email.get()
    course = self.txt_course.get()

    




def ask_quit(self):
    if messagebox.askokcancel("Exit Program","Okay to exit application?"):
        self.master.destroy()
        os._exit(0)



#def onSelect(self, event):




if __name__ == "__main__":
    pass
