class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __str__(self):
        return f"{self.name} - {self.price} руб."

class HotDrink(Product):
    def __init__(self, name, price, temperature):
        super().__init__(name, price)
        self.temperature = temperature
    
    def __str__(self):
        return f"{self.name} - {self.price} руб., температура: {self.temperature}°C"


coffee = HotDrink("Кофе", 100, 80)
tea = HotDrink("Чай", 50, 60)

print(coffee)
print(tea)