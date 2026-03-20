MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "coin": 0.0,
}

coins = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01
}

def resources_format(drink):
    water_need = MENU[drink]["ingredients"]["water"]
    milk_need = MENU[drink]["ingredients"]["milk"]
    coffee_need = MENU[drink]["ingredients"]["coffee"]
    if water_need > resources["water"]:
        print("sorry there is not enough water")
        return False
    elif milk_need > resources["milk"]:
        print("sorry there is not enough water")
        return False
    elif coffee_need > resources["coffee"]:
        print("sorry there is not enough water")
        return False
    else:
        return True

def coin_counter(drink, profit):
    money_inserted = 0
    change = 0
    price = MENU[drink]["cost"]
    print("Please insert coins.")
    n_quarters = int(input("How many quarters?: "))
    n_dimes = int(input("How many dimes?: "))
    n_nickles = int(input("How many nickles?: "))
    n_pennies = int(input("How many pennies?: "))
    money_inserted += (n_quarters * 0.25 + n_dimes * 0.10 + n_nickles * 0.05 + n_pennies * 0.01)
    if money_inserted >= price:
        change += float((money_inserted - price))
        print(f"Here is ${change} in change\n"
              f"Here is your {drink}. Enjoy!"
              )
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False

def sale_check(drink):
    water_left = resources["water"] - MENU[drink]["ingredients"]["water"]
    milk_left = resources["milk"] - MENU[drink]["ingredients"]["milk"]
    coffee_left = resources["coffee"] - MENU[drink]["ingredients"]["coffee"]
    money_earned = resources["coin"] + MENU[drink]["cost"]
    resources["water"] = water_left
    resources["milk"] = milk_left
    resources["coffee"] = coffee_left
    resources["coin"] = money_earned

power_on = True
while power_on:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    money = resources["coin"]
    if order == "off":
        power_on = False
        break
    if order == "report":
        print(
            f"Water: {resources["water"]}ml\n"
            f"Milk: {resources["milk"]}ml\n"
            f"Coffee: {resources["coffee"]}ml\n"
            f"Money: ${resources["coin"]}"
        )
    if order != "report":
        if resources_format(order):
            if coin_counter(order, money):
                sale_check(order)
        else:
            break

