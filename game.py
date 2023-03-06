import random
from gamedata import data
from art import logo
from art import vs
print(logo)
score = 0
account_b = random.choice(data)
run_again = True
while run_again:
    def formated_data(account):
        """ contains the formated data """
        account_name = account["name"]
        account_description = account["description"]
        account_country = account["country"]
        return f"{account_name}, {account_description},from {account_country}"


    def check_answer(guesses, a_follower, b_follower):
        """take the user guess and follower counts and returns if the got it right"""
        if a_followers > b_followers:
            guess == "a"
            return True
        elif guess == "b":
            return True
        else:
            return False


    account_a = account_b

    while account_a == account_b:
        account_b = random.choice(data)

    print(f"compare A:{formated_data(account_a)}")
    print(vs)
    print(f"against B: {formated_data(account_b)}")
    guess = input(" who has more followers' type  A 'or 'B' for your choice\n").upper()
    a_followers = account_a["follower_count"]
    b_followers = account_b["follower_count"]
    is_correct = check_answer(guesses=guess, a_follower=a_followers, b_follower=b_followers)

    if is_correct:
        score += 1
        print(f"you are right! current score: {score} ")
    else:
        print(f"sorry that's wrong. final score {score} ")
        run_again = False

