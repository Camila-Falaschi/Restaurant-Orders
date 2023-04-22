import pandas as pd

from services.inventory_control import InventoryMapping
from services.menu_data import MenuData
from models.ingredient import Restriction

DATA_PATH = "data/menu_base_data.csv"
INVENTORY_PATH = "data/inventory_base_data.csv"


class MenuBuilder:
    def __init__(self, data_path=DATA_PATH, inventory_path=INVENTORY_PATH):
        self.menu_data = MenuData(data_path)
        self.inventory = InventoryMapping(inventory_path)

    def make_order(self, dish_name: str):
        try:
            curr_dish = [
                dish
                for dish in self.menu_data.dishes
                if dish.name == dish_name
            ][0]
        except IndexError:
            raise ValueError("Dish does not exist")

        self.inventory.consume_recipe(curr_dish.recipe)

    # Req 4
    def get_main_menu(self, restriction=None) -> pd.DataFrame:
        menu = {
            "dish_name": [],
            "ingredients": [],
            "price": [],
            "restrictions": [],
        }

        for dish_data in self.menu_data.dishes:
            dish_restrictions_list = dish_data.get_restrictions()
            menu_has_restriction = False
            for restriction_data in dish_restrictions_list:
                if restriction_data == restriction:
                    menu_has_restriction = not menu_has_restriction

            if not menu_has_restriction:
                menu["dish_name"].append(dish_data.name)
                menu["ingredients"].append(dish_data.get_ingredients())
                menu["price"].append(dish_data.price)
                menu["restrictions"].append(dish_restrictions_list)

        df = pd.DataFrame(menu)
        return df
