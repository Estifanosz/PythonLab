import random

# Initialize variables to keep track of wins, losses, and draws
wins = 0
losses = 0
draws = 0

# Main game loop
while True:
    # Get user's choice
    user_choice = input("Choose rock, paper, or scissors: ")

    # Get computer's choice
    computer_choice = random.choice(["rock", "paper", "scissors"])

    # Compare choices and determine winner
    if user_choice == computer_choice:
        result = "draw"
        draws += 1
    elif user_choice == "rock" and computer_choice == "scissors":
        result = "win"
        wins += 1
    elif user_choice == "paper" and computer_choice == "rock":
        result = "win"
        wins += 1
    elif user_choice == "scissors" and computer_choice == "paper":
        result = "win"
        wins += 1
    else:
        result = "lose"
        losses += 1

    # Print the result and statistics
    print("You chose  {} and the computer chose {}. You {}.".format(
        user_choice, computer_choice, result))
    print("Wins: {} Losses: {} Draws: {}".format(wins, losses, draws))
