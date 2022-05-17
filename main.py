from tkinter import *

window =Tk()
window.title("Mile to KM Converter")
window.minsize(width=500, height=300)
window.config(padx=15, pady=15)


my_label = Label(text="is equal to", font=("Arial", 24,))
my_label.place(x=0, y=100)

my_label_1 = Label(text="Miles", font=("Arial", 24,))


my_label_2 = Label(text="km", font=("Arial", 24,))
my_label_2.place(x=400, y=100)

my_label_3 = Label(text="0", font=("Arial", 24,))
my_label_3.place(x=250, y=100)

def button_clicked():
    miles = float(input.get())
    km = round(miles * 1.689,  2)
    my_label_3.config(text=km)


input = Entry(width=30)
input.place(x=180, y=50)
print(input.get())


button = Button(text="Calculate", width=30, command=button_clicked)
button.place(x=160, y=200)


window.mainloop()