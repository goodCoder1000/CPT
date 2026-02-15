import random
import time

# function that slowly types out messages (i used this in my prev. game :D )
def type_out(text, delay=0.3):
    typed = ""
    for char in text:
        typed += char
        print("\n\n\n\n\n\n\n", typed)
        time.sleep(delay)
print("\n")

# possible letters for the game
characters = ["A", "B", "C", "D"]

sequence = []
round_number = 1

type_out("Welcome to the Simon Memory Game!", delay=0.075)
time.sleep(1)
type_out("Watch the sequence and repeat it.", delay=0.075)
time.sleep(1)
print("Game starting...\n")

while True:
    print(f"Round {round_number}")
    
    # add a new random letter to the sequence
    sequence.append(random.choice(characters))
    
    # show the sequence one character at a time
    for i in sequence:
        print(i)
        time.sleep(1)  # pause so player can see it
        print("\n\n\n\n\n\n")  # clears the screen
    
    # input
    user_input = input("Enter the sequence (no spaces): ")
    user_input = user_input.upper()
    
    # build the correct sequence string
    correct_sequence = ""
    for letter in sequence:
        correct_sequence += letter
    
    # Check if correct
    if user_input == correct_sequence:
        print("Correct!\n")
        round_number += 1
        time.sleep(1)
    else:
        print("Wrong!")
        print("The correct sequence was:", correct_sequence)
        print("You reached Round", round_number)
        break
