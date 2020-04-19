import random

num_a = 0
num_b = 0
answer = 0

def gen_ran_num():
    global num_a
    global num_b
    global answer 
    num_a = random.randint(0,10)
    num_b = random.randint(0,10)
    answer = num_a + num_b

def start_game():
    start = input("Would you like to play a game? yes or no? -> ").lower()
    if start == "yes":
        addition_problem()
    elif start == "no":
        print("Thanks for playing!")
        exit()
    else:
        print("Please choose a valid response")
        start_game()


def addition_problem():
    user_input = int(input(f"{num_a} + {num_b} = "))
    if user_input == answer:
        print(f"You are correct! {num_a} + {num_b} equals {answer}! Great Job!")
        play_again = input("Would you like to play again? yes or no? -> ").lower()
        if play_again == "yes":
            gen_ran_num()
            addition_problem()
        else:
            print("Thanks for playing!")
            exit()
    else:
        print("Please try again")
        addition_problem()

start_game()