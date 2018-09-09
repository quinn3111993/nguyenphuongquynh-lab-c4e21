from random import randint, choice
from calc import calculate

op_list = ['+', '-', '*', '/']
op = choice(op_list)

x_list = range(1,9)
x = choice(x_list)
y = choice(x_list)

correct_z = calculate(x,y,op)
z = correct_z + randint(-2,2)

if z == correct_z:
    correct_ans = 'Y'
else:
    correct_ans = 'N'

print(x, op, y, '=', z)

answer = input('Input answer (Y/N): ').upper()
if answer in ['Y', 'N']:
    if answer == correct_ans:
        print('Correct!')
    else:
        print('Incorrect!')
else:
    print('Invalid answer')






