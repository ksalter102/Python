shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

item_to_find = "Milk"
found_at = None #used to show it doesnt have a value
# for index in range(6):
# for index in range(len(shopping_list)):
#     if shopping_list[index == item_to_find]:
#         found_at = index
#         break

if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)
if found_at is not None:
    print("Item found in position {}".format(found_at))
else:
    print("{} Item not found".format(item_to_find))
