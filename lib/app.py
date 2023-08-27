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





# # Creating customer and restaurant instances
# customer1 = Customer("Alice", "Johnson")
# customer2 = Customer("Bob", "Smith")
# restaurant1 = Restaurant("Delicious Bites")

# # Creating review instances
# review1 = Review(customer1, restaurant1, 4)
# review2 = Review(customer2, restaurant1, 5)

# # Associating reviews with the restaurant
# restaurant1.add_review(review1)
# restaurant1.add_review(review2)

# # Using the methods
# restaurant_reviews = restaurant1.reviews()
# restaurant_customers = restaurant1.customers()

# print(f"Reviews for {restaurant1.name}:")
# for review in restaurant_reviews:
#     print(f"Rating: {review.review_rating}, Customer: {review.review_customer.full_name()}")

# print(f"Customers who reviewed {restaurant1.name}:")
# for customer in restaurant_customers:
#     print(f"{review.review_customer.full_name()}")

# # Getting all restaurant instances
# all_restaurants = Restaurant.all()
# for restaurant in all_restaurants:
#     print(f"Restaurant: {restaurant.name}")


# # Creating customer and restaurant instances
# customer1 = Customer("Alice", "Johnson")
# restaurant1 = Restaurant("Delicious Bites")
# restaurant2 = Restaurant("Pizza Palace")

# # Adding reviews
# customer1.add_review(restaurant1, 4)
# customer1.add_review(restaurant2, 5)

# # Using the methods
# reviewed_restaurants = customer1.restaurants()

# print(f"{customer1.full_name()} has reviewed the following restaurants:")
# for restaurant in reviewed_restaurants:
#     print(restaurant.name)

# # Getting all customer instances
# all_customers = Customer.all()
# for customer in all_customers:
#     print(f"Customer: {customer.full_name()}")


# # Creating customer instances
# customer1 = Customer("Alice", "Johnson")
# customer2 = Customer("Bob", "Smith")
# customer3 = Customer("Alice", "Doe")

# # Creating restaurant instances
# restaurant1 = Restaurant("Delicious Bites")

# # Adding reviews
# customer1.add_review(restaurant1, 4)
# customer1.add_review(restaurant1, 5)
# customer2.add_review(restaurant1, 3)
# customer3.add_review(restaurant1, 4)

# # Using the methods
# print(f"Total reviews by {customer1.full_name()}: {customer1.num_reviews()}")

# found_customer = Customer.find_by_name("Bob Smith")
# if found_customer:
#     print(f"Found customer: {found_customer.full_name()}")
# else:
#     print("Customer not found")

# all_matching_customers = Customer.find_all_by_given_name("Alice")
# print("Customers with given name 'Alice':")
# for matching_customer in all_matching_customers:
#     print(matching_customer.full_name())

# # Getting all customer instances
# all_customers = Customer.all()
# for customer in all_customers:
#     print(f"Customer: {customer.full_name()}")


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
average_rating = restaurant1.average_star_rating()

print(f"Average star rating for {restaurant1.name}: {average_rating:.2f}")

# Getting all restaurant instances
all_restaurants = Restaurant.all()
for restaurant in all_restaurants:
    print(f"Restaurant: {restaurant.name}")