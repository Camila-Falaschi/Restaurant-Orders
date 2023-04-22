from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient
import pytest


# Req 2
def test_dish():
    grilled_bread = Dish("pão na chapa", 2.25)
    yakisoba = Dish("yakisoba", 25.78)

    assert grilled_bread.name == "pão na chapa"
    assert grilled_bread.price == 2.25

    assert grilled_bread.__repr__() == "Dish('pão na chapa', R$2.25)"
    assert grilled_bread.__eq__(grilled_bread) == True
    assert grilled_bread.__eq__(yakisoba) == False
    assert grilled_bread.__hash__() == hash("Dish('pão na chapa', R$2.25)")

    grilled_bread.add_ingredient_dependency(Ingredient("pão"), 1)
    grilled_bread.add_ingredient_dependency(Ingredient("manteiga"), 1)

    assert grilled_bread.recipe == {
        Ingredient("pão"): 1,
        Ingredient("manteiga"): 1,
    }
    assert len(grilled_bread.get_restrictions()) == 2

    assert grilled_bread.get_ingredients() == {
        Ingredient("pão"),
        Ingredient("manteiga"),
    }

    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish("pão na chapa", "2.25")

    with pytest.raises(
        ValueError, match="Dish price must be greater then zero."
    ):
        Dish("pão na chapa", -2.25)
