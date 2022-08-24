pangram = "The quick brown fox jumps over the lazy dog"

letters = sorted(pangram) #will create list in alphabetical order
print(letters)

numbers = [2.3, 4.5, 8.7, 9.2, 1.6]
sorted_numbers = sorted(numbers) #will sort in numerical order, created new list
print(sorted_numbers)
print(numbers)

another_sorted_numbers = numbers.sort() #will alter orignal list and sort it
print(numbers)

missing_letter = sorted("The quick brown fox jumped over the lazy dog",
                        key=str.casefold)
print(missing_letter)

names = ["Graham",
         "John",
         "terry",
         "keelan",
         "eleanor"
         ]
names.sort(key=str.casefold) #will be in order and disregard capital letters
print(names)
