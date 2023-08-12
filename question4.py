#Write a function to determine if the given year is a leap year.
#A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400.
#(divisible by 4 = true)(not divisible by 100, unless divisible by 400)
#(leapyear/4 = true)(leapyear / 100 = false else elseif leapyear/400)
#return is boolean (true / false)

def is_leap_year():
    what_year=int(input("Pick a year!, any year!: "))
    if ((what_year % 4) == 0) or (what_year % 400 == 0) and (what_year % 100 != 0):
        print("ding!, ding!, ding!, we have a winner!!")
    else:
        print("you lose")
is_leap_year()