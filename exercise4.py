from array import *

library = { 
 "978-3-16-148410-0": {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "year": 1951},
 "978-0-14-028329-7": {"title": "1984", "author": "George Orwell", "year": 1949}, 
 "978-0-7432-7356-5": {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960}, 
 "978-0-452-28423-4": {"title": "Brave New World", "author": "Aldous Huxley", "year": 1932} 
} 

# 1. Print the details of all books in a user-friendly format. 

for _, details in library.items():
    title = details["title"]
    author = details["author"]
    year = details["year"]
    print(f"Title: {title}, Author: {author}, Year: {year}")
    
    
print("========================== Second ============================")

# 2. Find and print the details of the book with the ISBN "978-0-14-028329-7". 

print(library["978-0-14-028329-7"])

print("========================== Third ============================")

# 3. Add a new book with ISBN "978-1-4028-9462-6", title "The Great Gatsby", author "F. Scott Fitzgerald", and year 1925. 

library["978-1-4028-9462-6"] = {'title': "The Great Gatsby", 'author': "F. Scott Fitzgerald", 'year': 1925}



print("========================== Fourth ============================")


#  Update the year of "To Kill a Mockingbird" to 1961 and print the updated details. 

for i in library.keys():
  if(library[i]["title"] == "To Kill a Mockingbird"):
      library[i]["year"] = 1961
      break

print(library)

print("========================== Fifth ============================")



# 5. Remove the book with ISBN "978-0-452-28423-4" and print the updated library. 

library.pop("978-0-452-28423-4", None)

print(library)
