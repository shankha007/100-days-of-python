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

income = 0.0


def print_report():
    print("Here it the report:")
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}ml")
    print(f"Money: ${income}")


def is_resource_available(u_choice_ing):
    if "water" in u_choice_ing and u_choice_ing["water"] > resources["water"]:
        resource = "water"
    elif "milk" in u_choice_ing and u_choice_ing["milk"] > resources["milk"]:
        resource = "milk"
    elif "coffee" in u_choice_ing and u_choice_ing["coffee"] > resources["coffee"]:
        resource = "coffee"
    else:
        return True

    print(f"Sorry there is not enough {resource}")
    return False


def take_money():
    print("Please insert coins.")
    pennies = int(input("Pennies: "))
    nickles = int(input("Nickles: "))
    dimes = int(input("Dimes: "))
    quarters = int(input("Quarters: "))

    total_money = pennies * 0.01 + nickles * 0.05 + dimes * 0.1 + quarters * 0.25

    return total_money


def process_transaction(u_coffee, u_money):
    global income
    income += u_coffee["cost"]
    if u_money > u_coffee["cost"]:
        change = u_money - u_coffee["cost"]
        print(f"Here is ${round(change, 2)} dollars in change.")


def process_coffee(u_coffee):
    coffee_ing = MENU[user_choice]["ingredients"]

    if "water" in coffee_ing:
        resources["water"] -= coffee_ing["water"]

    if "milk" in coffee_ing:
        resources["milk"] -= coffee_ing["milk"]

    if "coffee" in coffee_ing:
        resources["coffee"] -= coffee_ing["coffee"]


    print(f"Here is your {u_coffee}. Enjoy!")


coffee_machine_is_open = True

while coffee_machine_is_open:
    user_choice = input("What would you like? (espresso/latte/cappuccino):").lower()

    if user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
        user_chosen_coffee = MENU[user_choice]

        if is_resource_available(user_chosen_coffee["ingredients"]):
            user_money = take_money()

            if user_money < user_chosen_coffee["cost"]:
                print("Sorry that's not enough money. Money refunded.")
            else:
                process_transaction(user_chosen_coffee, user_money)
                process_coffee(user_choice)
    elif user_choice == "report":
        print_report()
    elif user_choice == "off":
        coffee_machine_is_open = False
    else:
        print("Wrong input. Please try again.")

