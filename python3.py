#INPUT/OUTPUT,STRING MANIPULATION,COMMENTS
#print statement
age=20
print("My age is ",age)
#input statement{ if user wants to enter manually}
age=input("Enter the age:")
print("Age of the person is:",age)
#age can only be integer
age=int(input("Enter the age:"))
print("Age of the person is:",age)


boy_name=input("Enter the boy name>>")
girl_name=input("Enter the girl name>>")
print(boy_name)
print(girl_name)

#small project
boy_name=input("Enter the boy name:")
girl_name=input("Enter the girl name:")
boy_age=int(input("Enter the boy age:"))
girl_age=int(input("Enter the girl age:"))
age_diff=abs(boy_age-girl_age)#here i am using abs beacuse sometimes boy{age} may be younger
print(boy_name +" loves "+ girl_name + " and the age difference is "+ str(age_diff))
print(f"{ boy_name } loves { girl_name } and the age difference is {age_diff}")#formatted print statement

name="nikitha"
age=20
print("HELLO !" + name + " your age is " + str(age))
#formatted print statement {no need of string conversion}
print(f"hello{name}your age is{age}")

#Single line comments
'''This is a multi line comment'''
"""This is a multi line comment"""