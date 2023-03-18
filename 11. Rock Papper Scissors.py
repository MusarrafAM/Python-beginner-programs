rock = '''
      💎💎💎
       ROCK
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
      📜📜📜
       PAPER
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
         ✂️✂️✂️
          SCISSORS
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


import random  # we have to put import all the way up in our code just for now its ok.
print("Welcome to Musa's ROCK PAPER SCISSOR")
user_in = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_in >=3 or user_in < 0:
  print("Invalid Number You Loss")
else:
  game_images=[rock,paper,scissors]
  user_action = game_images[user_in]
  print(f"Users Action{user_action}")
  
  
  computer_action_num = random.randint(0, 2)
  computer_action = game_images[computer_action_num]
  print(f"Computer's Action\n{computer_action}")


  if user_in == 0 and computer_action_num == 1:
    print("You Loss")
  elif user_in == 0 and computer_action_num == 2:
    print("You Win")
  elif user_in == 1 and computer_action_num == 0:
    print("You Win")
  elif user_in == 1 and computer_action_num == 2:
    print("You Loss")
  elif user_in == 2 and computer_action_num == 0:
    print("You Loss")
  elif user_in == 2 and computer_action_num == 1:
    print("You Win")
  elif user_in == computer_action_num:
    print("Draw ")








