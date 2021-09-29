#QUESTION :
'''
Create a program that will take all the necessary information from the
user like (First Name, Last Name, Age, Gender, Religion, Nationality,
Polling Station City, User's residential city etc.).
Base on that information show that whether the user is allowed to cast
the vote or not keeeping the following parameters in mind for
decision making:

    User must be 18 or over
    User must belong to the same polling station city
    User must be Pakistani

Show all of user's provided info to the user
'''

first_name = input("Enter your first name : ")
last_name = input("Enter your last name : ")
age = int(input(f"{first_name} {last_name} please enter your age : "))
if age >= 18 :
    print("You are adult and allowed to cast vote")
    country = input(f"{first_name} {last_name} please enter your country : ")
    if country == "Pakistan" :
        print ("Superb!")
        city = input(f"{first_name} {last_name} please enter your city where you live :")
        polling_address = input(f"{first_name} {last_name} please enter your polling station city :")
        if city == polling_address :
            print("Congratulations! You are allowed to cast vote")
            print(f"{first_name} {last_name} please give us more info.")
            gender = (input("Enter your gender :"))
            religion = (input("Enter your religion :"))
            cnic = int(input('Enter your CNIC number (Without"-") : '))

            print(f""" Your info:
Full Name : {first_name} {last_name}
age : {age}
Gender : {gender}
Religion : {religion}
Nationality : {country}
City : {city}
Polling Station City : {polling_address}
CNIC : {cnic}

...YOU ARE ALLOWED TO CAST VOTE...

""")
        else:
            print(f"{first_name} {last_name} sorry! you must be from the same city where you cast vote")

    else:
        print(f"{first_name} {last_name} sorry you must be pakistani for casting vote")
    
    
else:
    print(f"{first_name} {last_name} sorry you are underage")