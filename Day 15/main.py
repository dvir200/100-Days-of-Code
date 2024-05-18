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

def report(list_resources):
  for item in list_resources:
    if item == "water" or item == "milk":
      print(f"{item}: {list_resources[item]}ml")
    else:
      print(f"{item}: {list_resources[item]}g")


def check_ingridiants(drink, list_resources):
  for item in list_resources:
    if (drink[ingredients[item]]  < list_resources[item])



def get_drink(drink, pennys, nickles, dimes, quarters):


money_gained = 0.0

while True:
  user_input = input("What would you like? (espresso, latte, cappuccino) ")
  if user_input == "report":
    report(resources)

