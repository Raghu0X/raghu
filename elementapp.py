def count_occurrences(my_list, element):
    count = my_list.count(element)  
    return count

numbers = [10, 20, 30, 20, 50, 20]
element_to_count = 20
occurrences = count_occurrences(numbers, element_to_count)

print(f"The element {element_to_count} appears {occurrences} times in the list.")
