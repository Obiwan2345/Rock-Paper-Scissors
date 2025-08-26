import random
import tkinter as tk
from tkinter import ttk

options = ['rock', 'paper', 'scissors']

# Set initial score
user_score = 0
computer_score = 0

def rock(): # When rock button is clicked
    global user_score, computer_score # Lets python know not to make new local variables for user score and compute score
    page3.tkraise()
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
    page3.tkraise()
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
    page3.tkraise()
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

game_mode = None

def update_score():
    Label_Score.config(text=f"You: {user_score} | Computer: {computer_score}")

    global game_mode

    if game_mode == "first5":
        # Check if either computer or player has reached 5
        if user_score == 5 and computer_score < 5:
            page5.tkraise()
            Label_Score2.config(text=f"PLAYER WINS", font=("Press Start 2P", 14))
            Label_Score3.config(text=f"you: {user_score} | Computer: {computer_score}", font=("Segoe", 10)) # Displays the score
        elif computer_score == 5 and user_score < 5:
            page5.tkraise()
            Label_Score2.config(text="COMPUTER WINS", font=("Press Start 2P", 14))
            Label_Score3.config(text=f"you: {user_score} | Computer: {computer_score}", font=("Segoe", 10))# Displays the score
    elif game_mode == "first10":
        # Check if either computer or player has reached 10
        if user_score == 10 and computer_score < 10:
            page5.tkraise()
            Label_Score2.config(text="PLAYER WINS", font=("Press Start 2P", 14))
            Label_Score3.config(text=f"you: {user_score} | Computer: {computer_score}", font=("Segoe", 10))# Displays the score
        elif computer_score == 10 and user_score < 10:
            page5.tkraise()
            Label_Score2.config(text="COMPUTER WINS", font=("Press Start 2P", 14))
            Label_Score3.config(text=f"You: {user_score} | Computer: {computer_score}", font=("Segoe", 10))# Displays the score

def unlimited():
    global game_mode
    game_mode = "unlimited"
    page2.tkraise()
    update_score()

def first_to_five_click():
    global game_mode
    game_mode = "first5"
    page2.tkraise()
    update_score()

def first_to_ten_click():
    global game_mode
    game_mode = "first10"
    update_score()
    page2.tkraise()


def show_score(): # This function allows the user to see their score
    update_score()
    page4.tkraise()

def restart_game():
    global user_score, computer_score, game_mode
    user_score = 0
    computer_score = 0
    game_mode = None
    Label_Score.config(text="You: 0 | Computer: 0")
    page1.tkraise()  # back to main menu


root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("420x320")

container = ttk.Frame(root, padding=10)
container.pack(fill="both", expand=True)

page1 = ttk.Frame(container)
page2 = ttk.Frame(container)
page3 = ttk.Frame(container)
page4= ttk.Frame(container)
page5 = ttk.Frame(container)

for p in (page1, page2, page3, page4, page5):
    p.place(relx=0, rely=0, relwidth=1, relheight=1) # stack pages full size

def show_page1():
    page1.tkraise()

def show_page2():
    page2.tkraise()

# Page 1, The opening page where the user picks the mode they want to play
ttk.Label(page1, text="ROCK, PAPER, SCISSORS", font=("Press Start 2P", 14)).pack(pady=10)
ttk.Label(page1, text="Which mode do you like to play", font=("Press Start 2P", 8)).pack(pady=10)
ttk.Button(page1, text="Unlimited Mode", command=unlimited).pack(pady=10)
ttk.Button(page1, text="First to 5", command=first_to_five_click).pack(pady=10)
ttk.Button(page1, text="First to 10", command=first_to_ten_click).pack(pady=10)

# Page 2
ttk.Label(page2, text="ROCK, PAPER, SCISSORS", font=("Press Start 2P", 14)).pack(pady=10)
ttk.Label(page2, text="Click an option to play", font=("Press Start 2P", 8)).pack(pady=10)
ttk.Button(page2, text="Rock", command=rock).pack(pady=10)
ttk.Button(page2, text="Paper", command=paper).pack(pady=10)
ttk.Button(page2, text="Scissors", command=scissors).pack(pady=10)
ttk.Button(page2, text="Show score", command=show_score).pack(pady=10)

#Page 3
Label_Result = ttk.Label(page3, text="") # Configured to show who won the round played
Label_Result.pack(pady=10)
ttk.Button(page3, text="Play Again", command=show_page2).pack(pady=10)

#Page 4 The score page
Label_Score = ttk.Label(page4, text="You: 0 | Computer: 0", font=("Segoe UI", 14))
Label_Score.pack(pady=10)
ttk.Button(page4, text="Go back", command=show_page2).pack(pady=10) # Allows to resume game
ttk.Button(page4, text="Restart Game", command=restart_game).pack(pady=10) # Starts the game over entirely

# Page 5
Label_Score2 = ttk.Label(page5, text="") # Configured to show who won the entire round only for first to 5 and first to 10
Label_Score2.pack(pady=10)
Label_Score3 = ttk.Label(page5, text="") # Configured to show the score at the end of the game. Only for first to 5 and first to 10
Label_Score3.pack(pady=10)
ttk.Button(page5, text="Restart Game", command=restart_game).pack(pady=10)

show_page1()
root.mainloop()
