available_parts = ["computer",
                   "monitor",
                   "keyboard",
                   "mouse",
                   "mouse mat",
                   "HDMI Cable",
                    "DVD Drive"
                   ]
# valid_choices = [str(i) for i in range(1, len(available_parts) +1)]
valid_choices = []
for i in range(1, len(available_parts) + 1):
    valid_choices.append(str(i))

current_choice = "-"
computer_parts = [] #create an empty list

while current_choice != '0':
    if current_choice in valid_choices:
        index = int(current_choice) - 1
        # -1 because the first position is 0 on
        # the list so when the input is '1', we mean 0
        chosen_part = available_parts[index]
        if chosen_part in computer_parts:
            #it's already i, so remove it
            print("Removing {}".format(current_choice))
            computer_parts.remove(chosen_part) #removing
        else:
            print("Adding {}".format(current_choice))
            computer_parts.append(chosen_part) #adding
        print("your list now contains {}".format(computer_parts))

    else:
        print("Please add options from list below: ")
        for number, part in enumerate(available_parts):
            print("{0}: {1}".format(number + 1, part))

    current_choice = input("Please type here: ")

print("Here is your list " + str(sorted(computer_parts)))







#built in functions --------------------------------------------------
# #A
# abs()
# aiter()
# all()
# any()
# anext()
# ascii()
#
# B
# bin()
# bool()
# breakpoint()
# bytearray()
# bytes()
#
# C
# callable()
# chr()
# classmethod()
# compile()
# complex()
#
# D
# delattr()
# dict()
# dir()
# divmod()
#
# E
# enumerate()
# eval()
# exec()
#
# F
# filter()
# float()
# format()
# frozenset()
#
# G
# getattr()
# globals()
#
# H
# hasattr()
# hash()
# help()
# hex()
#
# I
# id()
# input()
# int()
# isinstance()
# issubclass()
# iter()
# L
# len()
# list()
# locals()
#
# M
# map()
# max()
# memoryview()
# min()
#
# N
# next()
#
# O
# object()
# oct()
# open()
# ord()
#
# P
# pow()
# print()
# property()
#
#
#
#
# R
# range()
# repr()
# reversed()
# round()
#
# S
# set()
# setattr()
# slice()
# sorted()
# staticmethod()
# str()
# sum()
# super()
#
# T
# tuple()
# type()
#
# V
# vars()
#
# Z
# zip()
#
# _
# __import__()
