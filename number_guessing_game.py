#Number Guessing Game – User vs random number
import random

def number_guessing_game():
    print("🎲 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100...")
    
    number_to_guess = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            user_guess = int(input("🔢 Enter your guess: "))
            attempts += 1
            
            if user_guess < number_to_guess:
                print("📉 Too low. Try again!")
            elif user_guess > number_to_guess:
                print("📈 Too high. Try again!")
            else:
                print(f"🎉 Correct! The number was {number_to_guess}.")
                print(f"🏆 You guessed it in {attempts} tries!")
                break
        except ValueError:
            print("❌ Please enter a valid number!")

# Run the game
number_guessing_game()
