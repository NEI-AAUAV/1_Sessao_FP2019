# coding: utf-8
# This program finds the maximum of two numbers.
# It uses the built-in max function.
# Can you do it with conditional statements (if / if-else) instead?

x1 = float(input("number1? "))
x2 = float(input("number2? "))
x3 = float(input("number3? "))

# Use conditional statements instead of max function!
maximo = 0

if x1 >= x2 and x1>=x3:
	maximo = x1

elif x3>=x2:
	maximo = x3
	
else:
	maximo = x2


print("Maximum:", maximo)

