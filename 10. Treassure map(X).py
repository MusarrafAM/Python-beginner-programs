
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure?\nEnter Row then coloumn: ")




# print(type(position)) users input is in str need to change to int

hori = position[0] 
vert = position[1] 
hori_int = int(hori) - 1
vert_int = int(vert) - 1

map[hori_int][vert_int] ="X"






print(f"{row1}\n{row2}\n{row3}")