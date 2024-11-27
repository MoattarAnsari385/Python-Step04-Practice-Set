# In this task, you need to create a tuple with 5 different numbers. You should calculate the sum of all the elements in the tuple and find the minimum and maximum values. Then, convert the tuple into a list, add a new element to the list, and convert the list back into a tuple. Finally, print the modified tuple.

tuples = (1, 6, 8, 9, 2)

sum = sum(tuples)

min_max = min(tuples), max(tuples)

my_list = list(tuples)
my_list.append(10)

my_tuple = tuple(my_list)

print(f"Sum of all elements: {sum}")

print(f"Minimum and maximum values: {min_max}")

print(f"Modified tuple: {my_tuple}")
