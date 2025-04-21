""""
# This code is a simple rock-paper-scissors game where the player plays against the computer.
# The player inputs their choice, and the computer randomly selects its choice.
# The game then determines the winner based on the rules of rock-paper-scissors.
"""

import random

def show_banner():
    print("\n" + "="*40)
    print("🎮 Welcome to Rock - Paper - Scissors! 🎮")
    print("="*40)
    print("💻 VS 🧠 Let’s see who wins!\n")

def get_choices():
  player_choice = input("Enter your choice (rock,paper,scissors):")
  options = ["rock", "paper", "scissors"]
  computer_choice = random.choice(options)
  choices = {"player": player_choice, "computer": computer_choice}
  return choices

def get_win(player, computer):
  print(f"You chose {player}, computer chose {computer}")
  if player == computer:
    return "It's a tie!"
  elif player == "rock":
    if computer == "scissors":
      return "Rock smashes scissors! You win!"
    else:
      return "Paper cover rock! You lose!"
  elif player == "paper":
    if computer == "rock":
      return "Paper cover rock! You win!"
    else:
      return "Scissors cuts paper! You lose!"
  elif player == "scissors":
    if computer == "paper":
      return "Scissors cuts paper! You win!"
    else:
      return "Rock smashes scissors! You lose!"


# Run the game
show_banner()
choices = get_choices()
result = get_win(choices["player"], choices["computer"])
print(result)

#