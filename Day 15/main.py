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

""" resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
} """

PROFIT = 0.00

resources = {
    "water": 48,
    "milk": 200,
    "coffee": 15,
}

print(MENU["espresso"]["ingredients"]["coffee"])

def calc (product_price, quarters, dimes, nickles, pennys):
  coin_input = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennys * 0.01)
  if coin_input < product_price:
    return 0
  elif coin_input == product_price:
    return 1
  else:
    PROFIT += coin_input
    return [1, coin_input - product_price]


while True:
  missing_ingredients = []
  user_choice = input("What do you want to order? Espresso, Latte or Cappuccino ")
  user_choice = user_choice.lower()
  print(user_choice)
  for item in MENU[user_choice]["ingredients"]:
    print(item)
    if resources[item] < MENU[user_choice]["ingredients"][item]:
      missing_ingredients.append(item)
  if len(missing_ingredients) > 0:
    """ print to the customer what is missing """
  else:
    print("Please insert coins")
    quarters = input("How many quarters? ")
    dimes = input("How many dimes? ")
    nickles = input("How many nickles? ")
    pennys = input("How many pennys? ")

    result_check = calc(MENU[user_choice].get("cost"), quarters, dimes, nickles, pennys)
    if result_check[0] == 0:
        print("Not enough coins inserted")
    else:
        print(f"Here is your {user_choice}, ")
