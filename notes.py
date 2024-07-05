'''
This is a note for Module 2 of Python Basics. 
This is a Multi-line String comment. 

LESSON 5: Python Functions
'''
# print() function --> to display messages, it can print strings, numbers and variables, also can print multiple items
# you can use (\n) for a Newline and (\t) for a new Tab. This can be used inside the print() function
# Can also use String concatenation (adding strings together) by using Operator (+). 

#seperator 
#print("apple", "banana", "cherry", sep="-")

#end
#print("This is just the beginning... ", end="")
#print(" and here is the continuation.")
#print()

#seperator + end
#print("apple", "banana", "cherry", sep="-", end="...yum!")

#String Formatting

#placeholder eg
#name = "Ella"
#print("Her name is %s." % name)

#placeholder by format
#age = 25
#print("She is {} years old.".format(age))

# F-String
hobby = "writing"
print(f"Ella loves {hobby}.")

pi = 3.141592653
print(f"The value of PI to three decimal places is {pi:.3f}.")

#Getting User Input by input() function
# whatever the user types, input() function returns it as a string. 
# If you want a number, you have to convert it. (int() or float())

#-----  age = int(input("how old are you?: "))
#-----  print(age)


# Type Convertors ---> str()  bool()  int()  float()
#-- Know Data Type by type() |||  len()  ||| isinstance(x , int) -- checks if it is True or false

#Python -- abs(), round(), sum(), min(), max(), pow() -- , divmod() -- fair division

import math
# sqrt(), ceil(), floor(), exp(), log(), sin(), cos(), tan(), radians(), degrees()





