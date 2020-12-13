from tkinter import *
from tkinter import ttk
import os
from ast import literal_eval
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus.tables import Table
import datetime
from reportlab.lib import colors
from reportlab.platypus import TableStyle
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus.tables import Table
from reportlab.lib.pagesizes import letter
import sys
import tkinter.font as tkfont
import re


root = Tk()
root.title("MePod v1.11")
root.iconbitmap('D:/vs code proj/MePod/MePod/EXE builder/icon.ico')
root.geometry("500x500")

my_notbook = ttk.Notebook(root)
my_notbook.pack(pady=15)
my_frame1 = Frame(my_notbook, width=500, height=500, bg="blue")
my_frame2 = Frame(my_notbook, width=500, height=500, bg="red")

my_frame1.pack(fill="both", expand=1)
my_frame2.pack(fill="both", expand=1)

my_notbook.add(my_frame1, text="blue tab")
my_notbook.add(my_frame2, text="red tab")


root.mainloop()
