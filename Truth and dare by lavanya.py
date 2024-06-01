'''import random
import tkinter as tk
from tkinter import simpledialog, messagebox

# Initial scores and game counters
PLAYER_SCORE = 0
player = 0
count_game = 0

# Define the options for different levels
easy_options = 5
medium_options = 10
hard_options = 20

# Truth and dare lists
truths = [
    "Have you ever cheated in a game?",
    "What is your biggest fear?",
    "What is your most embarrassing moment?",
    "Have you ever lied to get out of trouble?",
    "What is your secret talent?",
    "Express your love for your love by a poem",
    "What's the craziest thing you've done on a dare?",
    "Who is your secret crush?",
    "What is the worst lie you’ve ever told?",
    "What’s something you’re glad your family doesn’t know about you?",
    "Have you ever been caught lying?",
    "What is your most guilty pleasure?",
    "What is the most childish thing you still do?",
    "What's the biggest mistake you've ever made?",
    "Have you ever stolen anything?",
    "What’s the most embarrassing thing you’ve posted on social media?",
    "Have you ever peed in a pool?",
    "What’s the most awkward date you’ve been on?",
    "What’s your biggest insecurity?",
    "Have you ever broken the law?"
]

dares = [
    "Do 10 push-ups.",
    "Sing a song out loud.",
    "Call a friend and tell them a joke.",
    "Dance for 30 seconds.",
    "Act like a chicken for a minute.",
    "Call your crush and expose your feelings",
    "Call your ex and say, 'Will you marry me?'",
    "Mimic your favorite teacher for one minute",
    "Run around the outside of the house three times.",
    "Let the person to your left draw on your face with a pen.",
    "Try to lick your elbow.",
    "Do your best impression of a baby being born.",
    "Do a dance from TikTok.",
    "Let someone in the group give you a new hairstyle.",
    "Eat a spoonful of mustard.",
    "Talk in an accent for the next 3 rounds.",
    "Do your best chicken dance outside on the lawn.",
    "Imitate a celebrity every time you talk for the next 3 minutes.",
    "Try to juggle 3 items (don't break anything!).",
    "Do 20 jumping jacks."
]

# Function to select truth or dare based on level
nd}\n\nScore Board\n{name.title()}: {PLAYER_SCORE}")
        
        level = simpledialog.askstring("Input", "Choose a level - Easy, Medium, or Hard:").lower()
        if level not in ["easy", "medium", "hard"]:
            messagebox.showwarning("Input Error", "Invalid level. Please choose Easy, Medium, or Hard.")
            continue
        
        truth, dare = truth_or_dare(level)
        if truth and dare:
            messagebox.showinfo("Truth or Dare", f"Truth: {truth}\nDare: {dare}")
        else:
            messagebox.showwarning("Input Error", "An error occurred while selecting truth or dare. Please try again.")
    
    messagebox.showinfo("Game Over", "Game over! Thanks for playing.")

# Create the main window
root = tk.Tk()
root.title("Truth or Dare Game")

# Create and place the start button
start_button = tk.Button(root, text="Start Game", command=start_game)
start_button.pack(pady=20)

# Run the application
root.mainloop()
import random
import tkinter as tk
from tkinter import simpledialog, messagebox

# Initial scores and game counters
PLAYER_SCORE = 0
player = 0
count_game = 0

# Define the options for different levels
easy_options = 5
medium_options = 10
hard_options = 20

# Truth and dare lists
truths = [
    "Have you ever cheated in a game?",
    "What is your biggest fear?",
    "What is your most embarrassing moment?",
    "Have you ever lied to get out of trouble?",
    "What is your secret talent?",
    "Express your love for your love by a poem",
    "What's the craziest thing you've done on a dare?",
    "Who is your secret crush?",
    "What is the worst lie you’ve ever told?",
    "What’s something you’re glad your family doesn’t know about you?",
    "Have you ever been caught lying?",
    "What is your most guilty pleasure?",
    "What is the most childish thing you still do?",
    "What's the biggest mistake you've ever made?",
    "Have you ever stolen anything?",
    "What’s the most embarrassing thing you’ve posted on social media?",
    "Have you ever peed in a pool?",
    "What’s the most awkward date you’ve been on?",
    "What’s your biggest insecurity?",
    "Have you ever broken the law?"
]

dares = [
    "Do 10 push-ups.",
    "Sing a song out loud.",
    "Call a friend and tell them a joke.",
    "Dance for 30 seconds.",
    "Act like a chicken for a minute.",
    "Call your crush and expose your feelings",
    "Call your ex and say, 'Will you marry me?'",
    "Mimic your favorite teacher for one minute",
    "Run around the outside of the house three times.",
    "Let the person to your left draw on your face with a pen.",
    "Try to lick your elbow.",
    "Do your best impression of a baby being born.",
    "Do a dance from TikTok.",
    "Let someone in the group give you a new hairstyle.",
    "Eat a spoonful of mustard.",
    "Talk in an accent for the next 3 rounds.",
    "Do your best chicken dance outside on the lawn.",
    "Imitate a celebrity every time you talk for the next 3 minutes.",
    "Try to juggle 3 items (don't break anything!).",
    "Do 20 jumping jacks."
]

# Function to select truth or dare based on level
def truth_or_dare(level):
    if level == "easy":
        truth = random.choice(truths[:easy_options])
        dare = random.choice(dares[:easy_options])
    elif level == "medium":
        truth = random.choice(truths[:medium_options])
        dare = random.choice(dares[:medium_options])
    elif level == "hard":
        truth = random.choice(truths[:hard_options])
        dare = random.choice(dares[:hard_options])
    else:
        return None, None  # Returning None if invalid level

    return truth, dare

# Function to start the game
def start_game():
    global count_game
    global PLAYER_SCORE
    
    name = simpledialog.askstring("Input", "Enter your name:")
    if not name:
        messagebox.showwarning("Input Error", "Please enter your name to start the game.")
        return

    # Password prompt
    password = simpledialog.askstring("Password", "Enter the password:")
    if password != "1234":
        messagebox.showwarning("Authentication Error", "Incorrect password. Access denied.")
        return

    rounds_to_play = simpledialog.askinteger("Rounds to Play", "How many rounds do you want to play?")
    if rounds_to_play is None or rounds_to_play <= 0:
        messagebox.showwarning("Input Error", "Please enter a valid number of rounds.")
        return

    messagebox.showinfo("Authentication Success", "Password accepted. Let's start the game!")

    while count_game < rounds_to_play:
        count_game += 1
        messagebox.showinfo("Game Round", f"Round {count_game}\n\nScore Board\n{name.title()}: {PLAYER_SCORE}")

        level = simpledialog.askstring("Input", "Choose a level - Easy, Medium, or Hard:").lower()
        if level not in ["easy", "medium", "hard"]:
            messagebox.showwarning("Input Error", "Invalid level. Please choose Easy, Medium, or Hard.")
            continue
        
        truth, dare = truth_or_dare(level)
        if truth and dare:
            messagebox.showinfo("Truth or Dare", f"Truth: {truth}\nDare: {dare}")
        else:
            messagebox.showwarning("Input Error", "An error occurred while selecting truth or dare. Please try again.")
    
    messagebox.showinfo("Game Over", "Game over! Thanks for playing.")

# Create the main window
root = tk.Tk()
root.title("Truth or Dare Game")

# Create and place the start button
start_button = tk.Button(root, text="Start Game", command=start_game)
start_button.pack(pady=20)

# Run the application
root.mainloop()'''
import random
import tkinter as tk
from tkinter import simpledialog, messagebox
import winsound  # Import the winsound module for playing sounds

