import math

def calculate_math_operations(number):
    if number < 0:
        return "Factorial is not defined for negative numbers"
    
    square_root = math.sqrt(number)
    
    if number.is_integer() and number >= 0:
        factorial = math.factorial(int(number))
    else:
        factorial = "Factorial is only defined for non-negative integers"
    
    sine_value = math.sin(number)

    return square_root, factorial, sine_value

number = float(input("Enter a number: "))

square_root, factorial, sine_value = calculate_math_operations(number)

print(f"Square Root of {number}: {square_root}")
print(f"Factorial of {number}: {factorial}")
print(f"Sine of {number}: {sine_value}")
