#QUESTION :
#Create a program that will take all the necessary information from the user like (First Name, Last Name, Age, Gender, Religion, Nationality, Polling Station City, User's residential city etc.). Base on that information show that whether the user is allowed to cast the vote or not keeeping the following parameters in mind for decision making:
#User must be 18 or over

first_name = (str(input("Enter your first name : ")))
last_name  = (str(input("Enter your last name : ")))
age = (int(input("Enter your age : ")))
gender = (str(input("Enter your gender :")))
religion = (str(input("Enter your religion :")))
nationality = (str(input("Enter your country name :")))
polling_station_address = (str(input("Enter your polling station address :")))
residential_city = (str(input("Enter your residential city :")))
cnic = (int(input('Enter your CNIC number (Without"-") : ')))

if age >= 18 :
    print(f"""Your info :
    Name :{first_name} {last_name}
    Age : {age}
    Gender : {gender}
    Religion : {religion}
    Nationality : {nationality}
    Polling Station City : {polling_station_address}
    Residential City : {residential_city}
    CNIC Number : {cnic}

    You are eligible for voting
    """)
else :
    print(" Sorry you are not eligible for voting")