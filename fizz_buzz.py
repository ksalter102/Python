#   divisble by 3 - FIZZ
#  divisible by 5 - bizz
#   both - FIZZ BUZZ
# UP TO AND INCLUDING 100

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FIZZBUZZ")
    if number % 3 ==0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)