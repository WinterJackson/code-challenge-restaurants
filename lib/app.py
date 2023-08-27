from Customer import Customer
from Restaurant import Restaurant
from Review import Review


# # Creating customer instances
# customer1 = Customer("Alice", "Johnson")
# customer2 = Customer("Bob", "Smith")

# # Using the methods
# print(customer1.given_name)        
# print(customer2.family_name)       
# print(customer1.full_name())       

# # Getting all customer instances
# all_customers = Customer.all()
# for customer in all_customers:
#     print(customer.full_name())


# # Creating restaurant instances
# restaurant1 = Restaurant("Delicious Bites")
# restaurant2 = Restaurant("Pizza Palace")

# # Using the methods
# print(restaurant1.name)   

# # Getting all restaurant instances
# all_restaurants = Restaurant.all()
# for restaurant in all_restaurants:
#     print(restaurant.name)


# # Creating customer and restaurant instances
# customer1 = Customer("Alice", "Johnson")
# restaurant1 = Restaurant("Delicious Bites")

# # Creating review instances
# review1 = Review(customer1, restaurant1, 4)
# review2 = Review(customer1, restaurant1, 5)

# # Using the methods
# review_customer = review1.get_customer()
# review_restaurant = review1.get_restaurant()

# print(f"Review by: {review_customer.full_name()}")
# print(f"Review for: {review_restaurant.name}")

# # Getting all review instances
# all_reviews = Review.all()
# for review in all_reviews:
#     print(f"Customer: {review.get_customer().full_name()}, Rating: {review.get_rating()}")





# Creating customer and restaurant instances
customer1 = Customer("Alice", "Johnson")
customer2 = Customer("Bob", "Smith")
restaurant1 = Restaurant("Delicious Bites")

# Creating review instances
review1 = Review(customer1, restaurant1, 4)
review2 = Review(customer2, restaurant1, 5)

# Associating reviews with the restaurant
restaurant1.add_review(review1)
restaurant1.add_review(review2)

# Using the methods
restaurant_reviews = restaurant1.reviews()
restaurant_customers = restaurant1.customers()

print(f"Reviews for {restaurant1.name}:")
for review in restaurant_reviews:
    print(f"Rating: {review.review_rating}, Customer: {review.review_customer.full_name()}")

print(f"Customers who reviewed {restaurant1.name}:")
for customer in restaurant_customers:
    print(f"{review.review_customer.full_name()}")

# Getting all restaurant instances
all_restaurants = Restaurant.all()
for restaurant in all_restaurants:
    print(f"Restaurant: {restaurant.name}")