#Advanced Requirements for the Exercise 03 - Biography
"""Have the user input their name, hometown, and age instead of hardcoding the
values. Try giving both your first and second name when asked for your name.
What happens? How can you handle multiple words in Python? Test the
program by entering a string value for age (e.g., “twenty”). What happens?
How can you prevent this issue?"""


#Answer:

#Starting with an empty dictionary for storing the information about user.
user_info = {}

#Asking the user to enter their personal information(name,hometown,and age), the store it in the dictionary.
user_info["name"] = input("Enter your name:")
user_info["hometown"] = input("Enter your hometown:")

#Confirming the age input as a valid integer.
while True:
    user_age = input("Enter your age:")
    #Converting age input to an integer type.
    try:
        user_info["age"] = int(user_age)
        break
    except ValueError:
        print("Age input is invalid.Please enter an integer.")

#Printing each item of user information from the dictionary.
print("\nUser Information:")
for key, value in user_info.items():
    print(f"{key.capitalize()}:{value}")

