countries = { 
 "USA": "Washington, D.C.", 
 "Canada": "Ottawa", 
 "France": "Paris", 
 "Germany": "Berlin", 
 "Japan": "Tokyo" 
} 

# 1. Print the names of all countries and their capitals. 

for i in countries.keys():
  print(f"{i} - Capital: {countries[i]}")

# 2. Find and print the capital of Germany. 

print("\n========================== Second ====================")

for i in countries.keys():
  if(i == "Germany"):
    print(countries[i])
    break

# 3. Add a new country "Australia" with capital "Canberra" to the dictionary and print the updated dictionary. 
print("\n========================== Third ====================")

countries["Australia"] = "Canberra"

print(countries)
# 4. Update the capital of "USA" to "New Washington" and print the updated dictionary. 
print("\n========================== Fourth ====================")

countries["USA"] = "New Washington"

print(countries)

# 5. Remove "France" from the dictionary and print the updated dictionary. 
print("\n========================== Fifth ====================")

countries.pop("France", None)

print(countries)