# In this task, you need to perform several operations with a list. First, create an empty list. Then, accept 5 numbers from the user and add them to the list. After that, sort the list in ascending order and print the sorted list. Next, remove the last element from the list and print the final list after removal.

numbers = []

num1 = int(input("Enter number here: "))
numbers.append(num1)

num2 = int(input("Enter number here: "))
numbers.append(num2)

num3 = int(input("Enter number here: "))
numbers.append(num3)

num4 = int(input("Enter number here: "))
numbers.append(num4)

num5 = int(input("Enter number here: "))
numbers.append(num5)

numbers.sort()

print("Sorted list:", numbers)

numbers.pop()

print("Final list after removal:", numbers)

