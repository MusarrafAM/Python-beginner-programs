
year = int(input("Which year do you want to check? "))



if year % 4 == 0:
  if year % 100 ==0:
    print(f" {year} is not a leap year.")
    if year % 400 == 0:
      print(f"HURRAY {year} is a leap year")
    else:
      print(f"{year} Is not a leap year")
  else:
    print(f"Hurray {year} Is a leap year")
else:
  print(f"{year} Is not a leap year")
 






