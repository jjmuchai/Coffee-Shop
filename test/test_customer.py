import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_customer_name_valid():
    c = Customer("Alice")
    assert c.name == "Alice"

def test_customer_name_invalid():
    with pytest.raises(ValueError):
        Customer("")
    with pytest.raises(ValueError):
        Customer("ThisNameIsWayTooLongToBeValid")

def test_create_order():
    c = Customer("Bob")
    coffee = Coffee("Latte")
    order = c.create_order(coffee, 4.5)
    assert order in Order.all_orders
    assert order.customer == c
    assert order.coffee == coffee

def test_most_aficionado():
    c1 = Customer("Tom")
    c2 = Customer("Jerry")
    coffee = Coffee("Espresso")
    c1.create_order(coffee, 4.0)
    c2.create_order(coffee, 5.0)
    c2.create_order(coffee, 4.0)
    assert Customer.most_aficionado(coffee) == c2