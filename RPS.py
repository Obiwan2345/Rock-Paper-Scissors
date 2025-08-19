import random
import tkinter as tk
from tkinter import ttk

options = ['rock', 'paper', 'scissors']

# Set initial score
user_score = 0
computer_score = 0

def rock(): # When rock button is clicked
    global user_score, computer_score # Let's python know not to make new local variables for user score and compute score
    page2.tkraise()
    computer = random.choice(options)
    user = 'rock'

    if user == computer:
        Label_Result.config(text="It's a tie. Play again?", font=("Segoe UI", 17))

    elif computer == 'scissors':
        Label_Result.config(text="Computer chose scissors, you win", font=("Segoe UI", 17))
        user_score +=1
    elif computer == 'paper':
        Label_Result.config(text="Computer chose paper, you lose", font=("Segoe UI", 17))
        computer_score += 1
    update_score() # updates the score

def paper(): #When paper is clicked
    global user_score, computer_score
    page2.tkraise()
    computer = random.choice(options)
    user = 'paper'

    if user == computer:
        Label_Result.config(text="It's a tie. Play again?", font=("Segoe UI", 17))
    elif computer == 'rock':
        Label_Result.config(text="Computer chose rock, you win", font=("Segoe UI", 17))
        user_score += 1
    elif computer == 'scissors':
        Label_Result.config(text="Computer chose scissors, you lose", font=("Segoe UI", 17))
        computer_score += 1
    update_score()

def scissors(): #When scissors is clicked
    global user_score, computer_score
    page2.tkraise()
    computer = random.choice(options)
    user = 'scissors'

    if user == computer:
        Label_Result.config(text="It's a tie. Play again?", font=("Segoe UI", 17))
    elif computer == 'paper':
        Label_Result.config(text="Computer chose paper, you win", font=("Segoe UI", 17))
        user_score += 1
    elif computer == 'rock':
        Label_Result.config(text="Computer chose rock, you lose", font=("Segoe UI", 17))
        computer_score += 1
    update_score()

def update_score():
    Label_Score.config(text=f"You: {user_score} | Computer: {computer_score}")

root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("420x280")

container = ttk.Frame(root, padding=10)
container.pack(fill="both", expand=True)

page1 = ttk.Frame(container)
page2 = ttk.Frame(container)

for p in (page1, page2):
    p.place(relx=0, rely=0, relwidth=1, relheight=1) # stack pages full size

def show_page1():
    page1.tkraise()

# Page 1
ttk.Label(page1, text="ROCK, PAPER, SCISSORS", font=("Segoe UI", 22)).pack(pady=10)
ttk.Label(page1, text="Pick an option").pack(pady=10)
ttk.Button(page1, text="Rock", command=rock).pack(pady=10)
ttk.Button(page1, text="Paper", command=paper).pack(pady=10)
ttk.Button(page1, text="Scissors", command=scissors).pack(pady=10)

#Page 2
Label_Score = ttk.Label(page2, text="You: 0 | Computer: 0", font=("Segoe UI", 14))
Label_Score.pack(pady=10)
Label_Result = ttk.Label(page2, text="")
Label_Result.pack(pady=10)
ttk.Button(page2, text="Play Again", command=show_page1).pack(pady=10)

show_page1()
root.mainloop()
