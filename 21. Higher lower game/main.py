import random
from art import logo, vs
from game_data import data
# from replit import clear


#radnomely select 1 data using choice from the lsit
def random_dic():
    """Create a random dictionary"""
    random_dictionary = random.choice(data)
    return random_dictionary



#Create a functuion called score_finder 
def high_score (first_score,second_score):
    """retrun highest value A or B"""
    if first_score > second_score:
        return "A"
    elif second_score > first_score:
        return "B"
    
 
#print the logo
print (logo)

#Create A
first = random_dic()
print(f"Compare A: {first['name']}, a {first['description']}, from {first['country']}.")
first_score = first['follower_count']
print(first_score)


#while the answer is correct continue the game

    
#vs logo
print(vs)

#create B
second = random_dic()
print(f"Against B: {second['name']}, a {second['description']}, from {second['country']}.")
second_score = second['follower_count']
print(second_score)
    
   
    
#user enter choise and check the answer using  fucntion called check
    
answer_correct = True
score = 0
while answer_correct: 
    winner = high_score(first_score,second_score)
    user = input("Who has more followers? Type 'A' or 'B'").upper()
    if user == winner:
        # clear()
        score +=  1
        print (logo)
        print(f"Your total score is {score}")
        answer_correct = True
        print(f"Against A: {second['name']}, a {second['description']}, from {second['country']}.")
        first_score = second_score
        print(first_score)
        print (vs)
        
        second = random_dic()
        print(f"Against B: {second['name']}, a {second['description']}, from {second['country']}.")
        second_score = second['follower_count']
        print(second_score)
        
        
    else :
        answer_correct = False
        # clear()
        print (f"Sorry thats wrong, Final score is {score}")
        

    
    
    
    
    













