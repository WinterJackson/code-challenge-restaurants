class Review:
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        self.review_customer = customer
        self.review_restaurant = restaurant
        self.review_rating = rating
        self.__class__.all_reviews.append(self)

    def get_customer(self):
        return self.review_customer

    def get_restaurant(self):
        return self.review_restaurant

    def get_rating(self):
        return self.review_rating

    @classmethod
    def all(cls):
        return cls.all_reviews
