# Task - 4 Rock-Paper-Scissors Game

import random

user_score = 0
computer_score = 0

while True:
    print("\nRock, Paper, Scissors Game")
    print("Enter your choice: rock, paper, or scissors")
    
    user_choice = input("Your choice: ").strip().lower()
    if user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice! Please enter rock, paper, or scissors.")
        continue
    
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    print(f"Computer chose: {computer_choice}")
    
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        print("You win!")
        user_score += 1
    else:
        print("You lose!")
        computer_score += 1
    
    print(f"Scores: You - {user_score}, Computer - {computer_score}")
    
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != 'yes':
        print("Thanks for playing! Goodbye!")
        break