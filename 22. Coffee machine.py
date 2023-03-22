MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# TODO 1: Change the menus ingredients / Dictionaries to usable formate.

espresso_water = MENU["espresso"]["ingredients"]["water"]
espresso_milk = 0
espresso_coffee = MENU["espresso"]["ingredients"]["coffee"]
espresso_cost = MENU["espresso"]["cost"]


latte_water = MENU["latte"]["ingredients"]["water"]
latte_milk = MENU["latte"]["ingredients"]["milk"]
latte_coffee = MENU["latte"]["ingredients"]["coffee"]
latte_cost = MENU["latte"]["cost"]


cappuccino_water = MENU["cappuccino"]["ingredients"]["water"]
cappuccino_milk = MENU["cappuccino"]["ingredients"]["milk"]
cappuccino_coffee = MENU["cappuccino"]["ingredients"]["coffee"]
cappuccino_cost = MENU["cappuccino"]["cost"]


# Resources
resources_water = resources["water"]
resources_milk = resources["milk"]
resources_coffee = resources["coffee"]
resources_money = 0


# TODO 2: create a function for report. Machine.
def call_report(m_water, m_milk, m_coffee, m_money):
    """print the report when called"""
    print(f"Water : {m_water}ml\nMilk : {m_milk}ml\nCoffee : {m_coffee}g\n"
          f"Money : {m_money}$")


# TODO 3 : function for take money :
def process_coin():
    """Return total money user entered"""
    print("Please insert coins ")
    quarters = (int(input("how many quarters? : "))) * 0.25
    dimes = (int(input("how many dimes? : "))) * 0.10
    nickles = (int(input("how many nickles? : "))) * 0.05
    pennies = (int(input("how many pennies? : "))) * 0.01

    total_money = quarters + dimes + nickles + pennies
    return total_money


# check sufficient money or not and give balance
def money_check(user_entered_money, beverage_cost):
    """Return True or FLase after checking money and print the balance"""
    if user_entered_money >= beverage_cost:
        balance = user_entered_money - beverage_cost
        rounded_balance = round(balance, 2)
        print(f"Here is ${rounded_balance} in change.")
        return True
    else:
        return False


# TODO 3 : Create a function for checking

def check_resources(drink_water, drink_milk, drink_coffee, machine_water, machine_milk, machine_coffee):
    if machine_water >= drink_water:
        if machine_milk >= drink_milk:
            if machine_coffee >= drink_coffee:
                return True
            else:
                print("Sorry, There is not enough Coffee")
        else:
            print("Sorry, There is not enough Coffee Milk")
    else:
        print("Sorry, There is not enough  Water")

    return False


def coffee_machine():
    global resources_money
    global resources_water
    global resources_milk
    global resources_coffee
    should_continue = True
    while should_continue:
        user = input("What would you like? (espresso/latte/cappuccino):").lower()
        if user == "espresso" and check_resources(espresso_water, espresso_milk, espresso_coffee, resources_water,
                                                  resources_milk, resources_coffee):
            user_entered_money = process_coin()
            if money_check(user_entered_money, espresso_cost):
                resources_water -= espresso_water
                resources_milk -= espresso_milk
                resources_coffee -= espresso_coffee
                resources_money += espresso_cost
                print("Here is your espresso ☕. Enjoy ")
            else:
                print("Sorry that's not enough money. Money refunded.")
        elif user == "latte" and check_resources(latte_water, latte_milk, latte_coffee, resources_water, resources_milk,
                                                 resources_coffee):
            user_entered_money = process_coin()
            if money_check(user_entered_money, latte_cost):
                resources_water -= latte_water
                resources_milk -= latte_milk
                resources_coffee -= latte_coffee
                resources_money += latte_cost
                print("Here is your latte ☕. Enjoy ")
            else:
                print("Sorry that's not enough money. Money refunded.")
        elif user == "cappuccino" and check_resources(cappuccino_water, cappuccino_milk, cappuccino_coffee,
                                                      resources_water, resources_milk, resources_coffee):
            user_entered_money = process_coin()
            if money_check(user_entered_money, cappuccino_cost):
                resources_water -= cappuccino_water
                resources_milk -= cappuccino_milk
                resources_coffee -= cappuccino_coffee
                resources_money += cappuccino_cost
                print("Here is your cappuccino ☕. Enjoy ")
            else:
                print("Sorry that's not enough money. Money refunded.")
        elif user == "report":
            call_report(resources_water, resources_milk, resources_coffee, resources_money)
        elif user == "off":
            should_continue = False  # WE can use return here. as well to stop the programme.


coffee_machine()
