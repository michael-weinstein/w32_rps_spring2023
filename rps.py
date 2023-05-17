#!/usr/bin/env python3
import random
import sys
from typing import List

winner_dict = {
    'rock' : ['paper'],
    'scissors' : ['rock'],
    'paper' : ['scissors']
}
objects = list(winner_dict.keys())

def get_cpu_throw(objects: List[str]) -> str:
    throw = random.randint(0,len(objects) - 1)
    return(objects[throw])

def get_player_throw(objects: List[str]) -> str:
    throw = input('Enter Throw: ').lower()
    if throw in objects:
        return(throw)
    else:
        if throw in ['quit', 'restart']:
            return(throw)
        else:
            print('Please enter valid object: ' + str(objects))
            return None

def get_winner(player_throw: str, cpu_throw: str) -> str:
    if cpu_throw == player_throw:
        return('Tie') 
    elif player_throw in winner_dict[cpu_throw]:
        return('Player')
    else:
        return('CPU')

if __name__ == '__main__':
    player_wins = 0
    cpu_wins = 0
    ties = 0
    while True:
        cpu_throw = get_cpu_throw(objects)
        player_throw = get_player_throw(objects)
        print('CPU throw: ', cpu_throw)
        print('Player throw: ', player_throw)
        if player_throw == 'quit':
            break
        if player_throw == 'restart':
            ties = 0
            cpu_wins = 0
            player_wins = 0
        winner = get_winner(player_throw, cpu_throw)
        if(winner == 'Tie'):
            print('TIE')
            ties += 1
        elif(winner == 'Player'):
            print('PLAYER WINS')
            player_wins += 1
        else:
            print('CPU WINS')
            cpu_wins += 1
        
    print('Total wins: CPU: %d PLAYER: %d TIE: %d'%(cpu_wins, player_wins, ties))
