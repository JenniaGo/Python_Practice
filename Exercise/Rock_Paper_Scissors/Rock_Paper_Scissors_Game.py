import random

def play():
    user = input("Choose 'r' for rock, 'p' for paper, 's' for scissors\n").lower()
    computer = random.choice(['r','p','s'])

    if user == computer:
        return 'Tie'

    # r > s, s > p, p > r
    if is_win(user,computer):
        return 'You won dear user!'

    return 'You Lost to the computer!'


def is_win(player, opponent):
    # return true if player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and  opponent == 'r'):
        return True

key = ''
while key != 'n':
    key = input("Hello, would you like to play? press 'Y' to start or 'N' to exit:  ").lower()
    if key == 'y':
        print(play())
    elif key == 'n':
        print('Game is over, thank you for playing, come back soon')
        continue
    else:
        print('Invalid input, please try again')
