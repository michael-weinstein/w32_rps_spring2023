import random

choices = {
    "rock": {"beats": "scissors", "loses_to": "paper"},
    "paper": {"beats": "rock", "loses_to": "scissors"},
    "scissors": {"beats": "paper", "loses_to": "rock"}
}

beat_choices = {
    "rock": ["scissors"],
    "paper": ["rock"],
    "scissors": ["paper"]
}


def get_computer_choice():
    computer_choice = random.choice(list(beat_choices.keys()))
    return computer_choice


def get_player_choice():
    return input("Enter your choice (rock, paper, or scissors): ").lower()


def play_round():
    print("Welcome to Rock, Paper, Scissors!")

    player_choice = get_player_choice()
    computer_choice = get_computer_choice()

    print("You chose", player_choice)
    print("The computer chose", computer_choice)

    if player_choice == computer_choice:
        return "Tie!"
    elif computer_choice in beat_choices[player_choice]:
        return "You win!"
    else:
        return "Computer wins!"

