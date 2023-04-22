import csv
from models.dish import Dish
from models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self.open_csv_file(source_path)

    def open_csv_file(self, source_path):
        with open(source_path, mode="r") as file:
            csv_file = csv.DictReader(file)
            dishes_list = []
            current_dish = ""
            for dish_data in csv_file:
                if current_dish != dish_data["dish"]:
                    current_dish = dish_data["dish"]
                    new_dish = Dish(
                        dish_data["dish"], float(dish_data["price"])
                    )
                    new_dish.add_ingredient_dependency(
                        Ingredient(dish_data["ingredient"]),
                        int(dish_data["recipe_amount"]),
                    )
                    dishes_list.append(new_dish)
                if current_dish == dish_data["dish"]:
                    dishes_list[-1].add_ingredient_dependency(
                        Ingredient(dish_data["ingredient"]),
                        int(dish_data["recipe_amount"]),
                    )
            for dish_dependency in dishes_list:
                self.dishes.add(dish_dependency)
