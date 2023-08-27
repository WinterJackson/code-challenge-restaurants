class Restaurant:
    all_restaurants = []

    def __init__(self, name):
        self.name = name
        self.review_list = []  
        self.__class__.all_restaurants.append(self)

    def add_review(self, review):
        self.review_list.append(review)  

    def reviews(self):
        return self.review_list  

    def customers(self):
        reviewed_customers = set()
        for review in self.review_list:
            reviewed_customers.add(review)
        return list(reviewed_customers)
    
    def average_star_rating(self):
        if not self.review_list:
            return 0  
        total_rating = sum(review.get_rating() for review in self.review_list)
        average_rating = total_rating / len(self.review_list)
        return average_rating

    @classmethod
    def all(cls):
        return cls.all_restaurants
