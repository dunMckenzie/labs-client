# guess_number.py
# Programmer: Lorenzo Openito
# Date: 8/08/2024
# Description: A number guessing game where the user guesses a number between 1 and 10

import random

def main():
    """Main function to run the guessing game"""
    repeat = True
    
    while repeat:
        random_number = random.randint(1, 10)
        print(f"rand # is {random_number}")
        print("I'm thinking of a number between 1 and 10! Try to guess the number I'm thinking of:", end=" ")
        
        guessing = True
        while guessing:
            guess = int(input())
            
            if guess == random_number:
                print("That's it!", end=" ")
                again = input("Would you like to play again? (yes/no) ").lower()
                if again == 'no':
                    repeat = False
                    guessing = False
                elif again == 'yes':
                    print()
                    guessing = False
            elif guess > random_number:
                print("Too high! Guess again:", end=" ")
            elif guess < random_number:
                print("Too low! Guess again:", end=" ")
    
    print("Thank's for playing!")

# Call the main function to start the game
if __name__ == "__main__":
    main()
