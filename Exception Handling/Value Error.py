try:
    age = int(input("Enter you age : "))
    print(age)
except ValueError as ve:
    print("ValueError", ve)
