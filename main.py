# Number guessing game

# import random module
import random
# create a function to pass hint when the users guess is wrong


def hint(a, b):
    """ give a hint whether number is closer or further"""
    if a > b:
        if (a - b) >= 10:
            print("You are far away too up, guess lower")
        if (a - b) < 10:
            print("Nice we are close!")
    else:
        if (b - a) >= 10:
            print("You are far away too down, guess higher")
        if (b - a) < 10:
            print("GOOD! Your guess is close!")


difficulty = {
    'hard': 10,
    'easy': 5
}

should_continue = True

while should_continue:
    count = 0
    level = input("Choose difficulty? hard or easy  ")
    generated_number = random.randint(1, 101)
    # print(generated_number)
    for _ in range(difficulty[level]):
        count += 1
        user_guess = int(input("Guess: "))
        if user_guess == generated_number:
            print("WAY TO GO YOU WIN !!!!")
            choice = input("would you like to play again?").lower()
            if choice == "no":
                should_continue = False
        else:
            print(f"You have {difficulty[level] -count} chances left")
            if count != difficulty[level]:
                hint(user_guess, generated_number)
                print("Try Again")
            else:
                print("Oops you run out of choicese")
                print(generated_number)
                choice = input("would you like to play again?").lower()
                if choice == "no":
                    should_continue = False