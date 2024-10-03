import random

def roll_dice():
    
    print("Welcome to the Dice Roll Simulator!")
    
    while True:
        dice_roll = random.randint(1, 6)
        print(f"\nYou rolled a {dice_roll}!")

        roll_again = input("\nDo you want to roll the dice again? (yes/no): ").lower()

        if roll_again not in ['yes', 'y']:
            print("Thanks for playing! Goodbye!")
            break

roll_dice()
