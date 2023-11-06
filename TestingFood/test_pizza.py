from Food.Pizza import Pizza


Pizza = Pizza("Pizza", "Hyderabad", 720, "Serves 2", "Texture is crucial")

def test_Pizza_category():
    assert Pizza.category() == "It is a Fast-food"

def test_Pizza_price():
    assert Pizza.price() == "It costs around $50"

 
