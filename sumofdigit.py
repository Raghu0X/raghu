def sum_of_digits(n):
    total = 0
    for digit in str(n):
        total += int(digit)  
    return total
result = sum_of_digits(12345)
print(result)
