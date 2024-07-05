#Assignment: Python Functions
'''
2. The Shopping List Maker

Objective: The aim of this assignment is to create a program that helps users make a shopping list.

Task 1: Write a function that lets the user add items to a list.

Task 2: Include a function to remove items from the list.

Task 3: Add a function that prints out the entire list in a formatted way.

Note: The goal of this is to be a program. The recommendation is to use a while loop that will allow the user to continue to add, 
remove, and print off their shopping list until they decide to "quit", also known as breaking the loop.
'''
shoplist = []

def additems(x):
    return shoplist.append(x)

def removei(x):
    return shoplist.remove(x)

def printlist():
    shoplist.sort()
    print(shoplist)
    return shoplist

x = '0'
y = input("Please enter what you want to do in the Shopping list:- 'a' for add items, 'r' for remove items, 'p' for print list, and q for 'quit':  ")
while (y != 'q' and x != 'q'):
    if (y == 'a' and x != 'q'):
       x = input("Please enter an item to add to list and 'q' to quit or 'p' to printlist: ")
       additems(x)
    
    if (y == 'r' and x != 'q'):
       x = input("Please enter an item to remove from the list and 'q' to quit:: ")
       removei(x)

    if (y == 'r' and x != 'q'):
       x = input("Please enter an item to remove from the list and 'q' to quit:: ")
       removei(x)

    if(y == 'p' or x == 'p'):
       print("The list is printed below")
       print(printlist)

    y = input("Please enter what you want to do in the Shopping list:- 'a' for add items, 'r' for remove items, 'p' for print list, and q for 'quit':  ")

