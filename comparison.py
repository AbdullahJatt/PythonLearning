# COMPARISON OPERATOR
#   Equal to (==)
#   Not equal to (!=)
#   Less than or equal to (<=)
#   Greater than or equal to (>=)
#   Greater (>)
#   Less (<)

# VARIABlES
males = 15
females = 21
#Equal operator
equal = (males == females)

print(f"""There are {males} males and {females} females in a meeting room.
According to Mr.Arham, there are {females} males and {males} females which is absolutely {equal}""")
#False


# VARIABlES
number_1 = 7
number_2 = 9

#Not equal operator
not_equal = (number_1 != number_2)

print(f"""According to Mr.Arham the number {number_1} and the number {number_2} is not equal
which is absolutely {not_equal}""")
#True

#Less than operator
less = (number_1 < number_2)

print( f"""There are two numbers {number_1} and  {number_2}.
I think that the number {number_1} is less than the number {number_2}
which is {less}""")
#True

#Greater than operator
greater = (number_2 > number_1)

print(f"""The number {number_2} is greater than number {number_1} which is {greater}""")
#True

#Less than or equal to operator
less_equal = (number_1 <= number_2)

print(f"The number {number_1} is less than or equal to {number_2} which is {less_equal}")
#True

#Greater than or eqaual to operator
greater_equal = (number_2 >= number_1)

print(f"The number {number_2} is greater than or equal to {number_1} which is {greater_equal}")
#True