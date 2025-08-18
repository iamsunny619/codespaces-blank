from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

def get_user_choice():
    try:
        user_input = int(input("Enter your choice (1 for Rock, 2 for Paper, 3 for Scissors): "))
        if user_input in [item.value for item in RPS]:
            print(f"You selected: {RPS(user_input).name}")
        else:
            print("Input not in range. Please enter a number between 1 and 3.")
    except ValueError:
        print("Invalid input. Please enter a number.")

get_user_choice()
