print("Welcome to Blind Auction")


print("Welcome to bid")
again = True
user_dictionary = {}
winner_name = ""


def highest_bid_amount(bid_record):
    high_bid = 0
    for key in bid_record: 
        ubid = bid_record[key]
        if ubid > high_bid:
            high_bid = ubid
            winner_name = key
    print(f"The winner is {winner_name} with the bidding of ${high_bid}")

    
while again :
    name = input("What is yout name?: ")
    bid = int(input("What's your bid?: $"))
    user_dictionary [name] = bid
    print(user_dictionary)
    user_again = input("Do you wanne bid again?: Type 'yes' or  'no'").lower()
    if user_again == "no":
        again = False

highest_bid_amount(bid_record = user_dictionary )







