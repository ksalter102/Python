empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = [even, odd] #create a list containing a list
print(numbers)

for number_list in numbers:
    print(number_list)

    for value in number_list:
        print(value)











# sorted_numbers = sorted(numbers) #now in order, in new list
# print(sorted_numbers)
#
# digits = list("432985617")
# print(digits) #will create a list of strings
#
# # more_numbers = list(numbers)
# # more_numbers = numbers[:] # slice existing list
# more_numbers = numbers.copy() #will copy list
# print(more_numbers)
# print(numbers is more_numbers) #false - not same list
# print(numbers == more_numbers) #true - same items in list












# even.extend(odd) #will add odd list to even list
# print(even)
# another_even = even
# print(another_even)
#
# even.sort() #will sort numbers in order
# print(even)
#
# even.sort(reverse=True) #prints in reverse order, highest to lowest
# print(even)
# print(another_even) #will also print in reverse order























# print(min(even)) #2
# print(max(even)) #8
# print(min(odd)) #1
# print(max(odd)) #9
#
# print()
# print(len(even)) #4 - 4 numbers
# print(len(odd)) # 5 - 5 numbers
#
# print()
#
# print("mississippi".count("s")) #will count 4 "s"
# even.append(10)
# print(even)
#
