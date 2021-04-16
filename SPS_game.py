from tkinter import *
from tkinter import messagebox
import random

root = Tk()

# root.geometry("400x100")

entry_box_1 = Entry(root, width = 50)
result_label = Label(root, text = "No result", pady = 10)
entry_box_2 = Entry(root, width = 50)

computer_score = 0
user_score = 0

entry_box_1.grid(row = 0, column = 0, columnspan = 1)
result_label.grid(row = 0, column = 1, columnspan = 1)
entry_box_2.grid(row = 0, column = 2, columnspan = 1)

def computerChoice(user_choice):
    global entry_box_1
    global entry_box_2

    # entry_box_1.pack_forget()
    # entry_box_1.pack_forget()



    computer_choice = random.randint(0, 2)

    print(computer_choice)

    if computer_choice == 0:
        computer_choice = 'Stone'
    elif computer_choice == 1:
        computer_choice = 'Paper'
    else:
        computer_choice = 'Scissor'
    print(computer_choice)

    entry_box_1.delete(0, "end")
    entry_box_2.delete(0, "end")
    entry_box_1.insert(0, user_choice)
    entry_box_2.insert(0, computer_choice)

    return computer_choice


def stone():
    global result_label
    result_label.destroy()

    computer_choice = computerChoice("Stone")

    if computer_choice == "Stone":
        result_label = Label(root, text="Draw", pady = 10)
        result_label.grid(row=0, column=1, columnspan=1)

    elif computer_choice == "Paper":
        global computer_score
        computer_score += 1
        result_label = Label(root, text="Computer Won", pady = 10)
        result_label.grid(row=0, column=1, columnspan=1)

    elif computer_choice == "Scissor":
        global user_score
        user_score += 1
        result_label = Label(root, text="You Won", pady = 10)
        result_label.grid(row=0, column=1, columnspan=1)


def paper():
    global result_label
    result_label.destroy()

    computer_choice = computerChoice("Paper")

    if computer_choice == "Stone":
        global user_score
        user_score += 1
        result_label = Label(root, text="You Won", pady = 10)
        result_label.grid(row=0, column=1, columnspan=1)

    elif computer_choice == "Paper":
        result_label = Label(root, text="Draw", pady = 10)
        result_label.grid(row=0, column=1, columnspan=1)

    elif computer_choice == "Scissor":
        global computer_score
        computer_score += 1
        result_label = Label(root, text="Computer Won", pady = 10)
        result_label.grid(row=0, column=1, columnspan=1)


def scissor():
    global result_label
    result_label.destroy()

    computer_choice = computerChoice("Scissor")

    if computer_choice == "Stone":
        global computer_score
        computer_score += 1
        result_label = Label(root, text="Computer Won", pady = 10)
        result_label.grid(row=0, column=1, columnspan=1)

    elif computer_choice == "Paper":
        global user_score
        user_score += 1
        result_label = Label(root, text="You Won", pady = 10)
        result_label.grid(row=0, column=1, columnspan=1)

    elif computer_choice == "Scissor":
        result_label = Label(root, text="Draw")
        result_label.grid(row=0, column=1, columnspan=1)


def show_result():
    global user_score
    global computer_score

    Label(root, text = "Your score: " + str(user_score), pady = 10).grid(row = 3, column = 0)
    Label(root, text = "Computer score: " + str(computer_score)).grid(row = 3, column = 1)

    result_message = ""

    if user_score == computer_score:
        result_message = "Ouuuu Its a draw... A close match!!!"
        Label(root, text = result_message, pady = 10).grid(row = 4, column = 1)

    elif user_score > computer_score:
        result_message = "Congratulation!!! You won the game..."
        Label(root, text = result_message, pady = 10).grid(row = 4, column = 1)

    else:
        result_message = "Ouch... You Lost!!! Better Luck Next Time"
        Label(root, text = result_message, pady = 10).grid(row = 4, column = 1)

    messagebox.showinfo("RESULT", result_message)

    button_exit = Button(root, text = "EXIT", bg = "red", command = root.quit)
    button_exit.grid(row = 5, column = 1)

button_stone = Button(root, text = "STONE", bg = "orange", command = stone)
button_paper = Button(root, text = "PAPER", bg = "white", command = paper)
button_scissor = Button(root, text = "SCISSOR", bg = "pink", command = scissor)
button_show_result = Button(root, text = "SHOW RESULT", bg = "green", command = show_result)

button_stone.grid(row = 1, column = 0, columnspan = 1)
button_paper.grid(row = 1, column = 1, columnspan = 1)
button_scissor.grid(row = 1, column = 2, columnspan = 1)
button_show_result.grid(row = 2,columnspan = 3)

root.mainloop()