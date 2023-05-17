import rpsSupport

if __name__=='__main__':
    num_games = input('Enter number of games to play: ')
    for i in range(num_games):
        outcome = play_game()
        if outcome == 'P':
            print('Player wins')
        elif outcome == 'C':
            print('Computer wins')
        else:
            print('Tie')
