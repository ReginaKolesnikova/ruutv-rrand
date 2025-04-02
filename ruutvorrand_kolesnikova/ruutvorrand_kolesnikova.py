# 1
neutrall=float(input("Input number: "))
if neutrall > 0:
    print("Positive")
    if neutrall % 2 == 0:
        print("Even")
    else:
        print("Odd")
else:
    print("Negative")

# 2
a = float(input("1st angle: "))
b = float(input("2nd angle: "))
c = float(input("3rd angle: "))
if a+b+c==180:
    if a==b==c:
        print("equilateral triangle") #ravnostoronniy
    elif a==b or a==c or b==c:
        print("isosceles triangle") #ravnobedrenniy
    else:
        print("scalene triangle") #raznostoronniy
else:
    print("It is not triangle (should be 180 degrees)")


# 3
answerr=input("Do you want to convert number of weekday in word? (yes/no): ").lower()
if answerr=="yes":
    wekday=int(input("Enter day of week (number from 1 to 7): "))
    if 1 <= wekday <=7:
        if wekday == 1:
            print("Monday")
        elif wekday == 2:
            print("Tuesday")
        elif wekday == 3:
             print("Wednesday")
        elif wekday == 4:
             print("Thursday")
        elif wekday == 5:
            print("Friday")
        elif wekday == 6:
            print("Saturday")
        else:
            print("Sunday")
    else:
        print("This weekday doesnt exist")
else:
    print("Goodbye")

#4
def get_zodiac_sign(day, month):

    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorn"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius"
    else:
        return "Pisces"

def check_date(day, month):

    if not isinstance(day, int) or not isinstance(month, int):
        print("Error: day should be an integer")
        return False
    
    if month < 1 or month > 12:
        print("Error: month should be between 1 and 12")
        return False
    
    days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (month == 2 and day > 29) or (day < 1 or day > days_in_month[month - 1]):
        print(f"Error: there is no such day in this month")
        return False
    
    return True

def main():
    print("Getting zodiac sign out of your birthday")
    
    try:
        day = int(input("Day of birth: "))
        month = int(input("Month of birth: "))
    except ValueError:
        print("Error: day and month should be integers.")
        return
    
    if check_date(day, month):
        zodiac_sign = get_zodiac_sign(day, month)
        print(f"Your zodiac sign is: {zodiac_sign}")
    else:
        print("Retry with right data.")

if __name__ == "__main__":
    main()

#5
strinteger = input("Enter text or number: ")
if strinteger.isdigit():  
    number = int(strinteger)
    print(f"50 percent out of your integer would be: {number} = {number * 0.5}")
elif strinteger.replace('.', '').isdigit():
    number = float(strinteger)
    print(f"70 percent out of your float number would be: {number} = {number * 0.7}")
elif strinteger.isalpha():  
    print(f"You entered this text: {strinteger}")
else:
    print("Wrong data.")


#6
import math

answer = input("Do you want to find discriminant? (yes/no): ").strip().lower()
if answer == "yes":

    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))

    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print(f"Two roots: x1 = {x1} и x2 = {x2}")
    elif discriminant == 0:
        x = -b / (2 * a)
        print(f"One root: x = {x}")
    else:
        print("No roots")
else:
    print("Goodbye")

