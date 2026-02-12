from tkinter import *
from PIL import Image, ImageTk  # using pillow due to a display error on macos

# label = an are widget that holds text and or an image wihtin a window

window = Tk()

img = Image.open("icon.jpeg")
photo = ImageTk.PhotoImage(img)

label = Label(
    window,
    text="Hello World",
    font=("Arial", 48, "bold"),
    fg="pink",
    bg="black",
    relief=RAISED,
    bd=10,
    padx=20,
    pady=20,
    image=photo,
    compound="center",
)

label.pack()
# label.place(x=0,y=0) sets the lebal to given corridenance

window.mainloop()
