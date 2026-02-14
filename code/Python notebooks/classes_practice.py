class Product:
    high_price_threshold = 25
    low_price_threshold = 10

    def __init__(self, origin, quantity, price):
        self.origin = origin
        self.quantity = quantity
        self.price = price

    def display_origin(self):
        print(f"This product is from {self.origin}")

    def display_quantity(self):
        print(f"Available quantity: {self.quantity} units")

    def display_price(self):
        print(f"Unit price: {self.price} credits")

    def calculate_total(self):
        total = self.price * self.quantity
        print(f"Total price: {total} credits")

    def check_price_level(self):
        if self.price == self.high_price_threshold:
            print(f"Price alert: {self.origin} product at maximum threshold")
        elif self.price == self.low_price_threshold:
            print(f"Price alert: {self.origin} product at minimum - opportunity to buy")
        else:
            print("Price within normal range")

    def convert_to_sar(self):
        sar_rate = 10
        price_in_sar = self.price * sar_rate
        total_in_sar = price_in_sar * self.quantity
        print(f"Unit price in SAR: {price_in_sar}\nTotal price in SAR: {total_in_sar}")

    def apply_bulk_discount(self):
        discount_rate = 0.5
        discounted_price = self.price * discount_rate
        total_discounted = discounted_price * self.quantity
        print(
            f"Discounted unit price: {discounted_price}\nTotal with discount: {total_discounted}"
        )

    def calculate_with_tax(self):
        tax_rate = 1.8  # 180% tax
        price_with_tax = self.price * (1 + tax_rate)
        total_with_tax = price_with_tax * self.quantity
        print(
            f"Unit price with tax: {price_with_tax}\nTotal with tax: {total_with_tax}"
        )


# Example usage
product = Product("Regional Farm", 5000, 10)

product.display_origin()
product.display_quantity()
product.display_price()
product.check_price_level()
product.calculate_total()
product.convert_to_sar()
product.calculate_with_tax()
