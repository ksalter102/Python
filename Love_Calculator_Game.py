# Love Calculator
#
# TRUE LOVE
# USE lower() function - will make all lower case
# USE count() function - will give number of times a letter occurs
# keelan.count("TRUELOVE")

print("Welcome to the Love Calculator!")
name1 = input("What's your name?\n ")
name2 = input("What is their name?\n ")

combined_string = name1 + name2
lower_case_string = combined_string.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")
total_true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e_e = lower_case_string.count("e")
total_love = l + o + v + e_e

truelove = total_love + total_true

if truelove < 10 or truelove > 90:
    print("Your score is {}, you can do better!".format(truelove))
elif truelove <= 50 and truelove >= 40:
    print("Your score is {}, not bad together!".format(truelove))
else:
    print("Your score is {}, you are amazing!".format(truelove))

