#Exercise 10 - Is it even?
"""Write a program that tests if a value is even or odd. Follow the instructions
outlined below:
Instructions:
• The program should ask the user for a number from within the main
function.
• The entered number should be passed to a function that determines if the
value is even or odd.
• The function should return a message indicating whether the number is
even or odd.
• The message returned by the function should be printed from within the
main function."""

#Answers:

#Checking the number is even or odd by defining a function.
def check_even_odd():
     
#Gets a number from the user.
     Number = int(input("Please input a number: "))

     #Determine if the number is even or odd & display the result
     if Number % 2 == 0:
         print(f"The number which you entered is even")
     else:
          print(f"The number which you entered is odd")

 #Directly call the function
check_even_odd()

