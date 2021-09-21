# PRECEDENCE

# BDMAS:
# B stands for Brackets
# D stands for Division
# M stands for Multiplication   
# A stands for Addition
# S stands for Subtraction

# This rule is applied when we solve any expression

res = 4 + 7 - 8 / 4 * 5
#      4 + 7 - 2 * 5
#      4 + 7 - 10
#      11 - 10
#      1

print (f"Result = {res}")

# res = 1.0

res = 4 + 7 - 8 / (4 * 5)
#     4 + 7 - 8 / 20
#     4 + 7 - 0.4
#     11 - 0.4
#     10.6
"""
print(4 + 7 - 8 / (4 * 5))      #10.6
print(4 + 7 - 8 / 20)           #10.6
print(4 + 7 - 0.4)              #10.6
print(11 - 0.4)                 #10.6
print(10.6)                     #10.6
"""
# I check a single line still the answer is same 

print (f"Result = {res}")
# res = 10.6

res = 4 + 7 - (8 / 4) * 5

"""print(4 + 7 - (8 / 4) * 5)      #1.0
print(4 + 7 - 2 * 5 )           #1
print(4 + 7 - 10 )              #1
print(11 - 10 )                 #1
print(1)                        #1
"""
# I check a single line still the answer is same it means our calculation is correct

print(f"Result = {res}")
# res = 1.0

"""
According to BDMAS rule which is also known as precedence,
we know that the operators in the brackets solve first
that's why we get different answers when we just change the place of brackets.

"""

res = (4 + 7) - 8 / 4 * 5**2 

"""
print ((4 + 7) - 8 / 4 * 5**2)          #-39.0
print ((4 + 7) - 8 / 4 * 25)            #-39.0
print (11 - 8 / 4 * 25)                 #-39.0
print (11 - 2 * 25)                     #-39
print (11 - 50)                         #-39
print(-39)

"""

print(f"Result = {res}")

"""
Here we notice that the answer is change and brackets are not solved first ...
exponentiation solved first
it's just because of their higher precedence
In such a way the modulus and floor division solved first than others

In short: higher precedence solve first and then lower
"""

print (".........................................")
print ("                 THE END                 ")
print (".........................................")