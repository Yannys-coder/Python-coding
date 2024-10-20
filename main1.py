from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("image")
root.geometry("500x500")

upload= Image.open("PHOTO.jpg")
image= ImageTk.PhotoImage(upload)

label= Label(root, image=image, height = 300, width= 300)
label.place(x=150, y=150)
label2= Label(root, text="What you expect to see in FANTASY")
label2.place(x=150, y=400)


root.mainloop()