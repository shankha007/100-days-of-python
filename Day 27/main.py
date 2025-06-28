from tkinter import *

def mile_to_km_conv():
    mile = inpt.get()
    km = float(mile) * 1.6
    label3.config(text=int(km))

window = Tk()
window.title("Mile to Km Converter")
window.minsize(200, 100)
window.config(padx=20, pady=20)

inpt = Entry(width=20)
inpt.grid(row=1, column=1)
inpt.focus()

label1 = Label(text="Miles")
label1.grid(row=1, column=2)

label2 = Label(text="is equal to")
label2.grid(row=2, column=0)

label3 = Label(text="0")
label3.grid(row=2, column=1)

label4 = Label(text="Km")
label4.grid(row=2, column=2)

btn = Button(text="Calculate", command=mile_to_km_conv)
btn.grid(row=3, column=1)

window.mainloop()