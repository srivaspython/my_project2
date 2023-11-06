from Food.food import Food

class Biryani(Food):
    def __init__(self, item, famous_place, calories, quantity, color):
        super().__init__(item, famous_place, calories, quantity)
        self.color = color

    def category(self):
         return f"It is a rice-dish"

    def price(self):
         return f"It costs around $18"