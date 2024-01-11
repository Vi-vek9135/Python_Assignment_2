
# Define a class 'Product' to represent individual products
class Product:
    def __init__(self, name, price, quantity, product_type):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.product_type = product_type
    
    def __str__(self):
        return f"{self.name}, {self.price} RS, {self.quantity}, {self.product_type}"



# Function to print the inventory list
def print_inventory(products):
    print("\nInventory List:")
    for product in products:
        print(product)
    print(f"Total number of products: {len(products)}")




# Function to add a new product to the inventory
def add_product(products, name, price, quantity, product_type):
    products.append(Product(name, price, quantity, product_type))






# Function to remove a product from the inventory by name
def remove_product(products, name):
    for product in products:
        if product.name == name:
            products.remove(product)
            break






# Function to get products of a specific type from the inventory
def get_products_by_type(products, product_type):
    matching_products = []
    for product in products:
        if product.product_type == product_type:
            matching_products.append(product)
    return matching_products








# Function to update the quantity of a product in the inventory
def update_quantity(products, name, quantity):
    for product in products:
        if product.name == name:
            product.quantity += quantity
            break







# Function to calculate the total payment for a list of items
def calculate_payment(products, items):
    total_payment = 0
    for item in items:
        for product in products:
            if product.name == item[0]:
                total_payment += product.price * item[1]
                break
    return round(total_payment)




# This is our Main Program where all the task have to perform

# Create an empty list to store products
products = []

# Prompt the user to enter product details until they enter 'done'
print("Enter product details in the format: Name, Price RS, Quantity, Type")
print("Enter 'done' to finish inputting products")

while True:
    product_input = input("Product: ")
    
    if product_input.lower() == "done":
        break


    # Split the input and extract product details
    product_details = product_input.split(", ")
    name = product_details[0]
    price = float(product_details[1].split(" ")[0])
    quantity = int(product_details[2])
    product_type = product_details[3]



    # Add the product to the inventory
    add_product(products, name, price, quantity, product_type)






# ------------------------------------------------------------------------------------------------ #

# Print all inventory list and total number of products
print_inventory(products)

# Add a new product
add_product(products, "Potato", 10.0, 50, "Root")
print_inventory(products)

# Get products of type 'Leafy green'
leafy_green_products = get_products_by_type(products, "Leafy green")
print("\nLeafy green products:")
for product in leafy_green_products:
    print(product)

# Remove Garlic from the inventory
remove_product(products, "garlic")
print_inventory(products)

# Update quantity of cabbages
update_quantity(products, "cabbage", 50)
cabbage_quantity = None
for product in products:
    if product.name == "cabbage":
        cabbage_quantity = product.quantity
        break
print(f"\nFinal quantity of cabbage: {cabbage_quantity}")

# Calculate payment for given items
items = [("lettuce", 1), ("zucchini", 2), ("broccoli", 1)]
total_payment = calculate_payment(products, items)
print(f"\nThe round figure that the user needs to pay: {total_payment} RS")
