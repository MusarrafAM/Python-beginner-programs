
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")




weight_as_int = int(weight)
height_as_float = float(height)

# Using the exponent operator **
bmi = weight_as_int / height_as_float ** 2
# or using multiplication and PEMDAS
bmi = weight_as_int / (height_as_float * height_as_float)

bmi_as_int = int(bmi)

print(bmi_as_int)

# Rounding
print(int(8/3)) #=>2
print(round(8/3)) #=>3
print(round( 8 /3, 2)) #=>2.67
print(round(2.6666666666 ,2)) #=>2.67

#Floor divition(int divition) =>//
print(8 // 3)#outcome will be int.not the float



#  +=  -=   /=   *=
score = 0

score = score + 1 #typical way
score += 1 #Advance way



#F-string=>put f before double quotes and need to enter the other data type in a curly brecs {}

points = 1
my_height = 1.9
iswinning = True
print(f"Your points is {points},Your height is {my_height}, You are winning is {iswinning}")






















