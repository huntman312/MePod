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


counter = 0

system = sys.platform
path = os.getcwd()


listA = os.listdir(path + "/" + "TOOL_DATABASE")

print(listA)
