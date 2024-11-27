# Write a program to accept marks of 6 students and display them in a sorted manner.
marks = []

std1 = int(input("Enter your marks: "))
marks.append(std1)
std2 = int(input("Enter your marks: "))
marks.append(std2)
std3 = int(input("Enter your marks: "))
marks.append(std3)
std4 = int(input("Enter your marks: "))
marks.append(std4)
std5 = int(input("Enter your marks: "))
marks.append(std5)
std6 = int(input("Enter your marks: "))
marks.append(std6)

marks.sort()

# Display the sorted marks
print("Sorted Marks:", marks)
