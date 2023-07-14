class HotDrink(Product):
    def __init__(self, name, price, temperature):
        super().__init__(name, price)
        self.temperature = temperature

    def __str__(self):
        return f"HotDrink{{name='{self.get_name()}', price={self.get_price()}, temperature={self.temperature}}}"


class PromotionalClient:
    promotion_name = "Summer Sale"
    client_id = 0
    participants_count = 0

    def __init__(self, client_id):
        self.client_id = client_id

    def participate_in_promotion(self):
        self.participants_count += 1


class VendingMachine:
    products = []

    def add_product(self, product):
        self.products.append(product)

    def get_product(self, index):
        return self.products[index]


class iReturnOrder:
    def return_order(self, order_id):
        pass

    def check_return_eligibility(self, order_id):
        pass


def main():
    vending_machine = VendingMachine()

    tea = HotDrink("Tea", 1.5, 80)
    coffee = HotDrink("Coffee", 2.0, 90)

    vending_machine.add_product(tea)
    vending_machine.add_product(coffee)

    print(vending_machine.get_product(0))
    print(vending_machine.get_product(1))

if __name__ == "__main__":
    main()