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
day = int(input("Input day of birth: "))
month = int(input("Input month of birth (number): "))

if month == [4,6,9,11] and day > 30:
    print("error")
elif month == [1,3,5,7,8,10,12] and day > 31:
    print("error")
elif month == [2] and day > 29:
    priint("error")
elif month > 12:
    print("error")
else:
 if month == 'december':
    if day < 22:
      print("Sagittarius")
    else:
      print("Capricorn")
 elif month == 'january':
    if day < 20:
      print("Capricorn")
    else:
      print("Aquarius")
 elif month == 'february':
     if day < 19:
      print("Aquarius")
     else:
      print("Pisces")
 elif month == 'march':
     if day < 21:
      print("Pisces")
     else:
      print("Aries")
 elif month == 'april':
     if day < 20:
      print("Aries")
     else:
      print("Taurus")
 elif month == 'may':
     if day < 21:
      print("Taurus")
     else:
      print("Gemini")
 elif month == 'june':
     if day < 21:
      print("Gemini")
     else:
      print("Cancer")
 elif month == 'july':
     if day < 23:
      print("Cancer")
     else:
      print("Leo")
 elif month == 'august':
     if day < 23:
      print("Leo")
     else:
      print("Virgo")
 elif month == 'september':
     if day < 23:
      print("Virgo")
     else:
      print("Libra")
 elif month == 'october':
     if day < 23:
      print("Libra")
     else:
      print("Scorpio")
 elif month == 'november':
     if day < 22:
      print("Scorpio")
     else:
      print("Sagittarius")


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

