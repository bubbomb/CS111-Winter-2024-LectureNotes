# Define a new type of data
class Chocolate:

    name = 'Seth bar'
    scratch = 'Seth'
    price = 100.00
    nutrition_info = ''
    inventory = 0
    # Set the initial values
    def __init__(self, name, price, nutrition_info):
        self.name = name
        self.price = price
        self.nutrition_info = nutrition_info

    # Define methods
    def increase_inventory(self, amount):
        self.inventory += amount

    def reduce_inventory(self, amount):
        self.inventory -= amount

    def get_label(self):
        return "Foxolate Shop: " + self.name

    def get_inventory_report(self):
        if self.inventory == 0:
            return "There are no bars!"
        return f"There are {self.inventory} bars."

    def purchase(self):
        pass


    # def get_total_price(self, quantity):
    #     return (self.price * (1 + self.sales_tax)) * quantity

    # sales_tax = 0.07

pina_bar = Chocolate("Piña Chocolotta", 7.99,
    ["200 calories", "24 g sugar"])
truffle_bar = Chocolate("Truffalapagus", 9.99,
    ["170 calories", "19 g sugar"])

print(pina_bar.get_label())
print(truffle_bar.get_label())

pina_bar.scratch = 'Seth'

print(getattr(pina_bar, 'scratch'))
all_chocolates = [pina_bar, truffle_bar]

for chocolate in all_chocolates:
    chocolate.get_label()
# print(pina_bar.sales_tax)
# print(truffle_bar.sales_tax)
# print(pina_bar.get_total_price(4))
# print(truffle_bar.get_total_price(4))

