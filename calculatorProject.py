from tkinter import *

root = Tk()

e = Entry(root, width = 50, borderwidth = 5)
e.grid(row = 0, column = 0, columnspan = 3)

def onclick(num):
    temp = e.get()
    e.delete(0, END)
    e.insert(0, temp + num)

def add():
    global operation
    operation = "add"
    global f_num
    f_num = e.get()
    e.delete(0, END)


def sub():
    global operation
    operation = "sub"
    global f_num
    f_num = e.get()
    e.delete(0, END)


def mul():
    global operation
    operation = "mul"
    global f_num
    f_num = e.get()
    e.delete(0, END)


def div():
    global operation
    operation = "div"
    global f_num
    f_num = e.get()
    e.delete(0, END)


def clear():
    e.delete(0, END)


def equal():
    temp = e.get()
    e.delete(0, END)
    if operation == "add":
        # label = Label(root, text = int(f_num) + int(e.get()))
        e.insert(0, int(f_num) + int(temp))
    elif operation == "sub":
        # label = Label(root, text=int(f_num) - int(e.get()))
        e.insert(0, int(f_num) - int(temp))
    elif operation == "mul":
        # label = Label(root, text = int(f_num) * int(e.get()))
        e.insert(0, int(f_num) * int(temp))
    elif operation == "div":
        # label = Label(root, text = int(f_num) / int(e.get()))
        e.insert(0, int(f_num) / int(temp))

button_1 = Button(root, text = "1", padx = 45, pady = 20, command = lambda: onclick("1"))
button_2 = Button(root, text = "2", padx = 45, pady = 20, command = lambda: onclick("2"))
button_3 = Button(root, text = "3", padx = 45, pady = 20, command = lambda: onclick("3"))
button_4 = Button(root, text = "4", padx = 45, pady = 20, command = lambda: onclick("4"))
button_5 = Button(root, text = "5", padx = 45, pady = 20, command = lambda: onclick("5"))
button_6 = Button(root, text = "6", padx = 45, pady = 20, command = lambda: onclick("6"))
button_7 = Button(root, text = "7", padx = 45, pady = 20, command = lambda: onclick("7"))
button_8 = Button(root, text = "8", padx = 45, pady = 20, command = lambda: onclick("8"))
button_9 = Button(root, text = "9", padx = 45, pady = 20, command = lambda: onclick("9"))
button_0 = Button(root, text = "0", padx = 45, pady = 20, command = lambda: onclick("0"))

button_add = Button(root, text = "+",bg = "blue", padx = 45, pady = 20, command = add)
button_sub = Button(root, text = "-",bg = "orange", padx = 45, pady = 20, command = sub)
button_mul = Button(root, text = "*",bg = "black",fg = "white", padx = 45, pady = 20, command = mul)
button_div = Button(root, text = "/",bg = "green", padx = 45, pady = 20, command = div)
button_clear = Button(root, text = "clear",bg = "red", padx = 38, pady = 20, command = clear)
button_equal = Button(root, text = "equal",bg = "white", padx = 38, pady = 20, command = equal)

button_7.grid(row = 1, column = 0)
button_8.grid(row = 1, column = 1)
button_9.grid(row = 1, column = 2)

button_4.grid(row = 2, column = 0)
button_5.grid(row = 2, column = 1)
button_6.grid(row = 2, column = 2)

button_1.grid(row = 3, column = 0)
button_2.grid(row = 3, column = 1)
button_3.grid(row = 3, column = 2)

button_add.grid(row = 4, column = 0)
button_sub.grid(row = 4, column = 1)
button_mul.grid(row = 4, column = 2)
button_div.grid(row = 5, column = 0)
button_clear.grid(row = 5, column = 1)
button_equal.grid(row = 5, column = 2)

root.mainloop()