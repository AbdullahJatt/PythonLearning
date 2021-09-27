# Boolean Algebra
# And ---> The result is true when both inputs are true otherwise false
# OR  ---> The result is true when atleast one input is true otherwise false
# NOT ---> convert true into false and false into true

# Problem # 1
# Create a program that will allow people over 18 and below 30 to watch IRON MAN 3

age = 26 
condition = age >18 and age <30
if condition:
    print("Yes, your are eligible.")
    # Yes, your are eligible.
else :
    print("Sorry, your are not eligible.")

#REASON :
"""
This programe show that you are eligible because the age of viewer is above 18 and below 30
This programe also show sorry message if you are below 18 or above 30
it depends on the viewer's age 
"""


#Problem # 2
#Create a program that will allow people over 4 and below 25 or above 50 and below 60 to watch cartoons
age = 40
condition = age >4 and age <25 or age > 50 and age < 60
if condition:
    print("Yes, your are eligible.")
else :
    print("Sorry, your are not eligible.")
    # Sorry, your are not eligible.

#REASON :
"""
This programe show sorry message because set the age of viewer between 4 to 25
and 50 to 60.
In this case the viewer is above 60 means this content is not for him

"""


#Problem # 3
#Suppose that you are a teacher, and you have make a list of all the students who scored above 60% and below 70% marks and those who scored above 90% in the examination.
marks = 92
condition_1 = marks > 60 and marks < 70
condition_2 = marks > 90
if condition_1 :
    print ( "You get C+ grade in your examintion.")
elif condition_2 :
    print( "Congrats! You get A+" )
else :
    print ( "Good luck for the next time." )
# Congrats! You get A+

#REASON :
"""
Here we do the same thing as we do in the above programe
here we show the grade of the student according to the marks of the student

The programe also show other grades according to marks
Example: if student get 65 marks then programe show C+ grade

"""