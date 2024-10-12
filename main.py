import tkinter as tk
import random

# List of possible moves
moves = ["Rock", "Paper", "Scissors"]

# Function to determine the winner
def determine_winner(user, computer):
    if user == computer:
        return "It's a Tie!"
    elif (user == "Rock" and computer == "Scissors") or \
         (user == "Paper" and computer == "Rock") or \
         (user == "Scissors" and computer == "Paper"):
        return "You Win!"
    else:
        return "You Lose!"

# Function to handle user move
def user_move(move):
    computer = random.choice(moves)
    user_choice_label.config(text=f"Your Choice: {move}")
    computer_choice_label.config(text=f"Computer's Choice: {computer}")
    result_label.config(text=determine_winner(move, computer))

# Function to reset the game
def reset_game():
    user_choice_label.config(text="Your Choice: None")
    computer_choice_label.config(text="Computer's Choice: None")
    result_label.config(text="")

# Create the main window
root = tk.Tk()
root.title("Rock Paper Scissors")

# Create and place labels
user_choice_label = tk.Label(root, text="Your Choice: None")
user_choice_label.pack(pady=5)

computer_choice_label = tk.Label(root, text="Computer's Choice: None")
computer_choice_label.pack(pady=5)

result_label = tk.Label(root, text="")
result_label.pack(pady=5)

# Create and place buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

rock_button = tk.Button(button_frame, text="Rock", command=lambda: user_move("Rock"))
rock_button.grid(row=0, column=0, padx=5)

paper_button = tk.Button(button_frame, text="Paper", command=lambda: user_move("Paper"))
paper_button.grid(row=0, column=1, padx=5)

scissors_button = tk.Button(button_frame, text="Scissors", command=lambda: user_move("Scissors"))
scissors_button.grid(row=0, column=2, padx=5)

# Create and place reset button
reset_button = tk.Button(root, text="Reset Game", command=reset_game)
reset_button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()

