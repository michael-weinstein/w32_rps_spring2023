
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

if __name__=='__main__':
    while True:
        player_throw = input('rock, paper, or scissors?: ')
        computer_throw = random.choice(list(rule_dict.keys()))
        print('computer: ' + computer_throw)
        outcome = play_game(player_throw, computer_throw, rule_dict)
        if outcome=='P':
            print('Player Wins')
            break
        elif outcome=='C':
            print('Computer Wins')
            break
        elif outcome=='T':
            print('Tie, Throw Again')
        else:
            print('Player Throw Invalid, Try Again')
