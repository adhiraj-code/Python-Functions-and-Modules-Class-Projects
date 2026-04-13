from datetime import date, time, datetime

today = date.today()
print("Today's date is", today)

now = datetime.now()
print(now)

print("\nDate components", today.year, today.month, today.day)