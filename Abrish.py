import random

def play_rps():
  try:
    # Get user choice
    user_choice = input("Choose rock, paper, or scissors: ")
    if user_choice not in ["rock", "paper", "scissors"]:
     raise ValueError("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")



    # Get computer choice
    computer_choice = random.choice(["rock", "paper", "scissors"])

    # Compare choices and determine winner
    if user_choice == computer_choice:
        result = "draw"
    elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
        result = "user"
    else:
        result = "computer"

    # Print result
    print("You chose {} and the computer chose {}. The result is a {}.".format(user_choice, computer_choice, result))
    return result
  except ValueError as ve:
    print(ve)

user_wins = 0
computer_wins = 0
draws = 0
while True:
    result = play_rps()
    if result == "user":
        user_wins += 1
    elif result == "computer":
        computer_wins += 1
    else:
        draws += 1
    print("You:", user_wins, "Computer:", computer_wins, "Draws:", draws)
