num_list = [2,5,8,57,-68,2,-9,0]

num_input = int(input("Enter your number: "))

for i, num in enumerate(num_list):
    if num_input == num:
        print("found it")
        print(i)
        break 
else:
    print("Not found")
