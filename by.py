import random


def maximum(lists):
    total1 = 0
    total = 0
    for items in lists:
        if items in above_10:
            value = above_10[items]
            total1 += value
        else:
            total += items
        return total + total1


def winner():

    print(f"user_cards = {user_cards}")
    print(f"computer_cards = {computer_cards}")
    user_cards_total = maximum(user_cards)
    computer_cards_total = maximum(computer_cards)

    if (user_cards_total >= 21) and (user_cards_total > computer_cards_total):
        print("computer wins")
        print("user went over")
    elif (computer_cards_total >= 21) and (computer_cards_total > user_cards_total):
        print("user wins")
        print("computer went over")
    elif (user_cards_total < 21) and (computer_cards_total < 21):
        if computer_cards_total > user_cards_total:
            print("computer wins")
        else:
            print("user wins")
    elif user_cards_total == computer_cards_total:
        print("Draw")
    elif (user_cards_total > 21) and (computer_cards_total > 21):
        print("both went over")


above_10 = {
    'king': 10,
    'queen': 10,
    'joker': 10
}
user_cards = []
computer_cards = []

randoms = [2, 3, 4, 5, 6, 7, 8, 9, random.choice(list(above_10))]

will_play = True
will_continue = True

while will_play:
    choice = input("Do you want to play black jack? 'Y' for yes and 'N'  for no").lower()
    if choice == 'y':
        user_cards.append(random.choice(randoms))
        computer_cards.append(random.choice(randoms))
        print(f"user_cards = {user_cards}")
        print(f"computer_cards = {computer_cards}")
        while will_continue:
            choice1 = input("Do you want to add another card? 'Y' for yes and 'N' for no").lower()
            if choice1 == 'y':
                user_cards.append(random.choice(randoms))
                computer_cards.append(random.choice(randoms))
                print(f"user_cards = {user_cards}")
                print(f"computer_cards = {computer_cards}")
                if (maximum(user_cards)) or (maximum(computer_cards)) > 21:

                    winner()
                    will_continue = False

            elif choice1 == 'n':

                winner()
                will_continue = False

        will_continue = True
    else:
        will_play = False
