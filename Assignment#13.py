#QUESTION
#Create a program to print all the numbers divisible by 3 and 5 to a user defined range

user_start = int(input("Enter the number you want to start :"))
user_end = int(input("Enter the number you want to end :"))

for i in range(user_start,user_end):
    if i % 3==0 and i % 5==0:
        print(f"{i} is divisible with 3 and 5")

#OUTPUT
# 0 is divisible with 3 and 5
# 15 is divisible with 3 and 5
# 30 is divisible with 3 and 5
# 45 is divisible with 3 and 5
