try:
    num1, num2 = eval(input("Enter two numbers seperated by comma : "))
    result = num1 / num2
    print(result)
except ZeroDivisionError:
    print("Number can not be divisible by 0")
except SyntaxError:
    print("Comma is missing")
finally:
    print("Coding is executed")
