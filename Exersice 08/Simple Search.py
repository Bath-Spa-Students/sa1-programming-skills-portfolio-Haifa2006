#Exercise 08 - Simple Search
"""Write a program that searches for a specific string within a list of strings. The list
is initialized with specific names (“Jake” “Zac”, “Ian”, “Ron”, “Sam”, “Dave”).
, and your task is to search for “Sam”.
Optional Requirements:
1. Allow the user to input the search term instead of using a predefined value.
2. Implement the search functionality based on user input."""


#Answer:

#Defining a list of sample names
name_list = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

#Getiing a name to find from the user
name_to_find = input("Please type the name you wish to find: ")

#Verifying if the name entered is existing in the list
if name_to_find in name_list:
    print ("present")
else:
    print("not present")

