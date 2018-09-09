# x = int(input("x = "))
# op = input("Operation(+, -, *, /): ")
# y = int(input("y = "))

# if op == '+':
#     z = x + y
#     print(x, '+', y, '=', z)
# elif op == '-':
#     z = x - y
#     print(x, '-', y, '=', z)
# elif op == '*':
#     z = x * y
#     print(x, '*', y, '=', z)
# elif op == '/':
#     z = x / y
#     print(x, '/', y, '=', z)
# else:
#     print('Invalid operator')

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


