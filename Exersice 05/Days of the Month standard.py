#Exercise 05 - Days of the Month
"""Write a program that tells a user how many days there are in a specific month.
Use a dictionary to map the month numbers (1-12) to the number of days in
each month.
Instructions:

1. Create a Dictionary: Define a dictionary where the keys are month num-
bers and the values are the number of days in those months.

2. Input Handling: Ask the user to input the month number.
3. Check and Output: Use an if-else statement to check if the input is valid
and print the number of days in the corresponding month."""


#Answer:

#Creating a dictionary, assosciating each month with its total number of days.
Number_of_days = {
    #Month of January
    1:31,
    #Month of February
    2:28,
    #Month of March
    3:31,
    #Month of April
    4:30,
    #Month of May
    5:31,
    #Month of June
    6:30,
    #Month of July
    7:31,
    #Month of August 
    8:31,
    #Month of September
    9:30,
    #Month of October
    10:31,
    #Month of November
    11:30,
    #Month of December
    12:31,

}


#Asking the user to enter the month number.
month_number = int(input("Type the month number:"))

#Checking the month and printing the numbers of days.
if 1 <= month_number <= 12:
    print(f"The number of days in month {month_number} is {Number_of_days[month_number]}")
else:
    print("Invalid month number!")
