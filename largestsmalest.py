def find_largest_smallest(my_list):
    largest = max(my_list)  
    smallest = min(my_list)  
    return largest, smallest

numbers = [10, 20, 30, 40, 50]
largest, smallest = find_largest_smallest(numbers)

print("Largest number:", largest)
print("Smallest number:", smallest)
