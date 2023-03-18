
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

both_name = name1 + name2
lower_both_name = both_name.lower()

t = lower_both_name.count("t")
r = lower_both_name.count("r")
u = lower_both_name.count("u")
e = lower_both_name.count("e")

true = t + r + u + e
str_true = str(true)

l = lower_both_name.count("l")
o = lower_both_name.count("o")
v = lower_both_name.count("v")
e = lower_both_name.count("e")

love = l+ o + v + e
str_love = str(love)


love_score = str_true + str_love
int_love_score = int(love_score)

if (int_love_score < 10) or (int_love_score >90): #Here ()  is optional.For better reading we used ().
  sentence = "You go together like coke and mentos."
elif int_love_score > 40 and int_love_score <50:
  sentence = "You are alright together."
else:
  sentence = ""



print(f"Your love score is {love_score},{sentence}")
