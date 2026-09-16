#CONSTANTS {Whose value does not change during the execution of the program}

PI = 3.14159
GRAVITY = 9.8
SPEED_OF_LIGHT = 299792458

#VARIABLES {Whose value can change during the execution of the program} 
a=10;
a=15;
print(a);

#Variable assignment tricks
a,b,c=10,20,30;
a,b,c=10,10,10;
a=b=c=10;

#Rules of Assigning the variables
#1. Variable names can contain letters, numbers, and underscores
#2. Variable names cannot start with a number
#3. Variable names are case-sensitive
#4. Variable names cannot be keywords
name="Nayana";
name_1="Nayana";
name_2="Nikitha";
1name="Nayana"; #Invalid variable name
_1name="Asha";#valid variable name because it starts with the underscore
Name="ASHA"; 
name="ASHA"; 
print(Name);#Case sensitiveprint(Name);#Case sensitive

if="Hello"; #Invalid variable name
print(if);


a=10;
b=20;
print(a);#The value of a will be printing 
print("a");#If we want to print the string a itself

#data types:- Tells which type of the data a variable is holding

a=10; #Integer
b=99.9; #float
name="nikitha"; #string
is_student=True; #boolean

#lets test
 
print(type(a));
print(type(b));
print(type(name));
print(type(is_student));
#type conversion
print(float(a));
print(int(b));
print(int(name)); #Invalid conversion

age=20;
rupees="100";
print(age+rupees);#invalid concatenation
#then
print(age+int(rupees));#valid concatenation

#Arithematic operations(+,-,*,/,%(modulus),//(floor division),**(exponential))
apple=100;
mango=40;
print(apple+mango);#addition
print(apple-mango);#subtraction
print(apple*mango);#multiplication
print(apple/mango);#division
print(apple%mango);#modulus/remainder
print(apple//mango);#floor division
print(apple**mango);#exponential
#BODMAS rule(multiple operations in a single expresion)
