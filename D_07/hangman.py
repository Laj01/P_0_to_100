import random
import os
from hangman_words import word_list
from hangman_art import stages


def main():
    clear = lambda: os.system('cls')
    chosen_word = random.choice(word_list)
    end_of_game = False
    user_lives = 6
    word_len = len(chosen_word)
    hidden_word = []

    for _ in range(word_len):
        hidden_word += '_'

    while not end_of_game:
        user_input = input('Guess a letter. ').lower()
        clear()
        if user_input in hidden_word:
            print(f'You have already guessed the letter "{user_input}"!')
        for pos in range(word_len):
            letter = chosen_word[pos]
            if letter == user_input:
                hidden_word[pos] = letter
        if user_input not in chosen_word:
            print(f'Your guess "{user_input}" is not in the word. You lost 1 life.')
            user_lives -= 1
            if user_lives == 0:
                end_of_game = True
                print(f'You lose. The correct word was: {chosen_word}')
        print(f'{" ".join(hidden_word)}')
        if '_' not in hidden_word:
            end_of_game = True
            print('You win. Well done.')
        print(stages[user_lives])


if __name__ == '__main__':
    main()