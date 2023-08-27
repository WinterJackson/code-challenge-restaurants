import unittest
import sys
sys.path.append('..') 
from lib.Review import Review
from lib.Customer import Customer
from lib.Restaurant import Restaurant

class TestReview(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("John", "Doe")
        self.restaurant = Restaurant("Burger Place")
        self.review = Review(self.customer, self.restaurant, 4)

    def test_init(self):
        self.assertEqual(self.review.review_customer, self.customer)
        self.assertEqual(self.review.review_restaurant, self.restaurant)
        self.assertEqual(self.review.review_rating, 4)
        self.assertIn(self.review, Review.all())

    def test_get_customer(self):
        self.assertEqual(self.review.get_customer(), self.customer)

    def test_get_restaurant(self):
        self.assertEqual(self.review.get_restaurant(), self.restaurant)

    def test_get_rating(self):
        self.assertEqual(self.review.get_rating(), 4)

    def test_all(self):
        all_reviews = Review.all()
        self.assertIn(self.review, all_reviews)

if __name__ == '__main__':
    unittest.main()
