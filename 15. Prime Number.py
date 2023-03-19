# Prime number

user = int(input("Enter a number: "))

prime_numbers = []

for user_number in range(1, user + 1):
    if user_number == 1:
        # print(f"Number {user_number} is not a prime number")
        pass
    elif user_number > 1:
        for num in range(2, user_number):
            if user_number % num == 0:
                # print(f"{user_number} is not a prime number")
                break
        else:
            # print(f"{user_number} is a prime number")
            prime_numbers.append(user_number)

print(prime_numbers)
