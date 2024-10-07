movies = { 
 "Inception": {"year": 2010, "rating": 8.8, "genre": "Sci Fi"}, 
 "The Godfather": {"year": 1972, "rating": 9.2, "genre": "Crime"}, 
 "The Dark Knight": {"year": 2008, "rating": 9.0, "genre": "Action"}, 
 "Pulp Fiction": {"year": 1994, "rating": 8.9, "genre": "Crime"}, 
 "Forrest Gump": {"year": 1994, "rating": 8.8, "genre": "Drama"} 
} 





# 1. Print the details of all movies in a user-friendly format. 

for title, details in movies.items():
    rating = details["rating"]
    genre = details["genre"]
    year = details["year"]
    print(f"Title: {title}\nGenre: {genre}\nRating: {rating}\nYear: {year}\n")
    
# 2. Find and print the highest-rated movie. 

print("========================== Second =================")

def high():
  high = 0
  movie = ""
  for title, details  in movies.items():
    if(details["rating"] > high):
      high = details["rating"]
      movie = title
      
  return movie

print(high())


# 3. Add a new movie "The Matrix" with year 1999, rating 8.7, and genre "Sci-Fi" to the database. 

print("========================== Third =================")


movies["The Matrix"] = {"year": 1999, "rating": 8.7, "genre": "Sci-Fi"}

print(movies["The Matrix"])

# 4. Update the rating of "Inception" to 9.0 and print the updated details.

print("========================== Fourth =================")
 

movies["Inception"]["rating"] = 9.0

print(movies["Inception"])

# 5. Remove "Pulp Fiction" from the database and print the updated list. 

print("========================== Fifth =================")


movies.pop("Pulp Fiction", None)

print(movies)



