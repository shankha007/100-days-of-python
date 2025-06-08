from art import logo
import random

def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)
    return random_card

def calculate_score(cards):
    """Take a list of cards and returns the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def blackjack():
    """Play a game of Blackjack with computer"""
    print(logo)

    human_cards = []
    human_total = -1

    computer_cards = []
    computer_total = -1

    is_game_over = False

    for _ in range(2):
        human_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        human_total = calculate_score(human_cards)
        computer_total = calculate_score(computer_cards)

        print(f"Your cards: {human_cards}, current score: {human_total}")
        print(f"Computer's first card: {computer_cards[0]}")

        if human_total == 0 or computer_total == 0 or human_total > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                human_cards.append(deal_card())
            else:
                is_game_over = True

    def compare(human_score, computer_score):
        if human_score == computer_score:
            return "Draw"
        elif computer_score == 0:
            return "You Lose. Opponent has Blackjack."
        elif human_score == 0:
            return "You Win. You have Blackjack."
        elif human_score > 21:
            return "You Lose. You went over."
        elif computer_score > 21:
            return "You Won. Computer went over."
        elif human_score > computer_score:
            return "You Won."
        else:
            return "You Lose."

    while computer_total != 0 and computer_total < 17:
        computer_cards.append(deal_card())
        computer_total = calculate_score(computer_cards)

    print(f"Your final hand: {human_cards}, final score: {human_total}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_total}")

    print(compare(human_total, computer_total))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
    print("\n" * 20)
    blackjack()