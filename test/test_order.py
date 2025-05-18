import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_valid_order():
    customer = Customer("Leo")
    coffee = Coffee("Flat White")
    order = Order(customer, coffee, 3.5)
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 3.5

def test_invalid_price():
    customer = Customer("Ann")
    coffee = Coffee("Macchiato")
    with pytest.raises(ValueError):
        Order(customer, coffee, 0.5)

    with pytest.raises(ValueError):
        Order(customer, coffee, 11.0)

def test_invalid_types():
    with pytest.raises(TypeError):
        Order("not a customer", Coffee("Americano"), 4.0)
    with pytest.raises(TypeError):
        Order(Customer("Rob"), "not a coffee", 4.0)