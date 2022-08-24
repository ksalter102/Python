shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]


# for i in shopping_list:
#     if i == "spam":
#         continue #causes everything after loop when "spam" is hit to be skipped e.g buy spam is skipped
#     print("buy " + i)

for i in shopping_list:
    if i == "spam":
        break #will stop the code running when it hits "spam"
    print("buy " + i)