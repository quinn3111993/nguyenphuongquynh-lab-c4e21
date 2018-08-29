items = [2,5,8,57,-68,2,-9,0]

x = int(input("Enter a number: "))

if x in items:
    print("Found")
    print(items.index(x))
else:
    print("Not found")