weather = { 
 "Monday": {"temperature": 20, "humidity": 60},  
 "Tuesday": {"temperature": 22, "humidity": 55},  
 "Wednesday": {"temperature": 19, "humidity": 65},  
 "Thursday": {"temperature": 23, "humidity": 50},  
 "Friday": {"temperature": 21, "humidity": 70} 
 }

# 1. Print the weather details for each day. 
for title, details in weather.items():
    temp = details["temperature"]
    humidity = details["humidity"]
    print(f"WeekDay: {title}\nTemperature: {temp}\nHumidity: {humidity}\n")

# 2. Find and print the day with the highest temperature. 

print("=================== Second ===================")

def highestTemp():
  highest_value = 0
  day = ""
  
  for title, details in weather.items():
    if details["temperature"] > highest_value:
      highest_value = details["temperature"]
      day = title
      
  return day

print(highestTemp())

  


# 3. Find and print the day with the lowest humidity. 

print("=================== Third ===================")

def lowestHum():
  lowest_value = 999999999999999
  day = ""
  
  for title, details in weather.items():
    if details["humidity"] < lowest_value:
      lowest_value = details["humidity"]
      day = title
      
  return day

print(lowestHum())


print("=================== Fourth ===================")

# 4. Update the temperature of "Wednesday" to 25 and print the updated weather data. 

weather["Wednesday"]["temperature"] = 25

print(weather["Wednesday"])

print("=================== Fifth ===================")

# 5. Add weather data for "Saturday" with temperature 24 and humidity 60 to the dictionary and print the updated weather data. 

weather["Saturday"] =  {"temperature": 24, "humidity": 60}

print(weather)