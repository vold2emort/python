import random
from art import logo, vs
from game_data import data
# Display art
print(logo)
# Generate a random account from the game data
# Format the account data into printable format
# ask user for guess
# check if user is correct
# Get follower count of each account
# use if statement to check if user is correct
# give user feedback on their guess
# score tracking
# game repeatable position b to a


def account_info(a_dict):
    """Formats data of accounts"""
    return f"{a_dict['name']}, {a_dict['description']}, from {a_dict['country']}"


def check_answer(a_guess, a_follower, b_follower):
    """check and returns highest follower account"""
    if a_follower > b_follower:
        return a_guess == "a"
    # checks if a > b then a_guess==a returns true or false according to correct guess
    else:
        return a_guess == "b"


score = 0
should_continue = True
account_b = random.choice(data)

while should_continue:
    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A:{account_info(account_a)}")
    print(vs)
    print(f"Against B:{account_info(account_b)}")
    guess = input("Who has more followers 'A' or 'B': ").lower()
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    # clear
    if is_correct:
        print(f"You are right!")
        score += 1
        print(f"current score is {score}")
    else:
        print(f"That's  wrong!, Final score is {score}")
        should_continue = False

