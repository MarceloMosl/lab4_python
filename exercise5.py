cities = { 
 "New York": 8419000, 
 "Los Angeles": 3980000, 
 "Chicago": 2716000, 
 "Houston": 2328000, 
 "Phoenix": 1690000 
} 

# 1. Print the population of each city in a user-friendly format. 2. Find and print the city with the highest population.

for i in cities.keys():
  print(f"{i} - Population {cities[i]:,}")
  
  


# 2. Find and print the city with the highest population.

print("======================= Second ================")


def highest():
  high = 0
  
  city = ""
  
  for i in cities.keys():
    if high < cities[i]:
      high = cities[i]
      city = i

  return city


print(highest())



# 3. Find and print the city with the lowest population. 

print("======================= Third ================")

def lowest():
  lowest = 9999999999
  
  city = ""
  
  for i in cities.keys():
    if lowest > cities[i]:
      lowest = cities[i]
      city = i

  return city

print(lowest())

# 4. Update the population of "Phoenix" to 1700000 and print the updated data. 

print("======================= Fourth ================")

cities["Phoenix"] = 1700000

print(cities)


# 5. Add a new city "San Francisco" with a population of 884000 and print the updated data. 

print("======================= Fifth ================")

cities["San Francisco"] = 884000

print(cities)
