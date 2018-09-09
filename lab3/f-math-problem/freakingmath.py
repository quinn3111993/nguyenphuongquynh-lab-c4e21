from random import *

def calculate(x,y,op):
    result = 0
    if op == '+':
        result = x+y
    elif op == '-':
        result = x-y
    elif op == '*':
        result = x*y
    elif op == '/':
        result = x/y
    return result

def generate_quiz():
    # Hint: Return [x, y, op, result]
    op_list = ['+', '-', '*', '/']
    op = choice(op_list)

    x_list = range(1,9)
    x = choice(x_list)
    y = choice(x_list)

    correct_z = calculate(x,y,op)
    result = correct_z + randint(-2,2)

    return [x, y, op, result]

def check_answer(x, y, op, result, user_choice):
    print(user_choice)
    if result == calculate(x,y,op):
        if user_choice:
            return True
        else:
            return False
    else:
        if user_choice:
            return False
        else:
            return True
