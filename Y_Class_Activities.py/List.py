#List

# Homogeneous List 

introduction = ["Haifa" , "18 years" , "Creative Computing"]
print (introduction)

# Heterogeneous List
Details = ["Fathima Haifa" , "18" , "30.09"]
print (Details)

# Repitition Operator , To repeat data

integers = [1,2,3,4]
new_integers = integers * 4
print(new_integers)

# Positive Indexing
integers = [8,9,10,11,6,7]
print(integers[6])

# Negative indexing starts from -1  , bcz 0 is a non-negative integer 

integers =[8,9,10,9,6,7]
print(integers[-6]) 

# lens function tells us number of items in the list 
integers =[8,9,10,11,6,7]
print("number of elements in a list :" ,len(integers)) 

# Mutability (Changable) we can change values in the list 

integers =[8,9,10,11,6,7]
integers[0]=1

#Concatenation Dont use small l (list) to write variable name eg (list )
List_1 =[11,12,13,14,15]
List_2=[18,17,16,15,14]

List_3=List_1 + List_2
print (List_3)

# List slicing  - to use one part of list 

recent_list =[4,5,6,12,17,8,9]
output= recent_list [0:3] # 2nd index exclusive index - 0-2 index , total 3 elements  , [3:7] 1st index inclusive
print(output)

# find elements in list  -if operator 

recent_list =[11,12,13,15,16,17,18,19]
if 10 in recent_list:
     print("discovered")
else:
      print ("Not discovered")

# (not in)  operator 

recent_list2 =[11,12,13,15,16,17,18,19]
if 20 not in recent_list2:
     print("yes")
else:
      print ("No")

 # built in methods - append

recent_list3 = [1,2,3,3,4]
recent_list3.append(100)
print(recent_list3) 

#   built in methods - index
recent_list4 = [1,2,3,3,4]
print (recent_list4.index(4))  # Identify index of number 7

#   built in methods - sort

recent_list5 = [9,12,11,8,6]
recent_list5.sort()
print(recent_list5)     

#   built in methods - reverse
recent_list6 = [9,12,11,8,6]
recent_list6.reverse()
print(recent_list6)

#   built in methods - remove

recent_list7 = [9,12,11,8,6]
recent_list7.remove(11)
print(recent_list7)