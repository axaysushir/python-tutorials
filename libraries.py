from datetime import date

date.fromisoformat('2021-04-12')
today = date.today()
print(today)


my_birthday = date(today.year, 6, 24)
if my_birthday < today:
    my_birthday = my_birthday.replace(year=today.year + 1)

print(my_birthday)