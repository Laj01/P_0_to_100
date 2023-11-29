import random


EASY = 10
HARD = 5

def main():
    hidden_number = pick_number()
    lives = set_difficulty()
    player_guess(lives, hidden_number)

def pick_number():
    return random.randint(1, 100)

def set_difficulty():
    setting = input('Welcome to the number guessing game!\nI\'m thinking of a number between 1 and 100.\nChoose a difficulty. Type \'easy\' or \'hard\': ').lower()
    if setting == 'easy':
        return EASY
    else:
        return HARD

def player_guess(life, number):
    guess = int(input(f'You have {life} attempts remaining to guess a number.\nMake  guess: '))
    while life > 1:
        if guess < number:
            life -= 1
            print('Too low.\nGuess again.')
            guess = int(input(f'You have {life} attempts remaining to guess a number.\nMake  guess: '))
        elif guess > number:
            life -= 1
            print('Too high.\nGuess again.')
            guess = int(input(f'You have {life} attempts remaining to guess a number.\nMake  guess: '))
        else:
            print(f'You got it! The answer was {number}.')
            break
    if life == 1:
        print('You run out of guesses. You lose.')


if __name__ == '__main__':
    main()