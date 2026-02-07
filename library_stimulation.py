# Build a system that:
# Stores books (ID, name, author, availability)
# Issues and returns books
# Displays available books
import array as ar
library = {
    "book1" : {
    "ID" : "1",
    "name": "b1",
    "author": "auth1",
    "available": True,
    },
    "book2" : {
    "ID" : "2",
    "name" : "b2",
    "author" : "auth2",
    "available" : True,
    },
    "book3" : {
    "ID" : "3",
    "name" : "b3",
    "author" : "auth3",
    "available" : True,
    },
    "book4" : {
    "ID" : "4",
    "name" : "b4",
    "author" : "auth4",
    "available" : True,
    }
}
library_copy = library.copy()
print(library_copy.items())
lib = list(library_copy.items())
Purpose = input("Enter issue/return:")
if Purpose == "issue" :  
  issued_book = input("Enter book ID to issue:" )
elif Purpose == "return":
  returned_book = input("Enter book ID to return:") 
  for y in library_copy.keys():
   if library[y]["ID"] == returned_book:
      library[y]["available"] = True
else:
   print("INVALID INPUT")
for x in library.keys():
   if library[x]["ID"] == issued_book:
      library[x]["available"] = False
def available_books():
    for z in library.keys():
        if library[z]["available"] == True:
         print(library[z]["name"])
available_books()





















