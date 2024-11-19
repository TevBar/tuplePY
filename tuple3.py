def process_customer_orders(orders):
    """
    Processes a list of customer orders and displays the details in a user-friendly format.

    Parameters:
        orders (list): A list of tuples, where each tuple contains (customer_name, product, quantity).
    """
    print("Customer Order Details:")
    print("-" * 30)
    for customer_name, product, quantity in orders:
        print(f"Customer: {customer_name}, Product: {product}, Quantity: {quantity}")

# Sample Order Data
orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    ("Charlie", "Smartphone", 3),
    ("Diana", "Headphones", 4)
]

# Process and display orders
process_customer_orders(orders)
