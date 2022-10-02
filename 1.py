# sort() will sort the list in-place, mutating its indexes and returning None , whereas sorted() will return a new sorted list leaving the original list unchanged

# 1. Write an algorithm that takes in an unsorted numerical list as an argument and sorts the list (use the sort() method).
lst = [6, 3, 1, 2]
lst.sort()
 
print(lst)

# 2. Write an algorithm that takes in an unsorted numerical list as an argument and creates a new sorted list (use the sorted() function).

unsorted_list = [6, 3, 1, 2]
sorted_list = sorted(unsorted_list)
print(sorted_list)
#3. Write an algorithm that takes in an unsorted numerical list as an argument and creates a new sorted list in descending order (use the sorted() function).

unsorted_list = [6, 3, 1, 2]
sorted_list = sorted(unsorted_list, reverse=True)
print(sorted_list)