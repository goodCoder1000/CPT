import random
import time

# Possible characters for the game
characters = ["A", "B", "C", "D"]

sequence = []
round_number = 1

print("Welcome to the Simon Memory Game!")
print("Watch the sequence and repeat it.")
print("Game starting...\n")

while True:
    print(f"Round {round_number}")
    
    # Add a new random character to the sequence
    sequence.append(random.choice(characters))
    
    # Show the sequence one character at a time
    for char in sequence:
        print(char)
        time.sleep(1)  # pause so player can see it
        print("\n\n\n\n\n\n")  # clears the screen (works in many terminals)
    
    # Ask player for input
    user_input = input("Enter the sequence (no spaces): ").upper()
    
    # Check if correct
    if user_input == "".join(sequence):
        print("Correct!\n")
        round_number += 1
        time.sleep(1)
    else:
        print("Wrong!")
        print("The correct sequence was:", "".join(sequence))
        print("You reached Round", round_number)
        break