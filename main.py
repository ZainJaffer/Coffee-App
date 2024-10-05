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
    "milk": 20,
    "coffee": 100
}

def resources_sufficient(prompt):
    for items in resources:
        if MENU[prompt]['ingredients'][items] >= resources[items]:
            print(f"Sorry there is not enough {items}.")
            resources_out = True
            return resources_out        

prompt = input(f"What would you like? (espresso/latte/cappuccino):")

if resources_sufficient(prompt) == None:
    print(f"There are enough resources, we can proceed to the next task")


machine_on = True

# while machine_on:

#     if prompt == 'off':
#         break
#     elif prompt == "report":
#         print(f"report to follow")
#     elif prompt == "espresso":
#         print("espresso selected")
#     elif prompt == "latte":
#         print("latte seelcted")
#     elif prompt == "cappucino":
#         print(f"cappucino selected")
    

