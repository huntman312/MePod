from tkinter import *
from tkinter import ttk


def newGUI():

    running = True  # Global flag

    def scanning():
        if running:  # Only do this if the Stop button has not been clicked
        print "hello"

    # After 1 second, call scanning again (create a recursive loop)
        root.after(1000, scanning)

    def start():
        # Enable scanning by setting the global flag to True."""
        global running
        running = True

    def stop():
        # Stop scanning by setting the global flag to False."""
        global running
        running = False

    root = Tk()

    shipToLabel = Label(root, text="Where to ship?")
    shipToLabel.grid(row=0, column=0)

    shipTo = StringVar()
    shipToEntry = ttk.Entry(root, textvariable=shipTo)
    shipToEntry.grid(row=0, column=1)

    billToLabel = Label(root, text="Customer to bill?")
    billToLabel.grid(row=0, column=5)

    billTo = StringVar()
    billToEntry = ttk.Entry(root, textvariable=billTo)
    billToEntry.grid(row=0, column=6)

    myLabel1 = Label(root, text="select tool brand!")

    myLabel1.grid(row=5, column=0)

    combo1List = ["max", "tech", "omer", "senco"]

    def comboStuff():

        comboExample = ttk.Combobox(root, values=combo1List)

        comboExample.grid(row=5, column=1)

        print(comboExample.current(), comboExample.get())

        comboList.append(billToEntry.get())
        print(comboList)

    def clickMe():
        comboList.append(billToEntry.get())

    button = Button(root, text="test", command=comboStuff)
    button.grid(row=7, column=1)

    root.mainloop()


newGUI()
