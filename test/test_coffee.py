import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from coffee import Coffee
from customer import Customer

def test_coffee_name_valid():
    coffee = Coffee("Mocha")
    assert coffee.name == "Mocha"

def test_coffee_name_invalid():
    with pytest.raises(ValueError):
        Coffee("Aa")

def test_average_price():
    c = Customer("Jade")
    coffee = Coffee("Cappuccino")
    c.create_order(coffee, 5.0)
    c.create_order(coffee, 3.0)
    assert coffee.average_price() == 4.0