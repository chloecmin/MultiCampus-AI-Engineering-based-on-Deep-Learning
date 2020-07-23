try:
    x = int(input("enter a number > 10 : "))
    if x <= 10:
        raise ValueError
except ValueError:
    print("Error out allowed range")
else:
    print("Within allowed range")