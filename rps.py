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
    throw = input('Throw: ').lower()
    if throw in objects:
        return(throw)
    else:
        if throw in ['quit', 'restart']:
            return(throw)
        else:
            print('Please enter valid object: ' + str(objects))
            return None

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
        elif cpu_throw == player_throw:
            print('Tie') 
            ties += 1   
        elif player_throw in winner_dict[cpu_throw]:
            print('Player wins')
            player_wins += 1
        else:
            print('CPU wins')
            cpu_wins += 1
    print('Total wins: CPU: %d PLAYER: %d TIE: %d'%(cpu_wins, player_wins, ties))