# Initial scores and game counters
PLAYER_SCORE = 0
player = 0
count_game = 0

# Define the options for different levels
easy_options = 5
medium_options = 10
hard_options = 20

# Truth and dare lists
truths = [
    "Have you ever cheated in a game?",
    "What is your biggest fear?",
    "What is your most embarrassing moment?",
    "Have you ever lied to get out of trouble?",
    "What is your secret talent?",
    "Express your love for your love by a poem",
    "What's the craziest thing you've done on a dare?",
    "Who is your secret crush?",
    "What is the worst lie you’ve ever told?",
    "What’s something you’re glad your family doesn’t know about you?",
    "Have you ever been caught lying?",
    "What is your most guilty pleasure?",
    "What is the most childish thing you still do?",
    "What's the biggest mistake you've ever made?",
    "Have you ever stolen anything?",
    "What’s the most embarrassing thing you’ve posted on social media?",
    "Have you ever peed in a pool?",
    "What’s the most awkward date you’ve been on?",
    "What’s your biggest insecurity?",
    "Have you ever broken the law?"
]

dares = [
    "Do 10 push-ups.",
    "Sing a song out loud.",
    "Call a friend and tell them a joke.",
    "Dance for 30 seconds.",
    "Act like a chicken for a minute.",
    "Call your crush and expose your feelings",
    "Call your ex and say, 'Will you marry me?'",
    "Mimic your favorite teacher for one minute",
    "Run around the outside of the house three times.",
    "Let the person to your left draw on your face with a pen.",
    "Try to lick your elbow.",
    "Do your best impression of a baby being born.",
    "Do a dance from TikTok.",
    "Let someone in the group give you a new hairstyle.",
    "Eat a spoonful of mustard.",
    "Talk in an accent for the next 3 rounds.",
    "Do your best chicken dance outside on the lawn.",
    "Imitate a celebrity every time you talk for the next 3 minutes.",
    "Try to juggle 3 items (don't break anything!).",
    "Do 20 jumping jacks."
]

