from Food.Biryani import Biryani

biryani = Biryani("Chicken Biryani", "Guntur", 560, "Serves 2", "Golden-Orange")


def test_biryani_category():
    assert biryani.category() == "It is a rice-dish"

def test_biryani_price():
    assert biryani.price() == "It costs around $18"

