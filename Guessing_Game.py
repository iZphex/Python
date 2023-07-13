from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(guess, answer):
    if guess > answer:
        print("Too high!")
    elif guess < answer:
        print("Too low!")
    else:
        print("You got it!")


def set_difficulty():
    level = input("Choose a difficulty (easy/hard): ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print("Welcome to the guessing game!")
    print("I am thinking of a number between 1 and 100.")
    answer = randint(1, 100)

    turns = set_difficulty()
    print(f"You have {turns} turns to guess the number.")

    guess = 0
    while guess != guess:
        guess = int(input("Make a guess: "))
        check_answer(guess, answer)


game()
