# BMI CALCULATOR
# BMI = WEIGHT(KG) /  HEIGHT**2 (M**2)
#
# below 18.5 – you're in the underweight range
# between 18.5 and 24.9 – you're in the healthy weight range
# between 25 and 29.9 – you're in the overweight range
# between 30 and 39.9 – you're in the obese range

weight_kg = float(input("enter weight in kgs:\n").strip())
height_M = float(input("Enter height in m:\n").strip())

BMI = weight_kg / (height_M ** 2)
BMI = int(BMI)
print("Your BMI:\n {}".format(BMI))

if BMI <= 18.5:
    print("Underweight")
elif BMI < 24.9 > 18.5:
    print("Healthy")
elif BMI < 29.9 > 25:
    print("overweight")
else:
    print("obese")