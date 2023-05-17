
import random

rule_dict = {'rock':['scissors'],
           'paper':['rock'],
           'scissors':['paper']}


def play_game(player_throw:str, computer_throw:str, rule_dict:dict):
    if player_throw not in rule_dict.keys():
        print('Player Throw Invalid')
        return(None)
    if computer_throw not in rule_dict.keys():
        print('Computer Throw Invalid')
        return(None)
    if computer_throw in rule_dict[player_throw]:
        print('Player Wins')
        return('Player')
    elif player_throw in rule_dict[computer_throw]:
        print('Computer Wins')
        return('Computer')
    else:
        print('Tie')
        return(None)

if __name__=='__main__':
    while True:
        player_throw = input('rock, paper, or scissors?: ')
        computer_throw = random.choice(['rock', 'paper', 'scissors'])
        print('computer: ' + computer_throw)
        outcome = play_game(player_throw, computer_throw, rule_dict)
        if outcome:
            break

