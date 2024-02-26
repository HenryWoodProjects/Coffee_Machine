coffee_emoji = "☕"

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
    "money": 0,
}


def report():
    print(resources)


def power_off():
    exit()


def check_water(order):
    if resources["water"] >= MENU[order]["ingredients"]["water"]:
        return True
    else:
        return False


def check_milk(order):
    if resources["milk"] >= MENU[order]["ingredients"]["milk"]:
        return True
    else:
        return False


def check_coffee(order):
    if resources["coffee"] >= MENU[order]["ingredients"]["coffee"]:
        return True
    else:
        return False


def check_resources(order):
    a = check_water(order)
    b = check_milk(order)
    c = check_coffee(order)
    if a and b and c:
        return True
    else:
        return False


def check_payment(order):
    print("\nPlease enter coins.")
    quarters = float(input("How many quarters?"))
    dimes = float(input("How many dimes?"))
    nickles = float(input("How many nickels?"))
    pennies = float(input("How many pennies?"))
    total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    if total >= MENU[order]["cost"]:
        change = total - MENU[order]["cost"]
        if change > 0:
            print(f"\nHere is ${'{0:.2f}'.format(change)} in change.")
        resources["money"] += MENU[order]["cost"]
        resources["water"] -= MENU[order]["ingredients"]["water"]
        resources["milk"] -= MENU[order]["ingredients"]["milk"]
        resources["coffee"] -= MENU[order]["ingredients"]["coffee"]
        print(f"\n\nHere is your {order.title()} {coffee_emoji}.\nThank you.")
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return


on = True
while on:
    proceed = False
    print("\nPrices:")
    for item in MENU:
        print(f"{item.title()}: ${'{0:.2f}'.format(MENU[item]['cost'])}")
    choice = input("\n\nWhat would you like? (Espresso/Latte/Cappuccino): ").lower()
    if choice == "off":
        power_off()
    elif choice == "report":
        report()
    else:
        if check_resources(choice):
            proceed = True
        else:
            if not check_water(choice):
                print("Sorry there is not enough water.")
            if not check_milk(choice):
                print("Sorry there is not enough milk.")
            if not check_coffee(choice):
                print("Sorry there is not enough coffee.")
        if proceed:
            check_payment(choice)
    available = 0
    for item in MENU:
        if check_resources(item):
            available += 1
    if available == 0:
        print("\n\nSorry, this machine no longer has the resources to make any more drinks, "
              "please refill the hoppers.")
        power_off()
