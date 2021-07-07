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
                    );")
        conn.commit()
    conn.close()
    




def addToList(self):
    fname = self.txt_fname.get().strip().title()
    lname = self.txt_lname.get().strip().title()
    phone = self.txt_phone.get().strip()
    email = self.txt_email.get().strip()
    course = self.txt_course.get().strip().upper()

    

    listName = ("{}, {}".format(lname, fname))
    print(listName)


    if (len(fname) > 0) and (len(lname) > 0):
        conn = sqlite3.connect('Student_Tracking.db')
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_student \
                        (FirstName,LastName,PhoneNumber,Email,CurrentCourse) \
                        VALUES \
                        (?,?,?,?,?)", (fname,lname,phone,email,course))
        populate(self)
        conn.commit()
        
    else:
        messagebox.showerror("Missing Text Error",
                             "Please ensure that there is data in all four fields.")
            
                        
        
def populate(self):
    self.lstList1.delete(0,END)
    conn = sqlite3.connect('Student_Tracking.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM tbl_student")
        count = cursor.fetchone()[0]
        
        
        i=0

        while i<count:
            lnameOrder = "SELECT lastName, firstName, CurrentCourse FROM tbl_student ORDER BY lastName DESC"
            cursor.execute(lnameOrder)
            varList = cursor.fetchall()[i]
            tupLength = len(varList) # gets length of tuple (lastName,firstName). It's always 3.
            # Since I'm calling columns from tbl_student, it would print their names twice
            # tupLength will take care of that in the below loops
                       
            for item in varList:
                if tupLength == 3:
                    self.lstList1.insert(0,"{}, {}, {}".format(varList[0],varList[1], varList[2]))
                    tupLength = 0
            i = i + 1

        onClear(self)
        
    conn.close()


def onClear(self):
    self.txt_fname.delete(0,END)
    self.txt_lname.delete(0,END)
    self.txt_phone.delete(0,END)
    self.txt_email.delete(0,END)
    self.txt_course.delete(0,END)

    self.txt_phone.insert(0,"###-###-####")
    self.txt_email.insert(0,"example@example.com")



def ask_quit(self):
    if messagebox.askokcancel("Exit Program","Okay to exit application?"):
        self.master.destroy()
        os._exit(0)



#Select item in ListBox
def onSelect(self,event):
    #calling the event is the self.lstList1 widget
    varList = event.widget
    select = varList.curselection()[0] #records where cursor clicks
    value = varList.get(select) #gets string from select
    lastName = value.split(',')[0] #splits string at the comma (lastname, firstname)
    firstName = value.split(', ')[1]
    
    
    conn = sqlite3.connect('Student_Tracking.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("SELECT FirstName, LastName, PhoneNumber, Email, CurrentCourse, ID \
                        FROM tbl_student WHERE LastName = (?) AND FirstName = (?)", [lastName, firstName])


        varBody = cursor.fetchall()
        # This returns a tuple and we can slice it into parts using data[] during the iteration
        for data in varBody:
            self.txt_fname.delete(0,END)
            self.txt_fname.insert(0,data[0])
            self.txt_lname.delete(0,END)
            self.txt_lname.insert(0,data[1])
            self.txt_phone.delete(0,END)
            self.txt_phone.insert(0,data[2])
            self.txt_email.delete(0,END)
            self.txt_email.insert(0,data[3])
            self.txt_course.delete(0,END)
            self.txt_course.insert(0,data[4])






def deleteStudent(self):
    onClear(self)

    if messagebox.askokcancel("Delete Student Record","Are you sure you want to delete this student?"):
        try:
            index = self.lstList1.curselection()[0]
            indexInfo = self.lstList1.get(index)
            lastName = indexInfo.split(',')[0] #splits string at the comma (lastname, firstname)
            firstName = indexInfo.split(', ')[1]
            

            conn = sqlite3.connect('Student_Tracking.db')
            with conn:
                cursor = conn.cursor()
                cursor.execute("SELECT ID FROM tbl_student WHERE LastName = (?) AND FirstName = (?)",
                               [lastName, firstName])
                selectID = cursor.fetchone()[0]
                
                cursor.execute("DELETE FROM tbl_student WHERE ID = (?)", [selectID])


            self.lstList1.delete(index)

        except IndexError:
            pass



def updateStudent(self):
    
    try:
        index = self.lstList1.curselection()[0]
        indexInfo = self.lstList1.get(index)
        lastName = indexInfo.split(',')[0] #splits string at the comma (lastname, firstname)
        firstName = indexInfo.split(', ')[1]
            

        conn = sqlite3.connect('Student_Tracking.db')
        with conn:
            cursor = conn.cursor()
            cursor.execute("SELECT ID FROM tbl_student WHERE LastName = (?) AND FirstName = (?)",
                               [lastName, firstName])
            selectID = cursor.fetchone()[0]
                
            cursor.execute("DELETE FROM tbl_student WHERE ID = (?)", [selectID])


        self.lstList1.delete(index)
        
    except IndexError:
        pass

    addToList(self)
    onClear(self)


if __name__ == "__main__":
    pass
