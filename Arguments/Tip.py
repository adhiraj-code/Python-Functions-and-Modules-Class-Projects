# to calculate the tip amount from the bill amount

def calculate(bill, tip):
    if bill <= 0:
        print("Bill amount should be greater than 0")
    else:
        return(bill * tip) / 100
    
print(calculate(1000, 10))
