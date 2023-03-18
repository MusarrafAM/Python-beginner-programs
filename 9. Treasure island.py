print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Musa's Treasure Island.")
print("Your mission is to find the treasure.")


selection1 = input("You are at a cross road. do you want to go 'left' or 'right'?\n").lower()
if selection1 == "left":
    print("You fell into abyys\nNever start with left\n GAME OVER")
elif selection1 == "right":
    selection2 = input("You have come to a beach\nDo You want to 'swim' to the island or 'wait' for the boat?\n").lower()
    if selection2 == "swim":
        print("Shark just got your head off !!!\nNeed to Be pations sometimes\nGAME OVER")
    elif selection2 == "wait":
        selection3 = input("You've Reached the island safely\nWhen you enter the castle there are 3 doors to open which door do you chose? 'Red' or 'Green' 'Yellow' \n").lower()
        if selection3 == "red":
            print("You just entered the HELL and burned there\nRED is caution\n GAME OVER")
        elif selection3 == "yellow":
            print("You enter the time loop and died there\nGAME OVER")
        elif selection3 == "green":
            print("You just enter the PARADISE and got The treassure\nYOU WON THE GAME\nThanks for playing Musa's Treassure island")
        print('''
              
                 ,-""""-.
               ,'      _ `.
              /       )_)  \
             :              :
             \              /
              \            /
               `.        ,'
                 `.    ,'
                   `.,'
                    /\`.   ,-._
                        `-'                hjw
                                                                   ,jf
   _am,    ,_am,  ,_g_oam,    _am,   _g_ag,   _am,   koewkovg   _mm_
 ,gF  @._-gF   @-"  jf   @  ,gF  @  ^ NX  #_,gF  @     jf      qK  "
 8Y      8Y    d   j#   jF .8Y  ,d   dY     8Y   d    jf       *b,
jK   ,  jK   ,N   jN   jF  :K  ,Z  ,jF     jK  ,Z"  ,jfk,       dN.
 NbpP    NbpP    dP   dFk_o8NbpP"V^dF       NbpY"V^"dF "dYo-"*h,W"
                         ,gF',@'
                        :8K  j8
                         "*w*"
              ''')