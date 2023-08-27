import unittest
import sys
sys.path.append('..') 
from lib.Restaurant import Restaurant
from lib.Review import Review
from lib.Customer import Customer

class TestRestaurant(unittest.TestCase):
    def setUp(self):
        self.restaurant = Restaurant("Burger Place")
        self.customer = Customer("John", "Doe")

    def test_init(self):
        self.assertEqual(self.restaurant.name, "Burger Place")
        self.assertEqual(self.restaurant.review_list, [])
        self.assertIn(self.restaurant, Restaurant.all())

    def test_add_review(self):
        review = Review(self.customer, self.restaurant, 4)
        self.restaurant.add_review(review)
        self.assertEqual(len(self.restaurant.review_list), 1)

    def test_reviews(self):
        review = Review(self.customer, self.restaurant, 4)
        self.restaurant.add_review(review)
        self.assertEqual(self.restaurant.reviews(), [review])

    def test_customers(self):
        review = Review(self.customer, self.restaurant, 4)
        self.restaurant.add_review(review)
        self.assertEqual(self.restaurant.customers(), [review.get_customer()])

    def test_average_star_rating(self):
        review1 = Review(self.customer, self.restaurant, 4)
        review2 = Review(self.customer, self.restaurant, 5)
        self.restaurant.add_review(review1)
        self.restaurant.add_review(review2)
        self.assertEqual(self.restaurant.average_star_rating(), 4.5)

    def test_all(self):
        all_restaurants = Restaurant.all()
        self.assertIn(self.restaurant, all_restaurants)

if __name__ == '__main__':
    unittest.main()
