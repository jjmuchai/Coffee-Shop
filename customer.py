from order import Order

class Customer:
    all_customers = []

    def __init__(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
            Customer.all_customers.append(self)
        else:
            raise ValueError("Customer name must be a string between 1 and 15 characters.")

    @property
    def name(self):
        return self._name

    def orders(self):
        return [order for order in Order.all_orders if order.customer == self]

    def coffees(self):
        return list(set([order.coffee for order in self.orders()]))

    def create_order(self, coffee, price):
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        spender = None
        max_spent = 0
        for customer in cls.all_customers:
            total = sum([order.price for order in customer.orders() if order.coffee == coffee])
            if total > max_spent:
                max_spent = total
                spender = customer
        return spender