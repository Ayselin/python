class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.served_customers = 0
       

    def describe_restaurant(self):
        print(f"{self.restaurant_name} is {self.cuisine_type} restaurant!")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open")

    def set_number_served(self, served_customers):
        self.served_customers = served_customers

    def increment_number_served(self,additional_customers):
        self.served_customers += additional_customers

   



restaurant = Restaurant('The Best', 'delicious')


restaurant.served_customers = 20
print(f"{restaurant.served_customers} customers were served today")


restaurant.increment_number_served(80)
print(f"{restaurant.served_customers} customers were served yesterday")


# print(f"{restaurant.restaurant_name} served {restaurant.number_served} customers on Monday")
# print(restaurant.restaurant_name)
# print(restaurant.cuisine_type)



# restaurant.describe_restaurant()
# restaurant.open_restaurant()


