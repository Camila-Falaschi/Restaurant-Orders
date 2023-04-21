from src.models.ingredient import Ingredient  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    cheese_ingredient = Ingredient("queijo mussarela")
    water_ingredient = Ingredient("água")

    assert water_ingredient.__hash__() == hash(water_ingredient.name)
    assert water_ingredient.__eq__(water_ingredient) == True
    assert water_ingredient.__eq__(cheese_ingredient) == False
    assert water_ingredient.__repr__() == "Ingredient('água')"
    assert len(cheese_ingredient.restrictions) == 2
