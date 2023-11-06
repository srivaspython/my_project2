from Food.Biryani import Biryani
from Food.Samosa import Samosa
from Food.Pizza import Pizza

biryani = Biryani("Chicken Biryani", "Guntur", 560, "Serves 2", "Golden-Orange")
Pizza =  Pizza("pizza", "Hyderabad", 720, "Serves 2", "Texture is crucial")
Samosa = Samosa("Large Samosa", "Mumbai", 210, "Serves 1", "Spicy taste")


print(biryani.category())
print(Pizza.category())
print(Samosa.category())
print(biryani.price())
print(Pizza.price())
print(Samosa.price())
