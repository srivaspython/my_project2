from Food.Samosa import Samosa

Samosa = Samosa("Large Pani-Puri", "Mumbai", 210, "Serves 1", "Sweet-Sour taste")
def test_Samosa_category():
    assert Samosa.category() == "It is a best snack item"

def test_Samosa_price():
    assert Samosa.price() == "It costs around $35"

 
