#Exercise 04 - Primitive Quiz
"""In this exercise, you’ll create a simple program that asks the user a question,
evaluates their answer, and provides feedback.
Steps:
1. Write a program that asks the user “What is the capital of France?” and
waits for their response.
2. If the user’s answer is correct (i.e., “Paris”), the program should print a
message saying the answer is correct.
3. If the answer is incorrect, the program should print a message saying the
answer is wrong."""


#Answer:

#Asking the user "What is the capital of France?" and waiting for their response.
Capital = input("What is the capital of France? ")

#Check for the user's answer whether it is correct (i.e., "Paris").
if Capital == "Paris":
   print("Correct!")

#If the answer is incorrect, It will print the message saying the answer is incorrect.
else:
   print("Incorrect.")
