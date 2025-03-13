def merge_and_remove_duplicates(list1, list2):
    merged_list = list1 + list2  
    unique_list = list(set(merged_list))  
    return unique_list

list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 60, 70]

merged_unique_list = merge_and_remove_duplicates(list1, list2)

print("Merged list without duplicates:", merged_unique_list)
