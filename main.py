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
    "coffee": 100
}

money = 0

def resources_sufficient(prompt):
    for items in resources:
        if MENU[prompt]['ingredients'][items] >= resources[items]:
            print(f"Sorry there is not enough {items}.")
            resources_out = True
            return resources_out        

def coin_counter():
    quarters = float(input("How many quarters?"))
    dimes = float(input("How many dimes?"))
    nickles = float(input("How many nickles?"))
    pennies = float(input("How many pennies?"))

    quarters *= 0.25
    dimes *= 0.10
    nickles *= 0.05
    pennies *= 0.01

    total = sum([quarters,dimes,nickles,pennies])

    print(round(total, 2))
    return(total)

machine_on = True

while machine_on:
    
    prompt = input(f"What would you like? (espresso/latte/cappuccino):")

    if prompt == 'off':
        break
    elif prompt == "report":
        for item in resources:
            print(f"{item.capitalize()}: {resources[item]}{"g" if item == "coffee" else "ml"}")
        print(f"Money: ${money}")
    elif prompt == "espresso":
        print("espresso selected")
        if resources_sufficient(prompt) == None:
            print(f"There are enough resources, we can proceed to the next task")
        break   
    elif prompt == "latte":
        print("latte selected")
        if resources_sufficient(prompt) == None:
            print(f"There are enough resources, we can proceed to the next task")
            coin_counter()
        break   
    elif prompt == "cappucino":
        if resources_sufficient(prompt) == None:
            print(f"There are enough resources, we can proceed to the next task")   
        print(f"cappucino selected")
        break
    