# Function to select truth or dare based on level
def truth_or_dare(level):
    if level == "easy":
        truth = random.choice(truths[:easy_options])
        dare = random.choice(dares[:easy_options])
    elif level == "medium":
        truth = random.choice(truths[:medium_options])
        dare = random.choice(dares[:medium_options])
    elif level == "hard":
        truth = random.choice(truths[:hard_options])
        dare = random.choice(dares[:hard_options])
    else:
        return None, None  # Returning None if invalid level

    return truth, dare

# Function to start the game3
def start_game():
    global count_game
    global PLAYER_SCORE
    
    # Play welcome sound3
    winsound.PlaySound('welcome_to_the_game.wav', winsound.SND_FILENAME)
    winsound.Beep(1000, 1000)  # 9Beep at 1000 Hz for 1 second
    
# Example usage of PlaySound function (playing a WAV file)


    name = simpledialog.askstring("Input", "Enter your name:")
    if not name:
        messagebox.showwarning("Input Error", "Please enter your name to start the game.")
        return

    # Password prompt
    password = simpledialog.askstring("Password", "Enter the password:")
    if password != "1234":
        messagebox.showwarning("Authentication Error", "Incorrect password. Access denied.")
        return

    rounds_to_play = simpledialog.askinteger("Rounds to Play", "How many rounds do you want to play?")
    if rounds_to_play is None or rounds_to_play <= 0:
        messagebox.showwarning("Input Error", "Please enter a valid number of rounds.")
        return

    messagebox.showinfo("Authentication Success", "Password accepted. Let's start the game!")

    while count_game < rounds_to_play:
        count_game += 1
        messagebox.showinfo("Game Round", f"Round {count_game}\n\nScore Board\n{name.title()}: {PLAYER_SCORE}")

        level = simpledialog.askstring("Input", "Choose a level - Easy, Medium, or Hard:").lower()
        if level not in ["easy", "medium", "hard"]:
            messagebox.showwarning("Input Error", "Invalid level. Please choose Easy, Medium, or Hard.")
            continue
        
        truth, dare = truth_or_dare(level)
        if truth and dare:
            messagebox.showinfo("Truth or Dare", f"Truth: {truth}\nDare: {dare}")
        else:
            messagebox.showwarning("Input Error", "An error occurred while selecting truth or dare. Please try again.")
    
    messagebox.showinfo("Game Over", "Game over! Thanks for playing.")

# Create the main window
root = tk.Tk()
root.title("Truth or Dare Game")

# Create and place the start button
start_button = tk.Button(root, text="Start Game", command=start_game)
start_button.pack(pady=20)

# Run the application
root.mainloop()
