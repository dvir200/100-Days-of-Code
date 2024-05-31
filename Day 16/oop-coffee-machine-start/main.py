from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
ourMenu = Menu()
money_object = MoneyMachine()

def operation(list_of_drinks, drink_wanted):
  if drink_wanted == "latte":
    user_drink = list_of_drinks.menu[0]
  elif drink_wanted == "espresso":
    user_drink = list_of_drinks.menu[1]
  elif drink_wanted == "cappuccino":
    user_drink = list_of_drinks.menu[2]
  return user_drink

machine_on = True
while machine_on == True:
  user_drink = input(f"Choose one of the following items: {ourMenu.get_items()}: ")
  if user_drink == "off":
    machine_on = False
  elif user_drink == "report":
    coffee_maker.report()
  else:
    ourMenu.find_drink(user_drink)
    user_drink = operation(ourMenu, user_drink)
    if coffee_maker.is_resource_sufficient(user_drink) is True:
      if money_object.make_payment(user_drink.cost) is True:
        coffee_maker.make_coffee(user_drink)


