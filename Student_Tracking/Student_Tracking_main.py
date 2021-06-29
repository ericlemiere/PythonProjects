from tkinter import *
import tkinter as tk

import Student_Tracking_gui
import Student_func


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
    

        # define master frame configuration
        self.master = master
        self.master.minsize(1100,400)
        self.master.maxsize(1100,400)

        self.master.title("Student Tracking")
        self.master.configure(bg="#F0F0F0")

        # This protocol method is a built-in tkinter method to catch if
        # the user clicks the upper corner "x" in the windows OS
        self.master.protocol("WM_DELETE_WINDOW", lambda: Student_func.ask_quit(self))
        arg = self.master


        Student_Tracking_gui.loadGUI(self)



















if __name__ == "__main__":

    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
