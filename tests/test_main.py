import pytest

def calculate_discounted_prices(product_names, prices):
    discounted_prices = [price * 0.85 for price in prices]
    return discounted_prices

def test_calculate_discounted_prices():
    product_names = ["Product A", "Product B", "Product C"]
    prices = [100, 200, 300]
    expected_discounted_prices = [85, 170, 255]
    assert calculate_discounted_prices(product_names, prices) == expected_discounted_prices

def test_calculate_discounted_prices_empty_lists():
    product_names = []
    prices = []
    expected_discounted_prices = []
    assert calculate_discounted_prices(product_names, prices) == expected_discounted_prices

def test_calculate_discounted_prices_negative_prices():
    product_names = ["Product A", "Product B", "Product C"]
    prices = [-100, -200, -300]
    expected_discounted_prices = [-85, -170, -255]
    assert calculate_discounted_prices(product_names, prices) == expected_discounted_prices
