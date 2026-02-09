from tkinter import *
from PIL import Image, ImageTk  # imports PILLOW for image formats suppourt


# widgets = GUI elements: buttons, textbooks, lables , images
# windows = servers as a container to hold or contain these widgets

window = Tk()  # instantiate an instanse of a window

window.geometry("420x350")

window.title("Hello World")

# JPEG IS NOT SUPPORTED USE PNG OR USE PILLOW LIB

# icon = PhotoImage(file="icon.jpeg") this is the syntaxt without PILLOW


# this is the syntaxt using PILLOW
img = Image.open("icon.jpeg")
icon = ImageTk.PhotoImage(img)

# Or one liner:
# icon = ImageTk.PhotoImage(Image.open("icon.jpeg"))

window.iconphoto(True, icon)  # sets the PhotoImage as the window icon

window.config(bg="black")  # configures the window


window.mainloop()  # plase a window on computer screen. listen for events
