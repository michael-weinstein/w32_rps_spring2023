
import random

def determine_winner(player_throw:str, computer_throw:str, rule_dict:dict) -> str:
    player_throw = player_throw.lower()
    if player_throw not in rule_dict.keys():
        return('')
    if computer_throw in rule_dict[player_throw]:
        return('P')
    elif player_throw in rule_dict[computer_throw]:
        return('C')
    else:
        return('T')

def play_game() -> str:
    rule_dict = {'rock': ['scissors'],
                 'paper': ['rock'],
                 'scissors': ['paper']}
    player_throw = input('rock, paper, or scissors?: ')
    computer_throw = random.choice(list(rule_dict.keys()))
    print('computer: ' + computer_throw)
    outcome = determine_winner(player_throw, computer_throw, rule_dict)
    return(outcome)
