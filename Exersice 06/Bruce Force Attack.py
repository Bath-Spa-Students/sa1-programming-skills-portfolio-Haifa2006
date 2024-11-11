#Excersice 06 - Bruce Force Attack
"""Write a program that simulates a password entry system. The correct password
is defined as 12345. The program should keep asking the user to enter the
password until they provide the correct one.

Basic Requirements:
1. Define the correct password.
2. Use a while loop to repeatedly ask the user for the password until the
correct one is entered.
3. Output an appropriate message when the correct password is entered.

Optional Requirements:
Modify the program to include a maximum of 5 password attempts. If the
user enters the wrong password, inform them of the remaining attempts. If the
maximum number of attempts is reached, inform the user that the authorities
have been alerted."""

#Answer:

#Define the expected password for verification
expected_password = "12345"

#Define the maximum attempt limit
attempt_limit = 5
limit = 0

#Continuously ask for password until attempt limit
while limit < attempt_limit:

    #Getting the password from the user 
    password_attempt = input("Type your password:")

    #Verify the entered password matches
    if password_attempt == expected_password:
     print("Password Correct. Enjoy your access!")
     break
    else:
        #Increasing the number of attempts
         limit += 1
         attempts_left = attempt_limit - limit
         if attempts_left > 0:
            print("Incorrect password. You have " + str(attempts_left) + " remaining tries.")
         else:
            print("Incorrect password. You've reached the attempt limit. The authorities have been notified.")