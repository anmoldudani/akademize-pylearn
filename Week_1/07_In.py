  
"""Inputs"""

from random import randint

r = randint(1, 11)
name = input("Enter your name: ")
n = int(input("Enter a number between 1 to 10: "))

if n >= r:
    print(f"{name} you are is lucky")
else:
    print(f"{name} you are not so lucky try again...")

'''
Output:
Enter your name: Jaeck
Enter a number between 1 to 10: 3
Jaeck you are not so lucky try again...
'''