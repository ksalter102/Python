# {key: Value}

programming_dictionary = {
    "Bug": "An error in a program that prevents the program"
    " from running as expected.",
    "Fuction": "A piece of code that you can easily call over and over again",
}
#finding value in dictionary

programming_dictionary["Bug"]

#adding new items to dictionary

programming_dictionary["Loop"] = "The action of doing something over and over again"

empty_dictionary = {}
empty_dictionary["Test"] = "I am testing adding into a dictionary"

#wipe existing dictionary

# programming_dictionary = {}

#edit item in dictionary

programming_dictionary["Bug"] = "A moth in computer"

#loop through dictionary

for key in programming_dictionary:
    print(key) #will print each key but not value
    print(programming_dictionary[key]) #print value aswell




