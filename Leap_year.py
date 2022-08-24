# CHALLENGE LEAP YEAR
#   if year % 4 == 0 then its a leap year
#       except every year that is everly divisible by 100 - NO LONGER LEAP YEAR
#           unless the year is also evenly divided for 400 - STILL A LEAP YEAR
#
# 2000 / 4 = 500 LEAP
# 2000 / 100 = 20 NOT LEAP
# 2000 / 400 = 5 LEAP
#
# 2100 / 4 = =525 LEAP
# 2100 / 100 = 21 NOT LEAP
# 2100 /400 = 5.25 NOT LEAP

year = int(input("Which year do you want to check?\n "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year!")
        else:
            print("Not a leap year")
    else:
        print("Leap year!")
else:
    print("Not a leap year")