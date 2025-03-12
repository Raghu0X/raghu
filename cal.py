def calculator(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            return "Error: Division by zero is not allowed"
        return num1 / num2
    else:
        return "Error: Invalid operator"

num1 = 10
num2 = 5
operator = "+"
result = calculator(num1, num2, operator)
print(f"The result of {num1} {operator} {num2} is {result}")
