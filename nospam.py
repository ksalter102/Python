menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]
#removing spam

for meal in menu:
    for i in range(len(meal) -1, -1, -1):
        if meal[i] == "spam":
            del meal[i]
    print(", ".join(meal)) #adds commer between items


print("-" * 80)

#or

# for meal in menu:
#     for item in meal:
#         if item != "spam":
#             print(item, end= ", ")# will add commer
#     print()

