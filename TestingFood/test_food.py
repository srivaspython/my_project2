from Food.food import Food

def test_food_is_abstract():
    try:
        Food("VadaPav", "famous_place", 202, "Serves 1 ")
    except TypeError as e:
        assert "Can't instantiate abstract class Food" in str(e)