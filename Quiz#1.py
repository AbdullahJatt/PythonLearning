# QUIZ 1

#Problem 1
#Write a program that will take three integers as user defined inputs and prints the maximum number out of them.

num_1 = int(input("Enter your 1st number : "))
num_2 = int(input("Enter your 2nd number : "))
num_3 = int(input("Enter your 3rd number : "))

if num_1 > num_2 and num_1 > num_3 :
    max = num_1
elif num_2 > num_1 and num_2 > num_3 :
    max = num_2
elif num_3 > num_1 and num_3 > num_2 :
    max = num_3
print(f"The highest value is {max}")
#OUTPUT
#print the highest value

#Problem 2
#Write a program to calculate Area of Circle by taking radius as input.

radius = int(input("Enter the radius : "))
area = 3.14*(radius**2)
print (f" The area of the circle is {area}")
#OUTPUT --> 153.86 (if radius is 7)

#Problem 3
#Write a program to calculate percentage of total marks obtained in final term for a student.

total_marks = int(input("Enter total marks : "))
obtain_marks = int(input("Enter obtained marks : "))
percentage = (obtain_marks / total_marks)*100
print("You get",round(percentage,2),"% marks in examination.")

#OUTPUT
#93.64 (if student get 1030 marks out of 1100)

#Problem 4
#Write a program to print whether the user defined number is a prime number or not with proper message.

num = int(input("Enter a number : "))
flag = False
if num > 1 :
    for i in range (2 , num):
        if (num % i) == 0 :
            flag = True
            break
if flag:
    print (f"{num} is not a prime number.")
else:
    print (f"{num} is a prime number.")

#OUTPUT
# 3 is a prime number

#Problem 5
#Write a Python program to check whether an alphabet is a vowel or consonant.

alphabet = input("Enter any alphabet : ")
vowel = {"A","a","E","e","I","i","O","o","U","u"}
if alphabet in vowel :
    print(f"{alphabet} is a vowel.")
else:
    print(f"{alphabet} is a consonant.")

#OUTPUT
# f is a consonant (if f is user input)

#Problem 6
# Write a Python program to sum up two user defined integers. However, if the sum is:

#     Below Zero - Display "Bigger number was negative"
#     Equal to ZERO - Display "Both numbers were equally distant on number line on opposite sides"
#     Greater than ZERO - Display "Bigger number was positive"

num_1 = int(input("Enter 1st number : "))
num_2 = int(input("Enter 2nd number : "))
if (num_1 + num_2) < 0 :
    print("Bigger number was negative.")
elif (num_1 + num_2) == 0 :
    print("Both numbers were equally distant on number line on opposite sides.")
elif (num_1 + num_2) > 0 :
    print("Bigger number was positive.")
#OUTPUT
# Both numbers were equally distant on number line on opposite sides. (if user give -10 and 10)

#Problem 7
#Write a Python program to check whether two user defined integers are additive inverse of each other.

num_1 = int(input("Enter 1st number : "))
num_2 = int(input("Enter 2nd number : "))
if num_1 + num_2 == 0:
    print (f"{num_1} and {num_2} are additive inverse of each other.")
else:
    print (f"{num_1} and {num_2} are not additive inverse of each other.")

#OUTPUT
# if we get 5 and -5 as integers then output will be ---> 5 and -5 are the additive inverse of each other.

#Problem 8
#Write a Python program to check whether two user defined integers are multiplicative inverse of each other.

num_1 = int(input("Enter 1st number : "))
num_2 = float(input("Enter 2nd number : "))
if num_1 * num_2 == 1:
    print (f"{num_1} and {num_2} are multiplicative inverse of each other.")
else:
    print (f"{num_1} and {num_2} are not multiplicative inverse of each other.")
#OUTPUT
#if we get 5 and 0.2 as integers then output will be ---> 5 and 0.2 are multiplicative inverse of each other.

#Problem 9
#Write a Python program to check a triangle is equilateral, isosceles or scalene.
# Note :

#     All triangles have three sides
#     An equilateral triangle is a triangle in which all three sides are equal
#     A scalene triangle is a triangle that has three unequal sides
#     An isosceles triangle is a triangle with (at least) two equal sides

print("Enter the sides of triangle.")
side_1 = int(input( ))
side_2 = int(input( ))
side_3 = int(input( ))
if side_1 == side_2 == side_3:
    print("This is an equilateral triangle because all the sides are equal.")
elif side_1 != side_2 != side_3:
    print("This is an scalene triangle because all the sides are unequal.")
elif side_1 == side_2 or side_2 == side_3 or side_3 == side_1:
    print("This is an isosceles triangle because two sides are equal and one is unequal")

#OUTPUT
# if 3 4 7 are the sides then output will be ---> This is an scalene triangle because all the sides are unequal.


#Problem 10
#Write a Python program to print user defined multiplication table and also reverse the table.

table = int(input("ENter the number : "))
for i in range(1,11):
    print(f"{table} * {i} = ",(table)*(i))
print("......... REVERSE TABLE ...........")
for i in range(10,0,-1):
    print(f"{table} * {i} = ",(table)*(i))
#OUTPUT
# if user enter 5 thne output will be:
# 5 * 1 =  5 
# 5 * 2 =  10
# 5 * 3 =  15
# 5 * 4 =  20
# 5 * 5 =  25
# 5 * 6 =  30
# 5 * 7 =  35
# 5 * 8 =  40
# 5 * 9 =  45
# 5 * 10 =  50
# ......... REVERSE TABLE ...........
# 5 * 10 =  50
# 5 * 9 =  45
# 5 * 8 =  40
# 5 * 7 =  35
# 5 * 6 =  30
# 5 * 5 =  25
# 5 * 4 =  20
# 5 * 3 =  15
# 5 * 2 =  10
# 5 * 1 =  5