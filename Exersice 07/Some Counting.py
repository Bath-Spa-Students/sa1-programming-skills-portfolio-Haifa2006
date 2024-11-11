#Exercise 07 - Some Counting
"""Use your newly acquired knowledge of the for loop to complete the following
tasks. Print all values to the console in each case. * Write a loop that counts
up from 0 to 50 in increments of 1. * Write a loop that counts down from 50 to
0 in decrements of 1. * Write a loop that counts up from 30 to 50 in increments
of 1. * Write a loop that counts down from 50 to 10 in decrements of 2. * Write
a loop that counts up from 100 to 200 in increments of 5. You may include all
loops in a single project"""

#Answer:

#A loop which starts from 0 and it counts till 50 in increments of 1.
print("Counting from 0 to 50 in increments of 1.")
for h in range(0,51,1):
    print(h)

#A loop which starts from 50 and it counts till 0 in decrements of 1.
print("Counting from 50 to 0 in decrements of 1.")
for h in range(50,-1,-1):
    print(h)

#A loop which starts from 30 and it counts till 50 in increments of 1.
print("Counting from 30 to 50 in increments of 1.")
for h in range(30,51,1):
    print(h)

#A loop which starts form 50 and it counts till 10 in decrements of 2.
print("Counting fro 50 to 10 in decrements of 2.")
for h in range(50,9,-2):
    print(h)

#A loop which starts from 100 and it counts till 200 in increments of 5.
print("Counting from 100 to 200 in increments of 5.")
for h in range(100,201,5):
    print(h)

