from tkinter import *
from tkinter import messagebox

root= Tk()
root.geometry("200x200")

def msg():
    messagebox.showerror("ERROR", "There seems to be an error with the information you entered. Click ok")

button= Button(root, text= "Go", command=msg)
button.place(x=100, y=60)

root.mainloop()