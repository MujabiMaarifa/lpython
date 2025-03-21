"""
Instructions:

Basic Calculator Program

Create a simple Python program that asks the user to input two numbers and a mathematical operation (addition, subtraction, multiplication, or division).
Perform the operation based on the user's input and print the result.
Example: If a user inputs 10, 5, and +, your program should display 10 + 5 = 15.



Note: Upload the code to GitHub and submit the GitHub link
"""
print("Calculators make mathematicians\n")
a = int(input("Enter the first number (1,2,3,4): "))
b = int(input("Enter the second number (1,2,3,4): "))

operation = str(input("Enter the operation to perform (+,-,/,%,*): "))

def operate() :
    if operation == '+' :
        result = a + b
        print("\nThe answer is: ", result)
    elif operation == '-' :
        result = a - b
        print("\nThe answer is: ", result)
    elif operation == '*' :
        result = a * b
        print("\nThe product is: ", result)
    elif operation == '%' :
        result = a % b
        print("\nThe answer remeinder: ", result)
    elif operation == '/' :
        result = a / b
        print("\nThe answer quotient: ", result)

operate()

print("\nThankyou for enjoying our calculator")
print("\nHappy coding!!")