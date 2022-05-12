import random

def guess(x): # x is the range limit, Guessing Game by the User and computer check input
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 to {x}: '))
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')
        else:
            print('Sorry, invalid input, please try again')
    print(f'Yay, Congratz! you guessed the number {random_number} ')


def computer_guess(x): #Guessing by the Computer - you need to chose number and answer if he is guess correct, low or high
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        else:
            print('Sorry, invalid input, please try again')

    print(f'Yay, The Computer guessed the number: {guess}, correctly!')


Game_mode = 'q'
Max_Range = 10

while Game_mode != 'e':
    Game_mode = input("Hello, Please chose a game mode, do you want to guess the number press U or the computer press C, to exit press E ?  ").lower()
    Max_Range = int(input("Please chose the limit: (1 to 9999999) "))
    if Game_mode == 'u':
        guess(Max_Range)
    elif Game_mode == 'c':
        computer_guess(Max_Range)
    else:
        print('Sorry, invalid input, please try again')
