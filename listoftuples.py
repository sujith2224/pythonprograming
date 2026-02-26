tuples_list = [(1, 3), (4, 1), (2, 5), (3, 2)]
sorted_list = sorted(tuples_list, key=lambda x: x[-1])
print("Sorted list:", sorted_list)