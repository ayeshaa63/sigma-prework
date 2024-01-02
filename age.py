from datetime import date


def age_calculator(year, month, day):
    given_date = date(year, month, day)
    today_date = date.today()
    diff = abs(given_date - today_date)
    age = diff.days//365
    return f"You are {age} years old"


print(age_calculator(1972, 12, 4))
