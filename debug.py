from customer import Customer
from coffee import Coffee
from order import Order

# Sample session
c1 = Customer("Max")
c2 = Customer("Sue")
cappuccino = Coffee("Cappuccino")
latte = Coffee("Latte")

c1.create_order(cappuccino, 5.5)
c2.create_order(cappuccino, 6.0)
c1.create_order(latte, 4.0)

print("C1 Coffees:", [c.name for c in c1.coffees()])
print("Latte orders:", latte.num_orders())
print("Latte avg price:", latte.average_price())
print("Most Aficionado (Cappuccino):", Customer.most_aficionado(cappuccino).name)