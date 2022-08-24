# row1 = ["🤠️  ","🤖️","⚔️"]
# row2 = ["⭐️","🐻️","🏹️"]
# row3 = ["⚪️","🤖️","🔫️"]


row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure?\nHorizontal 1:3\nVertical 1:3\n")


horizontal = int(position[0]) #1st number
vertical = int(position[1]) #2nd number

map[vertical -1][horizontal - 1] = "X"


print(f"{row1}\n{row2}\n{row3}")
