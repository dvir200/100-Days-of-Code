from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
ourMenu = Menu()
money_object = MoneyMachine()

machine_on = True
while machine_on == True:
  user_drink = input(f"Choose one of the following items: {ourMenu.get_items()}: ")
  if user_drink == "off":
    machine_on = False
  elif user_drink == "report":
    coffee_maker.report()
    money_object.report()
  else:
    if ourMenu.find_drink(user_drink) != None:
      user_drink = ourMenu.find_drink(user_drink)
      if coffee_maker.is_resource_sufficient(user_drink) is True:
        if money_object.make_payment(user_drink.cost) is True:
          coffee_maker.make_coffee(user_drink)