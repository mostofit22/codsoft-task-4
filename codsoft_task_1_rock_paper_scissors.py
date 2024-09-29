import tkinter as tk
import random

# Function to decide the winner
def decide_winner(user_choice):
    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)
    
    # Update the label with both choices
    result_label.config(text=f"You chose: {user_choice}, Computer chose: {computer_choice}")
    
    if user_choice == computer_choice:
        outcome_label.config(text="It's a Tie!")
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        outcome_label.config(text="You Win!")
        update_score("user")
    else:
        outcome_label.config(text="Computer Wins!")
        update_score("computer")

# Function to update the score
def update_score(winner):
    global user_score, computer_score
    if winner == "user":
        user_score += 1
    else:
        computer_score += 1
    score_label.config(text=f"User: {user_score} | Computer: {computer_score}")

# Function to reset the game
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    score_label.config(text=f"User: {user_score} | Computer: {computer_score}")
    result_label.config(text="")
    outcome_label.config(text="")

# Initialize main window
window = tk.Tk()
window.title("Rock Paper Scissors Game")

# Set window size and background color
window.geometry("400x300")  # Make the window slightly larger
window.config(bg="light green")  # Set the background color to light green

# Track scores
user_score = 0
computer_score = 0

# Title label
title_label = tk.Label(window, text="Rock Paper Scissors", font=('Helvetica', 18), bg="light green")
title_label.pack(pady=10)

# User choice buttons
frame = tk.Frame(window, bg="light green")
frame.pack(pady=10)

rock_button = tk.Button(frame, text="Rock", width=10, command=lambda: decide_winner("Rock"))
rock_button.grid(row=0, column=0, padx=5)

paper_button = tk.Button(frame, text="Paper", width=10, command=lambda: decide_winner("Paper"))
paper_button.grid(row=0, column=1, padx=5)

scissors_button = tk.Button(frame, text="Scissors", width=10, command=lambda: decide_winner("Scissors"))
scissors_button.grid(row=0, column=2, padx=5)

# Label to display result
result_label = tk.Label(window, text="", font=('Helvetica', 12), bg="light green")
result_label.pack(pady=10)

# Label to display outcome
outcome_label = tk.Label(window, text="", font=('Helvetica', 14, 'bold'), bg="light green")
outcome_label.pack(pady=10)

# Score label
score_label = tk.Label(window, text=f"User: {user_score} | Computer: {computer_score}", font=('Helvetica', 12), bg="light green")
score_label.pack(pady=10)

# Play Again button
reset_button = tk.Button(window, text="Reset Game", command=reset_game)
reset_button.pack(pady=10)

# Run the main loop
window.mainloop()