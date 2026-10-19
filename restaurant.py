class Restaurant:
    def __init__(self,restaurant_name,cuisine_type,customer_served=0):
           self.name=restaurant_name
           self.cuisine=cuisine_type
           self.cus_served=customer_served

    def describe_restaurant(self):
          print(f"Welcome to {self.name}.We here serve the {self.cuisine} cuisine.")

    def open_restaurant(self):
          print("Restaurant is open!")        

    def set_customer_served(self,num_customers):  
              self.cus_served+=num_customers

restaurant=Restaurant("Les Deux","classic French")
restaurant.open_restaurant()
restaurant.describe_restaurant()
restaurant.set_customer_served(10)
print(restaurant.cus_served)