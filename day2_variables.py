# Variables store kar rahe hain
item_name = "Laptop"
item_price = 120000   # price in PKR
item_quantity = 2
discount_percentage = 10

# Total price without discount
total_price = item_price * item_quantity

# Discount amount
discount_amount = total_price * (discount_percentage / 100)

# Final price after discount
final_price = total_price - discount_amount

# Output
print("Item:", item_name)
print("Price per item:", item_price)
print("Quantity:", item_quantity)
print("Total Price:", total_price)
print("Discount:", discount_amount)
print("Final Price to Pay:", final_price)
