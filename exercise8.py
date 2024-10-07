cart = [
    {"item": "apple", "quantity": 3, "price_per_unit": 0.5},
    {"item": "banana", "quantity": 6, "price_per_unit": 0.2},
    {"item": "orange", "quantity": 4, "price_per_unit": 0.3},
    {"item": "pear", "quantity": 2, "price_per_unit": 0.4}
]

# 1. Print the details of all items in the cart.
for item in cart:
    print(f'Item: {item["item"]}, Quantity: {item["quantity"]}, Price (per unit): ${item["price_per_unit"]:.2f}')

  
print("============================== Second ========================")

# 2. Calculate and print the total cost of the cart. 

def CartTotalValue():
  total_value = 0
  
  for f in cart:
    total_value += f["quantity"] * f["price_per_unit"]
    
  return total_value

print(f"${CartTotalValue()}")

# 3. Add a new item "grape" with quantity 5 and price per unit 0.6 to the cart.

cart.append({"item": "grape", "quantity": 5, "price_per_unit": 0.6})


# 4. Update the quantity of "banana" to 10 and print the updated cart. 

for i in cart:
  if i["item"] == "banana":
    i["quantity"] = 10
    break

print("============================== Fifth ========================")

# 5. Remove "pear" from the cart and print the updated cart. 

for i in range(len(cart)):
  if cart[i]["item"] == "pear":
    cart.pop(i)
    break
  
  
print(cart)
