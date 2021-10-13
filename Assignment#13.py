#QUESTION
#Create a program to print all the numbers divisible by 3 and 5 to a user defined range

user_start = int(input("Enter the number you want to start :"))
user_end = int(input("Enter the number you want to end :"))

for i in range(user_start,user_end):
    if i % 3==0:
        print(f"{i} is divisible with 3")
    if i % 5==0:
        print(f"{i} is divisible with 5")

#OUTPUT
# 0 is divisible with 3
# 0 is divisible with 5
# 3 is divisible with 3
# 5 is divisible with 5
# 6 is divisible with 3
# 9 is divisible with 3
# 10 is divisible with 5
# 12 is divisible with 3
# 15 is divisible with 3
# 15 is divisible with 5
# 18 is divisible with 3
# 20 is divisible with 5
# 21 is divisible with 3
# 24 is divisible with 3
# 25 is divisible with 5
# 27 is divisible with 3
# 30 is divisible with 3
# 30 is divisible with 5
# 33 is divisible with 3
# 35 is divisible with 5
# 36 is divisible with 3
# 39 is divisible with 3
# 40 is divisible with 5
# 42 is divisible with 3
# 45 is divisible with 3
# 45 is divisible with 5
# 48 is divisible with 3