name = input("Your name?")
age = int(input("What is your current age? "))

months = (90 - age) * 12
weeks = (90 - age) * 52
days = (90 - age) * 365

print(f"Great {name}, you are {age} years old\n"
      f"you have:\n"
      f"{months} Months\n"
      f"{weeks} Weeks\n"
      f"{days} Days")