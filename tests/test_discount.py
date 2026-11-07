import unittest
from aims.cart import Cart 


class TestDiscount(unittest.TestCase):
    
    def setUp(self):
        
        self.cart = Cart()

    def test_calculate_discount_valid(self):
        result = self.cart.calculate_discount(100, 20)
        self.assertEqual(result, 80)

    def test_calculate_discount_invalid_percent(self):
        
        with self.assertRaises(ValueError):
            self.cart.calculate_discount(100, 150)


if __name__ == "__main__":
    unittest.main()