#DATATYPE
x=None
print(type(x))#Special datatype

#Operators 1.Arithematic
#1.=
x=10
print(x)
#2.+=
y=5
y+=5 #ShortForm{y=y+5}
print(y)
#3.-=
y=5
y-=5
print(y)
#4.*=
y=5
y*=5
print(y)
#5./=
y=5
y/=5
print(y)
#6.%=
y=5
y%=5
print(y)

#Comparison Operators
a=10
b=20
print(a==b)
print(a!=b)
print(a>b)
print(a>=b)
print(a<b)
print(a<=b)

#Logical Operators {and,or,not}
x=10
y=20
print(x<10 and y>20)
print(x<10 or y<25)
print(not(x<15 and  y>20))

#Membership operators {In strings}
name="Nayana"
#in
print( "N " in name) #false because in the name there is no space after N
print("a" in name) #true because a is present in the name
#not in
print( "N " not in name) #false because in the name there is no space after N
print("a" not in name) #true because a is present in the name
#Membership operators {In tuples}
my_list=[1,2,3]
print(1 in my_list)
print(9 not in my_list)

#Bitwise Operators
x = 2 
y = 3
print(x & y)#{Bitwise and}
print(x | y)#{Bitwise or}
print(~ x)#{Bitwise not}
print(~ y)
print(x ^ y)#{Bitwise XOR}
print(~(x ^ y))
print(y<<1)#{Left shift by 1}
print(x>>1)


 