tuples_list = [(1, 4), (3, 2), (5, 7), (2, 5)]

sorted_list = sorted(tuples_list, key=lambda x: x[1])

print("Sorted list based on the second element:", sorted_list)
