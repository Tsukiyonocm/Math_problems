import random

num_a = random.randint(0,10)
num_b = random.randint(0,10)
answer = num_a + num_b


def start_game():
    start = input("Would you like to play a game? yes or no? -> ").lower()
    if start == "yes":
        addition_problem()
    elif start == "no":
        exit()
    else:
        print("Please choose a valid response")
        start_game()



def addition_problem():
    user_input = int(input(f"{num_a} + {num_b} = "))
    if user_input == answer:
        print(f"You are correct! {num_a} + {num_b} equals {answer}! Great Job!")
    else:
        print("Please try again")
        addition_problem()

start_game()