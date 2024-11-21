#Functions

# Void function 
def print_message():
    print("Welcome to CodeLab 1")  

# Local variable 
def print_message():
    Introduction ="Welcome to CodeLab 1"  
    print(Introduction)

# Calling function 
print_message()
# If i call this message it shows an error 

def print_message():
    Introduction ="Welcome to CodeLab 1"  
    print(Introduction)
# The message will be not defined because of the local variable life is inside of program 

print_message()

#Same local variable name in different functions, No Syntax error

def Full_Name():
  Name ="Fathima Haifa"
  print(Name)
  
def Emirate_Living():
  Emirate ="Ajman"
  print(Emirate)

Full_Name()
Emirate_Living()

# Assigning argument value to variable 

def print_message_2(message):  
  print(message)

University ="Welcome to Bathspa University"
print_message_2(University)

#Parameter x is holding a value and returns its double
def main():
    number =8
    show_double(number)
    
def show_double(x):
      print(x*2)

main()