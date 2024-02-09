# Get arithmetic expression from the user
expression = input("Enter an arithmetic expression: ")

# Initialize variables
stack = []
operators = set(['+', '-', '*', '/'])
current_number = 0
current_operator = '+'
result = 0
is_negative = False

# Iterate through each character in the expression
for char in expression:
    if char.isdigit():
        current_number = current_number * 10 + int(char)
    elif char == '-':
        is_negative = True
    elif char == '(':
        if is_negative:
            current_number *= -1
            is_negative = False
        stack.append(result)
        stack.append(current_operator)
        stack.append('(')
        result = 0
        current_operator = '+'
    elif char == ')':
        if is_negative:
            current_number *= -1
            is_negative = False
        if current_operator == '*':
            result *= current_number
        elif current_operator == '/':
            if current_number != 0:
                result /= current_number
            else:
                print("Error: Division by zero")
                exit(1)
        current_number = result
        operator = stack.pop()
        while operator != '(':
            operand = stack.pop()
            if operator == '+':
                current_number += operand
            elif operator == '-':
                current_number -= operand
            operator = stack.pop()
    elif char in operators:
        if is_negative:
            current_number *= -1
            is_negative = False
        if current_operator in ('+', '-'):
            stack.append(result)
            stack.append(current_operator)
            result = 0
        elif current_operator == '*':
            result *= current_number
        elif current_operator == '/':
            if current_number != 0:
                result /= current_number
            else:
                print("Error: Division by zero")
                exit(1)
        current_number = 0
        current_operator = char

# Process the last number in the expression
if is_negative:
    current_number *= -1
if current_operator in ('+', '-'):
    stack.append(result)
    stack.append(current_operator)
elif current_operator == '*':
    result *= current_number
elif current_operator == '/':
    if current_number != 0:
        result /= current_number
    else:
        print("Error: Division by zero")
        exit(1)

# Calculate the final result by applying BODMAS rule
while stack:
    operator = stack.pop(0)
    operand = stack.pop(0)
    if operator == '+':
        result += operand
    elif operator == '-':
        result -= operand

# Display the result
print(f"Result: {result}")
