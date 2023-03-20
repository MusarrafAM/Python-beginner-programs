#Number Guessing Game Objectives :

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
# from art import logo

times = 5 
guess = 0
print("""

   _____                       _______ _            _   _                 _                  ____  __               __  
  / ____|                     |__   __| |          | \ | |               | |                / /  \/  |              \ \ 
 | |  __ _   _  ___  ___ ___     | |  | |__   ___  |  \| |_   _ _ __ ___ | |__   ___ _ __  | || \  / |_   _ ___  __ _| |
 | | |_ | | | |/ _ \/ __/ __|    | |  | '_ \ / _ \ | . ` | | | | '_ ` _ \| '_ \ / _ \ '__| | || |\/| | | | / __|/ _` | |
 | |__| | |_| |  __/\__ \__ \    | |  | | | |  __/ | |\  | |_| | | | | | | |_) |  __/ |    | || |  | | |_| \__ \ (_| | |
  \_____|\__,_|\___||___/___/    |_|  |_| |_|\___| |_| \_|\__,_|_| |_| |_|_.__/ \___|_|    | ||_|  |_|\__,_|___/\__,_| |
                                                                                            \_\                     /_/ 
                                                                                                                        

""")

print("Welcome to Musa's Number guessing game!\nI'm thinking of a number between 1 and 100.")
difficulty = input("Choos a difficulty type 'easy' or 'hard': ")


if difficulty == "easy":
    times = 10
elif difficulty == "hard":
    times = 5

number = random.randint(1,100)
answer_correct = False
while not answer_correct:
    if times != 0:
        print(f"You have {times} attempts remaining to guess the number.")
        
        times -= 1
        
        guess = int(input("Make a guess: "))
        if number == guess:
            print(f"You Got it the answer was {number}")
            answer_correct = True
        elif number > guess:
            print("Too low\nGuess again.")
            answer_correct = False
        elif number < guess:
            print("Too high\nGuess again.")
            answer_correct = False
    else:
        print(f"You've run out of guesses, you lose. The number was {number}")
        answer_correct = True












