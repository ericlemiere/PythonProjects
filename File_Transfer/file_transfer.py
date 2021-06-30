import shutil
import os, time
import datetime
from datetime import timedelta
import tkinter as tk
from tkinter import *
import tkinter.filedialog as fd



class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)


        self.master = master
        self.master.minsize(730,250)
        self.master.maxsize(730,250)
    
        self.master.title("Check files")
        self.master.configure(bg="lightgray")


        # BUTTONS
        self.btn1 = tk.Button(self.master, width=15, height=1, text="Browse...", highlightbackground="lightgray",
                              command=lambda: Browse(self,1))
        self.btn1.grid(row=1, column=1, padx=(15,0),pady=(40,0))

        self.btn2 = tk.Button(self.master, width=15, height=1, text="Browse...", highlightbackground="lightgray",
                              command=lambda: Browse(self,2))
        self.btn2.grid(row=3, column=1, padx=(15,0), pady=(40,0))

        self.btnCFF = tk.Button(self.master, width=15, height=3, text="Check for files...", highlightbackground="lightgray",
                                command=lambda: CheckFiles(self))
        self.btnCFF.grid(row=5, column=0, padx=(15,0), pady=(40,0))

        self.btnClose = tk.Button(self.master, width=12, height=3, text="Close Program", highlightbackground="lightgray",
                                  command=lambda: CloseWindow(self))
        self.btnClose.grid(row=5, column=7, padx=(0,0), pady=(40,0), sticky=E)

        # TEXT BOXES
        self.text1 = tk.Text(self.master, width=40, height=1, font="helvetica")
        self.text1.grid(row=1, column=2, columnspan=6, padx=(15,0),pady=(40,0))

        self.text2 = tk.Text(self.master, width=40, height=1, font="helvetica")
        self.text2.grid(row=3, column=2, columnspan=6, padx=(15,0),pady=(40,0))

        # LABELS
        self.lbl1 = tk.Label(self.master, bg="lightgray", text="Move from destination:")
        self.lbl1.grid(row=1, column=0, padx=(40,0), pady=(40,0), sticky=W)

        self.lbl2 = tk.Label(self.master, bg="lightgray", text="Move to destination:")
        self.lbl2.grid(row=3, column=0, padx=(40,0), pady=(40,0), sticky=W)


# ============================= FUNCTIONS ==================================

def Browse(self, num):
    thisDir = fd.askdirectory()
    if num == 1:
        UpdateBox1(self,thisDir)
    if num == 2:
        UpdateBox2(self,thisDir)
    else:
        print("Error")

# The UpdateBox functions show the file path in the text boxes on GUI
def UpdateBox1(self,thisDir):
    print(thisDir)
    self.text1.insert(END, thisDir)

def UpdateBox2(self,thisDir):
    print(thisDir)
    self.text2.insert(END, thisDir)
    

# Close window function for Close button
def CloseWindow(self):
    self.master.destroy()
    os._exit(0)



def CheckFiles(self):
        
    # get text from text box, end-1c deletes the carriage return,
    # then / is added to end of string to complete file path
    source = self.text1.get("1.0","end-1c") + "/"
    destination = self.text2.get("1.0","end-1c") + "/"

    # list files in source folder
    files = os.listdir(source)

    print("\nFiles modified in the last 24 hours:\n")
    
    for i in files:
        # thisFile creates an absolute path
        # files variable only contains a string of the name of file
        # it does not contain time information
        thisFile = os.path.join(source, i)

        # modTime variable gets last modified time with getmtime,
        # then converts that into datetime object for later comparisons
        modTime = datetime.datetime.fromtimestamp(os.path.getmtime(thisFile))

        # variable turns time into readable format
        timeFMT = time.ctime((os.path.getmtime(thisFile)))

        currentTime = datetime.datetime.now()

        # Compare times. If the time (currentTime - 24hours) is less than
        # the modified time, then perform the if statement
        if (currentTime - timedelta(hours=24)) <= modTime:
            print("{}: {}".format(i, timeFMT))
            shutil.copy(source+i, destination)

# ============================= END ==================================


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()




