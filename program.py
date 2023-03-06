import random
from art import logo,vs
from data import data



def geting_info(account):
    name = account['name']
    description = account['description']
    country = account['country']
    return f" {name} a {description} from {country}"

account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b:
    account_b = random.choice(data)

end_game = False
score = 0
while not end_game:
    print(logo)
    print(f" Compare A: {geting_info(account_a)}")
    print(vs)
    print(f" Against B: {geting_info(account_b)}")
    user_input = input("Who has more followers? Type 'A' or 'B': ").upper()
    if user_input == 'A' and account_a['follower_count'] > account_b['follower_count']:
        score += 1
        print(f"You're right! Current score: {score}")
        account_a = account_a
        account_b = random.choice(data)
    elif user_input == 'B' and account_a['follower_count'] < account_b['follower_count']:
        score += 1
        print(f"You're right! Current score: {score}")
        account_b = account_b
        account_a = random.choice(data)
    else:
        end_game = True
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")
