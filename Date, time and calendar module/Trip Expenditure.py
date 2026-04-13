def hotel(nights):
    return nights * 2

def plane_cost(city):
    if city.lower() == "paris":
        return 200
    elif city.lower() == "london":
        return 250
    elif city.lower() == "new york":
        return 300
    
def trip_cost(city, nights, spending_money):
    return hotel(nights) + plane_cost(city) + spending_money

total_cost = trip_cost("Paris", 5, 100)
print("Total trip cost:", total_cost)
