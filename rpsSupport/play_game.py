
import random

rule_dict = {'rock':['scissors'],
           'paper':['rock'],
           'scissors':['paper']}


def play_game(player_throw:str, computer_throw:str, rule_dict:dict) -> str:
    player_throw = player_throw.lower()
    if player_throw not in rule_dict.keys():
        return('')
    if computer_throw in rule_dict[player_throw]:
        return('P')
    elif player_throw in rule_dict[computer_throw]:
        return('C')
    else:
        return('T')