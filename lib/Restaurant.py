class Restaurant:
    all_restaurants = []

    def __init__(self, name):
        self.name = name
        self.review_list = []  # Renamed the attribute to avoid conflict
        self.__class__.all_restaurants.append(self)

    def add_review(self, review):
        self.review_list.append(review)  # Update the attribute name here

    def reviews(self):
        return self.review_list  # Update the attribute name here

    def customers(self):
        reviewed_customers = set()
        for review in self.review_list:
            reviewed_customers.add(review)
        return list(reviewed_customers)

    @classmethod
    def all(cls):
        return cls.all_restaurants
