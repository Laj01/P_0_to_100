import random

def main():
    user_hand = []
    computer_hand = []
    is_game_over = False

    for _ in range(2):
        user_hand.append(deal_card())
        computer_hand.append(deal_card())

    while not is_game_over:    
        user_score = calculate_score(user_hand)
        computer_score = calculate_score(computer_hand)
        print(f'Your hand: {user_hand}\nTotal: {user_score}\nBank hand: {computer_hand[0]}[]\n')

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_next_move = input('Type "d" to draw one more card, type "p" to pass: ')
            if user_next_move == 'd':
                user_hand.append(deal_card())
                user_score = calculate_score(user_hand)
                print(compare_scores(user_score=user_score, computer_score=computer_score))
            else:
                print(compare_scores(user_score=user_score, computer_score=computer_score))
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_hand.append(deal_card())
        computer_score = calculate_score(computer_hand)
        

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare_scores(user_score, computer_score):
    if user_score == computer_score:
        return 'DRAW'
    elif computer_score == 0:
        return 'You lose, bank has a BlackJack!'
    elif user_score == 0:
        return 'You win, you have a BlackJack!'
    elif user_score > 21:
        return 'You lose, you went over!'
    elif computer_score > 21:
        return 'You win, bank went over!'
    elif user_score > computer_score:
        return 'You win!'
    else:
        return 'You lose!'
    

if __name__ == '__main__':
    main()