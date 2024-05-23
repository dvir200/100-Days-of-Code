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


""" resources = {
    "water": 48,
    "milk": 200,
    "coffee": 15,
} """

print(MENU["espresso"]["ingredients"]["coffee"])

while True:
  user_choice = input("What do you want to order? Espresso, Latte or Cappuccino ")
  user_choice = user_choice.lower()
  print(user_choice)
  for item in MENU[user_choice]["ingredients"]:
    print(item)
    if resources[item] < MENU[user_choice]["ingredients"][item]:
      print(f"Not Enough {item} in the machine")
      break

