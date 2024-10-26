#Advanced Requirements for the Exercise 04 - Primitive Quiz
"""Ignore Capitalization: Modify your program to accept answers regardless of
the capitalization (e.g., “paris”, “Paris”, and “PaRis” should all be considered
correct). Multiple Questions: Extend the program into a quiz that asks for the
capitals of 10 European countries. Provide feedback for each question."""

#Answer:

#A list containing 10 questions asking for the capitals of 10 European countries.
Countries_and_capitals = [
    "What is the capital of France?", 
    "What is the capital of United Kingdom?", 
    "What is the capital of Ukraine?",
    "What is the capital of Turkey?",
    "What is the capital of Russia?", 
    "What is the capital of Italy?",
    "What is the capital of Ireland?", 
    "What is the capital of Greece?",
    "What is the capital of Bulgaria?", 
    "What is the capital of Belgium?"
]

#A list containing 10 correct answers for the above 10 questions.
correct_response = [
  "paris",
  "london",
  "kiev",
  "ankara",
  "moscow",
  "rome",
  "dublin",
  "athens",
  "sofia",
  "brussels"
]


#Loop through every questions and its answer from the above 10 European countries and its capitals.
for i in range(len(Countries_and_capitals)):

#Asking questions to the user
 response = input(Countries_and_capitals[i] + " ")

# The responses from the user and the correct answer is converting due to avoid the affection of answer validation from the case differences.
 if response.strip().lower() == correct_response[i]:
  print("The answer is correct!")

 else:
     print(f"The answer is incorrect.The correct answer is {correct_response[i].capitalize()}.")