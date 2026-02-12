from tkinter import *

count = 0


def click():
    # global count
    # count += 1
    # print(count) #a clikcer counter example
    print("you clicked me")


window = Tk()

photo = PhotoImage(file="button.png")

button = Button(
    window,
    text="click me!",
    command=click,
    font=("Times New Roman", 50),
    fg="#00FF00",
    bg="brown",
    activebackground="brown",
    activeforeground="#00FF00",
    state=ACTIVE,
    image=photo,
    compound="bottom",
)

button.pack()


window.mainloop()
