import random

num_a = 0
num_b = 0
answer = 0
choice = ""

def start_game():
    global choice
    start = input("Would you like to play a game? yes or no? -> ").lower()
    if start == "yes":
        chosen_game(start)    
    elif start == "no":
        print("Thanks for playing!")
        exit()
    else:
        print("Please choose a valid response")
        start_game()


def gen_ran_num():
    global num_a
    global num_b
    num_a = random.randint(0,10)
    num_b = random.randint(0,10)


def generate_answer(choice):
    global answer 
    if choice == "addition":
        answer = num_a + num_b
    elif choice == "subtraction":
        answer = max(num_a, num_b) - min(num_a, num_b)


def chosen_game(start):
    if start == "yes":
        choice = input("Subtraction or Addition? -> ").lower()
        if choice == "addition":
            gen_ran_num()
            generate_answer(choice)
            addition_problem()
        elif choice == "subtraction":
            gen_ran_num()
            generate_answer(choice)
            subtraction_problem()
        else:
            choice = input("Subtraction or Addition? -> ")


def addition_problem():
    user_input = int(input(f"{num_a} + {num_b} = "))
    if user_input == answer:
        print(f"You are correct! {num_a} + {num_b} equals {answer}! Great Job!")
        start = input("Would you like to play again? yes or no? -> ").lower()
        if start == "yes":
            chosen_game(start)
        else:
            print("Thanks for playing!")
            exit()
    else:
        print("Please try again")
        addition_problem()


def subtraction_problem():
    user_input = int(input(f"{max(num_a,num_b)} - {min(num_a,num_b)} = "))
    if user_input == answer:
        print(f"You are correct! {max(num_a, num_b)} - {min(num_a, num_b)} equals {answer}! Great Job!")
        start = input("Would you like to play again? yes or no? -> ").lower()
        if start == "yes":
            chosen_game(start)
        else:
            print("Thanks for playing!")
            exit()
    else:
        print("Please try again")
        subtraction_problem()


start_game()