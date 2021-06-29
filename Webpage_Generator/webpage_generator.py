import webbrowser
import os
import tkinter as tk
from tkinter import *
import tkinter.filedialog as fd




# Create tkinter GUI
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)


        self.master = master
        self.master.minsize(600,200)
        self.master.maxsize(600,200)
        self.master.title("Webpage Generator")
        

        # LABEL
        self.lbl = Label(self.master, text="Please input the text to be displayed:")
        self.lbl.grid(row=1, column=0, padx=(15,0), pady=(40,0), sticky=W)

        # TEXT BOX
        self.text1 = tk.Text(self.master, width=70, height=4, font="helvetica")
        self.text1.grid(row=2, column=0, padx=(15,0),pady=(10,0), sticky=E)

        # BUTTON
        self.btn1 = tk.Button(self.master, text="Create Webpage", command=lambda: GetInput(self))
        self.btn1.grid(row=3, column=0, padx=(15,0), pady=(10,0), sticky=W)
        

        
# ==========================================================================
# Functions
# ==========================================================================

def GetInput(self):
    userInput = self.text1.get("1.0",END).splitlines()
    lineInput = """"""

    for line in userInput:
        lineInput = """{}\n{}""".format(lineInput,line)
        
    CreatePage(self, lineInput)
    print(lineInput)
    


def CreatePage(self, userInput):
    # Initialize/Open html doc
    webpage = open('index.html', "w") # "w" means the page is writeable

    message = userInput

    # Create html with insertable message
    webpage_html = """
    <!DOCTYPE html>
    <html>
        <head>
            <style>
                pre {{
                    display: block;
                    font-family: helvetica;
                    font-size: 3em;
                    text-align: center;
                    white-space: pre;
                    margin: 1em 0;
                }} 
            </style>
        </head>
        <body>
            <pre>{}</pre>
        </body>
    </html>
    """.format(message)

    webpage.write(webpage_html)
    webpage.close()

    # Open newly created file using the local path
    filename = 'file:///Users/ericlemiere/Documents/GitHub/PythonProjects/Webpage_Generator/index.html'
    webbrowser.open_new_tab(filename)


# ==========================================================================



if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
