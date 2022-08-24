print("Welcome to the tip calculator")
bill = float(input("What was the total bill? £"))
people = int(input("How many people are there to split between?"))
tip = int(input("Choose a tip: \n12% \n15% \n20%\n"))

tip_new = bill / people * (tip / 100)
tip_new = round(tip_new, 2)
final_amount = tip_new + bill
print(f"Your tip will be £{tip_new}")
print(f"Your bill will now be £{final_amount}")
