import os
import tkinter as tk
from tkinter import simpledialog

# Meant to look like beginner code

x=tk.Tk()

x.withdraw()

y=simpledialog.askstring(title="input", prompt="What do you want to echo")

os.system("echo " + y)


# there you have it, no its not secure, no its not good, no its not even useful, but it meets the criteria of having a GUI for a shell command. 


# the project can be scaled up in many ways with many additions so as a programmer grows they can do a better job. 