#PROBLEM
# Suppose that you are a teacher and you want to find average obtained marks of a student. Create a Python program to perform the following tasks:

#     Ask user if he/she has entered marks against desired number of subjects and wants to calculate average so far or wants to enter marks for more subjects
#     Print Number of subjects against marks were added
#     Print Average of all obtained marks


count = 1
flag = True
total_marks = 0
while flag :
    marks = int(input(f"Enter marks for subject {count} : "))
    total_marks += marks
    exit = input("Press N to exit or any other key to continue : ")
    if exit == "N" or exit == "n":
        flag = False
    count += 1
count -= 1
average = total_marks/count
print (f"Number of subjects are {count}")
print (f"The average marks of the student is {average}")

# OUTPUT
#15 if user give 5 numbers 5,10,15,20 and 25