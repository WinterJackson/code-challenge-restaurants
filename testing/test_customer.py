import unittest
import sys
sys.path.append('..') 
from lib.Customer import Customer
from lib.Restaurant import Restaurant
from lib.Review import Review


class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("John", "Doe")
        self.restaurant = Restaurant("Burger Place")

    def test_init(self):
        self.assertEqual(self.customer.given_name, "John")
        self.assertEqual(self.customer.family_name, "Doe")
        self.assertEqual(self.customer.reviews, [])
        self.assertIn(self.customer, Customer.all())

    def test_given_name_method(self):
        self.assertEqual(self.customer.get_family_name(), "Doe")  # Rename method

    def test_family_name(self):
        self.assertEqual(self.customer.family_name(), "Doe")

    def test_full_name(self):
        self.assertEqual(self.customer.full_name(), "John Doe")

    def test_restaurants(self):
        self.customer.add_review(self.restaurant, 4)
        self.assertEqual(self.customer.restaurants(), [self.restaurant])

    def test_add_review(self):
        self.customer.add_review(self.restaurant, 4)
        self.assertEqual(len(self.customer.reviews), 1)
        self.assertEqual(len(self.restaurant.review_list), 1)

    def test_num_reviews(self):
        self.customer.add_review(self.restaurant, 4)
        self.assertEqual(self.customer.num_reviews(), 1)

    def test_find_by_name(self):
        found_customer = Customer.find_by_name("John Doe")
        self.assertEqual(found_customer, self.customer)

    def test_find_all_by_given_name(self):
        matching_customers = Customer.find_all_by_given_name("John")
        self.assertEqual(matching_customers, [self.customer])

    def test_all(self):
        all_customers = Customer.all()
        self.assertIn(self.customer, all_customers)

if __name__ == '__main__':
    unittest.main()
