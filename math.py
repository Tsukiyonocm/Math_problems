import random 
num_a = random.randint(0,10)
num_b = random.randint(0,10)
answer = num_a + num_b



def math_problem():
    user_input = int(input(f"{num_a} + {num_b} = "))
    if user_input == answer:
        print(f"You are correct! {num_a} + {num_b} equals {answer}! Great Job!")
    else:
        print("Please try again")
        math_problem()

math_problem()