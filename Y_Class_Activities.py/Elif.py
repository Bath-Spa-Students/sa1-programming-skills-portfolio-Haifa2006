#Elif

#Assigning values to the respective variables
num_1 = 2000
num_2 = 2024

#Checking that the num_2 is greater than num_1
if num_2 > num_1:
    print("num_2 is greater than num_1")

#Checking that the num_1 and num_2 are equal
elif num_1 == num_2:
    print("num_1 and num_2 are equal")

#Checking that the num_1 is greater than num_1
else:
    print("num_1 is greater than num_2")

#Practice 
#Determining a grade through Nested decision structure
score = int(input("Enter the score"))

#It will print the score if it is equal or greater than 90
if score>=90:
    print("Your grade is A")

#It will print the score if it is equal or greater than 80
elif score>=80:
    print("Your grade is B")

#It will print the score if it is equal or greater than 70
elif score>=70:
    print("Your grade is c")

#It will print the score if it is equal or greater than 60
elif score>=60:
    print("Your grade is D")
    
#It will print the score If it is less than 60
else:
    print("Your grade is F")