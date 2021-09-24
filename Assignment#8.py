# Multiple assignment
student = 47
# every single teacher teach one student only
teacher = student
# every teacher teach a different book
subject = teacher

print(subject)
#47

# Another method
student = teacher = subject = 47

print(student)
#47
print(teacher)
#47
print(subject)
#47

#QUESTION 1
# Program a simple scenario that involves Decision Making

student = True
#if student is present in class

if student:
    print("This student is present in the class")
# This student is present in the class

#QUESTION 2
# Suppose that you are a teacher, and you have make a list of all the students who passed the examination successfully. Suppose that the passing criteria is 60% marks.

marks = 100
#if student get 60 marks then he passed
if marks >= 60:
    print("Congrats! You have passed.")
#Congrats! You have passed.

#QUESTION 3
#Suppose that you are a teacher, and you have make a list of all the students who did not pass the examination successfully. Suppose that the all students with marks below 55% are fail.
total_marks = 100
obtain_marks = 50
condition = obtain_marks <= 55
if condition:
    print("Good luck for the next time.")
#Good luck for the next time.