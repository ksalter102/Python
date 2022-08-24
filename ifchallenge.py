name = str(input("Please enter your name: "))
age = int(input("Please enter your age: "))

if age >= 18 and age <= 30:
    print("Hello {}, enjoy your holiday".format(name))
else:
    print("{}, you shall not pass".format(name))

