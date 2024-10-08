MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk" : 0,
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
payment = 0

def resources_sufficient(prompt):
    for items in resources:
        if MENU[prompt]['ingredients'][items] >= resources[items]:
            print(f"Sorry there is not enough {items}.")
            return False
    return True

def coin_counter(prompt):
    print(f"The cost will be ${MENU[prompt]['cost']}")
    
    quarters = 0.25 * float(input("How many quarters?"))
    dimes = 0.10 * float(input("How many dimes?"))
    nickles =  0.05 * float(input("How many nickles?"))
    pennies = 0.01 * float(input("How many pennies?"))

    total = sum([quarters,dimes,nickles,pennies])

    change = round(total - MENU[prompt]['cost'],2)

    if total == MENU[prompt]['cost']:
        return MENU[prompt]['cost']
    elif total > MENU[prompt]['cost']:
        print(f"Here is ${change} in change")
        return MENU[prompt]['cost']    
    else: print("Sorry that's not enough money. Money refunded.")
    return 0

def resource_deductor(prompt):
    
    for items in resources:
        resources[items] -= MENU[prompt]['ingredients'][items]
    return resources

machine_on = True

while machine_on:
    
    prompt = input(f"What would you like? (espresso/latte/cappuccino):")

    if prompt ==  'off':
        break
    elif prompt == "report":
        for item in resources:
            print(f"{item.capitalize()}: {resources[item]}{'g' if item == 'coffee' else 'ml'}")
        print(f"Money: ${money}")
    else:
        drink = MENU[prompt]
        print(prompt, "selected")
        if resources_sufficient(prompt):   
            payment = coin_counter(prompt)
            if payment != 0:
                resource_deductor(prompt)
            money += payment 
 

#TODO: how to change code if dict doesn't specify milk for espresso.
#TODO: implement error handling 