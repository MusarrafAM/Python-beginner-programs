age = input("What is your current age?")


#print(type(age)) =>age in strings
int_age = int(age)
left_year = 90 - int_age

days = 365 * left_year
weeks = 52 * left_year
months = 12  * left_year

message = f"You have {days} days, {weeks} weeks, and {months} months left."

print(message)
 




