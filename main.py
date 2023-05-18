import rpsSupport


def playARound():
    outcome = rpsSupport.play_game.play_game()
    if outcome == 'P':
        print('Player wins')
    elif outcome == 'C':
        print('Computer wins')
    elif outcome == 'T':
        print('Tie')
    else:
        print('Player Throw Invalid')


if __name__=='__main__':
    num_games = int(input('Enter number of games to play: '))
    for i in range(num_games):
        playARound()

            