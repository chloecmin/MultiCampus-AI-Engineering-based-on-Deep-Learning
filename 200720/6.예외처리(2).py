try:
    x = int(input('enter a number : '))
    y = int(input('enter a number2 : '))
    result = x/y
except ValueError:
    print("out of allowed a value")
except ZeroDivisionError:
    print("Division zero by a value")
else:
    print("ok")
finally:
    print("end")
