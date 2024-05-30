from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
ourMenu = Menu()


machine_on = True
while machine_on == True:
  user_drink = input(f"Choose one of the following items: {ourMenu.get_items()}: ")
  if user_drink == "off":
    machine_on = False
  else:
    ourMenu.find_drink(user_drink)
    choice = MenuItem(user_drink)
