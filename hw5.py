#Assignment: Python Functions
'''
1. The Calculator App

Objective: The aim of this assignment is to build a basic calculator that can perform addition, subtraction, 
multiplication, and division.

Task 1: Create functions for each arithmetic operation.

Task 2: Use inputs to ask the user what operation they want to perform, and what numbers they want to use.

Task 3: Ensure your code can handle division by zero and other potential errors. So if you divide by 0, 
there is error handling set up to prevent an error from showing in the console.

'''
ty = (input("Enter the type of operation you want to perform-- (a for addition) | (s for subtraction) | (m for multiplication) | (d for division): "))
x = int(input("Enter the first number you want to use: "))
y = int(input("Enter the second number you want to use: "))

def addition(x, y):
    z = 0
    z = x + y
    return z

def subtraction(x, y):
    z = 0
    z = x - y
    return z

def multiplication(x, y):
    z = 0
    z = x * y
    return z

def division(x, y):
    z = 0
    try:
        # Attempt to perform the division operation and store the result in the 'z' variable.
        z = x / y
        return z
    except ZeroDivisionError:
        # Handle the exception if a division by zero is attempted.
        print("The division by zero operation is not allowed. Please Try Again")

if(ty == 'a'):
    print(addition(x,y))
    

if(ty == 's'):
    print(subtraction(x,y))

if(ty == 'm'):
    print(multiplication(x,y))

if(ty == 'd'):
    print(division(x,y))




