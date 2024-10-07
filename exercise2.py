inventory = { 
 "apple": (50, 0.5), 
 "banana": (100, 0.2), 
 "orange": (75, 0.3), 
 "pear": (20, 0.4) 
}

# 1. Print the current inventory in a user-friendly format. 

for i in inventory.keys():
  print(f"{i.capitalize()}s")
  print(f"Ammount (In-stock): {inventory[i][0]}")
  print(f"Price: ${inventory[i][1]}/each")
  print()
  


# 2. Calculate and print the total value of the inventory. 

print("============================ Second =======================")

def totalInventoryValue(): 
  total = 0;
  
  for i in inventory.keys():
    crrntItem = inventory[i]
    
    total += (crrntItem[0] * crrntItem[1])
    
  return total

print(totalInventoryValue())

print("============================ Third =======================")

# 3. Add a new product "mango" with 30 items priced at $0.6 each to the inventory. 

inventory["mango"] = (30, 0.6)

# Not requested but I added just to show
print(inventory)


print("============================ Fourth =======================")

# 4. Update the quantity of "banana" to 120 and print the updated inventory. 

inventory["banana"] = (120, 0.2)

print(inventory)

print("============================ Fifth =======================")

# 5. Remove "pear" from the inventory and print the updated inventory. 

inventory.pop('pear', None)

print(inventory)
