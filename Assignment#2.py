#RULES of assigning variables 
# some of theme are as following 
# variables must be letters
# numbers or digits are not allowed
# varaibles can be self explainatory
# fullstop , commas , exclamatery marks , symbols are not allowed insted of underscor(_)
# spaces are also not allowed 
#  semicolon , colon , brackests are also not allowed 

#........................................

# data types
# int , string , float , object , bool , range 

#..........................................

#Print Function

boys = 4
girls = 7
teachers = 10
ratio = 5.2
first_controller = "Principal"
sec_controller =  "Voice principal"


print (boys+girls)
#11
print (girls-boys)
#3
print (boys*girls)
#28
print (boys/girls)
#0.5714285714285714
print (boys+girls+teachers)
#21
res = boys+girls-teachers
print (res)
#1
boys = girls
print (boys)
#7


print (first_controller,sec_controller)
#Principal Voice principal

print(type(boys))
#<class 'int'>
print(type(girls))
#<class 'int'>
print(type(ratio))
#<class 'float'>
print(type(first_controller))
#<class 'str'>
print(type(sec_controller))
#<class 'str'>
print("--------- THE END ------------")
