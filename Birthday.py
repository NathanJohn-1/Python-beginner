from datetime import date
birth_year = int(input("Enter your birth year: "))
birth_month = int(input("Enter your birth month: "))
birth_day = int(input("Enter your birth day: "))
today = date.today()
first_check = 2025 - birth_year
T_F = 1
if birth_year > today.year or birth_year < 1:
    T_F = 0
    print("Invalid birth year")
if birth_year == today.year and birth_month >today.month:
    T_F = 0
    print("Invalid birth month")
if birth_year == today.year and birth_month == today.month and birth_day >today.day:
    T_F = 0
    print("invalid birth day")
if birth_year == today.year and birth_month == today.month and birth_day == today.day:
    T_F = 0
    age = 0
    print("Your age is: ",age)

if birth_month > 12 or birth_month < 1:
    T_F = 0
    print("Invalid birth month")

if birth_month == 1 or birth_month == 3 or birth_month == 5 or birth_month == 7 or birth_month == 8 or birth_month == 10 or birth_month == 12:
    if birth_day > 31 or birth_day < 1:
       T_F = 0
       print("Invalid birth day")
elif birth_month == 2:
    second_check = birth_year/4
    third_check = birth_year/100
    fourth_check = birth_year/400
    code = 1

    if second_check.is_integer():
        if third_check.is_integer():
            code = 1
        else:
         code = 2

    if fourth_check.is_integer():
        code = 2

    if code == 1:
      if birth_day > 28 or birth_day < 1:
       T_F = 0
       print("Invalid birth day")
    if code == 2:
      if birth_day > 29 or birth_day < 1:
       T_F = 0
       print("Invalid birth day")
else:
    if birth_day >30 or birth_day < 1:
        T_F = 0
        print("Invalid birth day")


if T_F == 1:
 if birth_month > today.month:
    age = first_check - 1
    print("Your age is: ",age)
 elif birth_month < today.month:
    age = first_check
    print("Your age is: ",age)
 else:
    if birth_day > today.day:
        age = first_check -1
        print("Your age is: ",age)
    else:
        age = first_check
        print("Your age is: ",age)


print(today)











