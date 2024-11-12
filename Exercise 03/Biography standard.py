#Exercise 03 - Biography
"""In this exercise, you’ll create a program that stores and prints your name, home-
town, and age to the console using a Python dictionary.

Steps:
1. Store the information (name, hometown, and age) as key-value pairs in a
dictionary.
2. Print the values on separate lines using a single print() statement.
3. Use variables with appropriate data types for each piece of information."""


#Answer:

#Storing the information (name,hometown,and age) as key value pairs in a dictionary.
user_info = {
    "name" : "Fathima Haifa",
    "hometown" : "kasaragod",
    "age" : 18
}

#The values are printed on separate lines using a single print() statement.
print(f"Name : {user_info['name']}\nHometown : {user_info['hometown']}\nAge : {user_info['age']}")