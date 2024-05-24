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

PROFIT = 0.00

""" resources = {
    "water": 48,
    "milk": 200,
    "coffee": 15,
} """

print(MENU["espresso"]["ingredients"]["coffee"])

def calc (product_price, quarters, dimes, nickles, pennys, product):
  global PROFIT
  coin_input = float((quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennys * 0.01))
  if coin_input < product_price:
    print("Not enough coins inserted. money refunded")
  elif coin_input == product_price:
    print(f"Here is your {product}. Enjoy :)")
  else:
    change = (coin_input - product_price)
    reduce_resources(resources, MENU[product]["ingredients"])
    PROFIT += product_price
    print(f"Your change is {change % 10}. Enjoy :)")


""" check function next time """
def reduce_resources (machine_resources, product_ingrediants):
  global resources
  for item in machine_resources:
    if item == product_ingrediants[item]:
      item = item - product_ingrediants[item]



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
    if len(missing_ingredients) == 1:
      print(f"Not Enough {missing_ingredients[0]} to make {user_choice}")
    elif len (missing_ingredients) == 2:
      print(f"Not Enough {missing_ingredients[0]} and {missing_ingredients[1]} to make {user_choice}")
    else:
      print(f"Not Enough {missing_ingredients[0]}, {missing_ingredients[1]} and {missing_ingredients[2]} to make {user_choice}")

  else:
    print("Please insert coins")
    quarters = float(input("How many quarters? "))
    dimes = float(input("How many dimes? "))
    nickles = float(input("How many nickles? "))
    pennys = float(input("How many pennys? "))

    calc(MENU[user_choice].get("cost"), quarters, dimes, nickles, pennys, user_choice)

