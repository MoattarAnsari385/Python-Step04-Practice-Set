# In this task, you need to create a list and a tuple, each containing the same 5 elements. You should compare the list and the tuple to check if they are equal. Then, append a new element to the list and compare the list and tuple again to see if they are equal after the update.

my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)

# Compare the list and tuple
if my_list == my_tuple :
    print("The lists are equal.")
else :
    print("The lists are not equal.")

# Append a new element to the list

my_list.append(6)

if my_list == my_tuple:
    print("The lists are equal after appending the new element.")
else :
    print("The lists are not equal after appending the new element.")
    print("Updated list:", my_list)
