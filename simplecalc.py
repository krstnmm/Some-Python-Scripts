def layout():
	print("---------------MENU---------------\n")
	print("|                                |\n")
	print("|  (1) Add      (2) Subtract     |\n")
	print("|  (3) Multiply (4) Divide       |\n")
	print("|  (5) Power    (6) Squareroot   |\n")
	print("|                                |\n")
	print("----------------------------------\n")

def add(a, b):
	return a + b

def subtract(a, b):
	return a - b

def multiply(a, b):
	return a * b

def divide(a, b):
	return a / b

def power(a, b):
	return a ** b

def square_root(a, b):
	return a ** (1/b)

def print_ans(ans):
	print("The answer is ", ans,"\n")


# main
print("\nWELCOME TO MY SIMPLE CONSOLE CALCULATOR!\n")
layout()
operator = int(input("Select a number as your operator on the menu:\n"))
num1 = int(input("Enter the first number: \n"))
num2 = int(input("Enter the second number: \n"))

if operator == 1:
	print_ans(add(num1, num2))
if operator == 2:
	print_ans(subtract(num1, num2))
if operator == 3:
	print_ans(multiply(num1, num2))
if operator == 4:
	print_ans(divide(num1, num2))
if operator == 5:
	print_ans(power(num1, num2))
if operator == 6:
	print_ans(square_root(num1, num2))

