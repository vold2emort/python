from  random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
# number = list(range(1, 100)) not necessary


def check_answer(a_guess, a_answer, a_turn):
    if a_guess > a_answer:
        print("Too high")
        return a_turn - 1
    elif a_guess < a_answer:
        print("Too Low")
        return a_turn - 1
    else:
        print(f"You win!! The answer was {a_answer}")


def choose_difficulty():
    """chooses the difficulty level"""
    level = input("Choose a difficulty.Type 'easy' for easy or 'hard' for level: ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    elif level == "hard":
        return HARD_LEVEL_TURNS


def play_game():
    answer = randint(1, 100)
    print(answer)
    print(logo)
    print("WELCOME TO NUMBER GUESSING GAME!")
    print("I am thinking a number between 1 and 100")
    turns = choose_difficulty()
    user_guess = 0
    while answer != user_guess:
        print(f"You have {turns} attempts remaining")
        user_guess = int(input("Make a guess: "))
        turns = check_answer(user_guess, answer, turns)
        if turns == 0:
            print("you have ran out of guesses, You Loose!!")
            return
        elif answer != user_guess:
            print("Guess again.")


play_game()