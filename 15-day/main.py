# This is a coffee machine project

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
}

# Money in the machine
money = 0

# TODO: 1. Print report of all coffee machine resources
def report():
    """Give the report of all resources"""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")
    
# TODO: 2. Check if the resources are sufficient
def enough_resources(drink=str):
    """Check if there are enough resources"""
    for resource in resources: 
        if MENU[drink]["ingredients"][resource] > resources[resource]:
            print(f"Sorry there is not enough {resource}.")
            return False
    return True
    
# TODO: 3. Process coins
def process_coins(drink=str):
    """Check if the sum of inserted money is enough"""
    coins = {
        "quarters": 0,
        "dimes": 0,
        "nickles": 0,
        "pennies": 0
    }
    global money
    print("Please insert coins.")
    for coin in coins:
        value = input(f"how many {coin}? ")
        if value != '':
            coins[coin] = int(value)
    inserted_sum = coins["quarters"] * 0.25 + coins["dimes"] * 0.1 + coins["nickles"] * 0.05 \
    + coins["pennies"] * 0.01
    price_of_drink = MENU[drink]["cost"]
    change = round(inserted_sum - price_of_drink, 2)
    if change >= 0:
        money += price_of_drink
        print(f"Here is ${change} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

# TODO: 4. Make Coffee
def make_coffee(drink=str):
    """Make coffee"""
    for resource in resources:
        resources[resource] -= MENU[drink]["ingredients"][resource]
    print(f"Here is your {drink} ☕️. Enjoy!")

# TODO: 5. Check resources
def checking_function(drink=str):
    """Checking resources"""
    if enough_resources(drink) and process_coins(drink):
        make_coffee(drink)
        return True
    else:
        False

# TODO: 6. Asking prompt
def asking_prompt():
    """Asking client for a choice"""
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice in MENU:
        checking_function(choice)
    elif choice == "off":
        exit(1)
    elif choice == "report":
        report()
    else:
        asking_prompt()

working = True
while working:
    asking_prompt()