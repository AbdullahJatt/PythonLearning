#Question 1
#Create a program to print any user defined multiplication table

#for loop 

user = int(input("Enter a number : "))
for i in range(1,11):
    print(f"{user} * {i} = {user * i}")

#OUTPUT
#9 * 1 = 9
# 9 * 2 = 18
# 9 * 3 = 27
# 9 * 4 = 36
# 9 * 5 = 45
# 9 * 6 = 54
# 9 * 7 = 63
# 9 * 8 = 72
# 9 * 9 = 81
# 9 * 10 = 90

#Question 2
print("-----Reverse table-----")
user = user
for i in range(10,0,-1):
    print(f"{user} * {i} = {user * i}")

#OUTPUT
# 9 * 10 = 90
# 9 * 9 = 81
# 9 * 8 = 72
# 9 * 7 = 63
# 9 * 6 = 54
# 9 * 5 = 45
# 9 * 4 = 36
# 9 * 3 = 27
# 9 * 2 = 18
# 9 * 1 = 9