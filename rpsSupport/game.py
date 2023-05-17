import random

choices = {
    "rock": {"beats": "scissors", "loses_to": "paper"},
    "paper": {"beats": "rock", "loses_to": "scissors"},
    "scissors": {"beats": "paper", "loses_to": "rock"}
}


def get_computer_choice(my_choice):
    computer_choice = random.choice(list(choices.keys()))
    return computer_choice


def get_player_choice():
    return input("Enter your choice (rock, paper, or scissors): ").lower()


def play_round():
    print("Welcome to Rock, Paper, Scissors!")

    player_choice = get_player_choice()
    computer_choice = get_computer_choice(player_choice)

    print("You chose", player_choice)
    print("The computer chose", computer_choice)

    if player_choice == computer_choice:
        print("Tie!")
    elif choices[player_choice]["beats"] == computer_choice:
        print("You win!")
    else:
        print("You lose!")

        # Display the choices and the winner
    print(f"You chose {player_choice}, and the computer chose {computer_choice}.")

