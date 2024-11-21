#Loops - Pizza Toppings:
"""Write a loop that prompts the user to enter a series of pizza toppings until they enter a
'quit' value. As they enter each topping,
Print a message saying you’ll add that topping to their pizza."""

#Answers:
#Loop through the selected pizza toppings
while True:
    #Asking the user to input a pizza topping
    pizza_topping = input("What topping would you like to add to your pizza?(Please type 'quit' to stop): ")

    #Verifying if the user entere a 'quit'
    if pizza_topping.lower() == 'quit':
        print("All toppings have been selected!")
        break
    else:
        print(f"{pizza_topping} is now part of your pizza!")
