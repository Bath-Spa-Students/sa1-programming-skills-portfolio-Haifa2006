#Dictionaries

# Creating a dictionary

dictionary = {}
print(dictionary)

# Varifying the type of dictionary

dictionary = {}
print(dictionary, type(dictionary))

# Another method for creating a dictionary
 
dictionary = dict()
print(dictionary, type(dictionary))

# Adding something into the dictionary
Personal_Information = {'Name' : 'Fathima Haifa '  , 
           'Module' : 'CodeLab 1' ,
           'University' : 'Bathspa University '}
print (Personal_Information)


# Adding a value to the dictionary

dictionary  = { 'Name' : 'Fathima Haifa' , 
               'Age ' :  '18' , 
               'Fathers name ': 'Muhammad Haneefa' } 
print(dictionary,type(dictionary))
 

# Check if returning a single value results in a dictionary

dictionary  = { 'Name' : 'Fathima Haifa' ,
                'Age ' :  '18' , 
                'Fathers name ': 'Muhammad Haneefa' } 
print(dictionary["Name"],type(dictionary))


# Testing dictionary 

dictionary  = { 'Name' : 'Fathima Haifa' , 'Age ' :  '18' , 'Fathers name ': 'Muhammad Haneefa' } 
#Raises an exception if the key is not found in the dictionary
print(dictionary["student"]) 

# Use the get method to check if the student exists in the dictionary
dictionary  = { 'Name' : 'Fathima Haifa' , 'Age' :  '18' , 'Fathers name ': 'Muhammad Haneefa' } 
print(dictionary.get("student"))

# Since the student is not there in the dictionary, use a default a value to avoid none

dictionary  = { 'Name' : 'Fathima Haifa' , 'Age ' :  '18' , 'Fathers name ': 'Muhammad Haneefa' } 
print(dictionary.get("student", "Aysha "))


# Testing the .items method

dictionary  = { 'Name' : 'Fathima Haifa' , 'Age ' :  '18' , 'Fathers name ': 'Muhammad Haneefa' } 
print(dictionary.items())
 
 #Checking the keys in the dictionary

dictionary  = { 'Name' : 'Fathima Haifa' , 'Age ' :  '18' , 'Fathers name ': 'Muhammad Haneefa' } 
print(dictionary.keys())

#Using the deleted method

dictionary  = { 'Name' : 'Fathima Haifa' , 'Age' :  '18' , 'Fathers name ': 'Muhammad Haneefa' } 
del dictionary ["Age"]
print(dictionary.items())


# Delete method -Cont

dictionary  = { 'Name' : 'Fathima Haifa' , 
               'Roll No' :  '1234' , 
               'Fathers name ': 'Muhammad Murtaza' } 
del dictionary ["Age"]
print(dictionary.items())
print(dictionary.keys())
print(dictionary.values())


# Using Pop Method  - to remove 

dictionary  = { 'Name' : 'Fathima Haifa' ,
                'Age' :  '18' , 
                'Fathers name ': 'Muhammad Haifa' } 
print(dictionary.pop("Name"))
print(dictionary.keys())
print(dictionary.values())


# Using pop to remove items, it returns the element as a tuple

dictionary  = { 'Name' : 'Fathima Haifa' ,
                'Age' :  '18' , 
                'Fathers name ': 'Muhammad Haneefa' } 
print(dictionary.popitem())
print(dictionary.keys())
print(dictionary.values())



# Looping through dictionary elements

Personal_Information = {'Name' : 'Fathima Haifa '  , 
           'Module' : 'CodeLab 1' ,
           'University' : 'Bathspa University '}
print (Personal_Information)