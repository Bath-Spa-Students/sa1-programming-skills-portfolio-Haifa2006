#Advanced requirements for the Exercise 05 - Days of the Month
"""Leap Year Adjustment: Modify the program to account for leap years. For
February, ask the user if the year is a leap year and adjust the number of days
accordingly."""


#Answer:

##Creating a dictionary, assosciating each month with its total number of days.
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
month_number = int(input("Type your month number:"))
calendar_year = int(input("Type the year:"))

#Asking the user if the year is a leap year and modifying February's day count.
if month_number == 2:
    leap_year = input(f"{calendar_year} is a leap year?")
    if leap_year == "yes":

        #In a leap year the month of February has 29 days .
        print(f"The no. of days in month {month_number} of year {calendar_year} is 29 a leap year.")
    else:
        #In a non-leap year the month of February has 28 days.
        print(f"The no.of days in month {month_number} of year {calendar_year} is 28.")
else:
#The months other than February will be directly outputting the number of days.
  if 1 <= month_number <= 12: 
      print(f"The no. of days in month {month_number} of year {calendar_year} is {Number_of_days[month_number]}")

  else:
      print("Invalid month number!")