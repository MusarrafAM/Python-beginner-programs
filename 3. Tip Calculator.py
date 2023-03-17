#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60


print("Welcome to Musarraf's tip calculator")
bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage of tip would you like to give? 10, 12, 15? (Dont add % sign)"))
num_people = int(input("How many people to split the bill? "))
# user entered data is in str so we covered it to int and foat



total_tip = (bill * tip_percentage / 100)
final_bill = bill + total_tip
each_person_bill = final_bill / num_people
final_bill = round(each_person_bill, 2)
#If you want the final_amount to always have 2 decimal places.
#e.g. $12 becomes $12.00

#This is how you can implement it:
final_bill = "{:.2f}" .format(each_person_bill)#extra get from googeld lecture also googled not worry much sometimes round doest work properly this is only for that 
print(f"Each person should pay ${final_bill}")

#line 21 or 22 one is enoughf round funct sometimes doesn't work properly thats why line 22




