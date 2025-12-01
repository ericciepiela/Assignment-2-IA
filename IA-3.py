#Project 1
#Enter the first number
first_number = float(input("Enter first number: "))
#Enter an operator
operator = input("Enter an operator (+, -, *, /): ")
#Enter the second number
second_number = float(input("Enter second number: "))
#Perform operation
if operator == "+":
result = first_number + second_number
print(f"The result of {first_number} + {second_number} is {result:.2f}")
elif operator == "-":
result = first_number - second_number
print(f"The result of {first_number} - {second_number} is {result:.2f}")
elif operator == "*":
result = first_number * second_number
print(f"The result of {first_number} * {second_number} is {result:.2f}")
elif operator == "/":
if second_number != 0:
result = first_number / second_number
print(f"The result of {first_number} / {second_number} is {result:.2f}")
else:
print("Cannot divide by zero")
else:
print("invalid operator")
#Problem 2
#Input total sales target
sales_target = float(input("Enter sales target: "))
#Cumulative sales
cumulative_sales = 0.0
#Go through 5 days
for day in range(1,6):
daily_sales = float(input(f"Enter day {day} sales: "))
cumulative_sales += daily_sales
percentage = (cumulative_sales / sales_target) * 100
print(f"Cumulative sales: {cumulative_sales:.1f} ({percentage:.1f}%)")
