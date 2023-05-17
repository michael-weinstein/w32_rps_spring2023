
import random

rule_dict = {'rock':['scissors'],
           'paper':['rock'],
           'scissors':['paper']}


while True:
    player_throw = input('rock, paper, or scissors?: ')
    computer_throw = random.choice(['rock','paper','scissors'])
    print('computer: '+computer_throw)
    if computer_throw in rule_dict[player_throw]:
        print('Player Wins')
        break
    elif player_throw in rule_dict[computer_throw]:
        print('Computer Wins')
        break
    else:
        print('Throw Again')

