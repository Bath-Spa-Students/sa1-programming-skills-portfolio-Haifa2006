#Loops

#Print j as long as j is less than 10
j = 1
while j < 10:
  print(j)
  j += 1  


  count = 1
while count <= 5:
    print("Count is:", count)
    count += 1

    #Infinite Loop With Break Statement 

j = 1
while j < 6:
  print(j)
  if j == 3:
    break
  j += 1   # j=j+1  Both are same 

#For loop 
Colors = ["Black", "White", "Grey"]
for x in Colors:
  print(x)


  # Looping through a sequence with range

  for x in range(0,25,5):
      print (x)

for x in range(10):
     print (x)

# Enhance readability by using range in the loop

for x in range(0,25):
      print (x, end=",")
  
 # Standard step count with an increment of 1 

for x in range (0,25,3):   
   print(x ,end=",")

# Count +5
for x in range (0,50,5):
      print(x,end=",")

# Asking for the users input in a controlled loop

Number= int (input("Enter maximum number for range :"))
for x in range (0,50,5):
      print(x,end=",")


# Running time Total 

Total =0 
for i in range(5):
    x=float(input("Enter the Number :  "))
    Total +=x   
print(Total)

# Controlling the loop through sentinels value 

Total =0 
while True:
    x=float(input("Enter the Number :  "))
    Total +=x  
    if x ==-1 :
        break 
print(Total)


#Nested Loops, A loop withon a loop



x= [11,12,13]
y=[14,15,16]
for i in x:
    for j in y:
        print (i,j)

        
# Another Example 

for i in range (2):   # 0,1,
    
      for j in range(3) :  #0,1,2
             print("outer loop" ,i , "Inner Loop" , j )