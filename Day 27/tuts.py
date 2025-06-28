from tkinter import *

def button_clicked():
    print("I got clicked!")
    my_label.config(text=inpt.get())

window = Tk()
window.title("My First GUI Program")
window.minsize(400, 300)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="I am a Label", font=("Courier", 24, "bold"))
my_label["text"] = "New Text"
my_label.config(text="New Text") # Both ways are possible
# my_label.place(x=0, y=0)
my_label.grid(column=0, row=0)
my_label.config(padx=20, pady=20)

# Button
button1 = Button(text="Click Me", command=button_clicked)
# button.place(x=10,y=100)
button1.grid(column=2, row=0)

button2 = Button(text="Click Me Again", command=button_clicked)
button2.grid(column=1, row=1)

# Entry
inpt = Entry(width=10)
# inpt.place(x=200,y=250)
inpt.grid(column=3, row=2)

window.mainloop()