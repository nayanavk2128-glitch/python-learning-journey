#TUPLES {collection of items which are ordered and immutable}
genders=("male","female","others")
print(genders)
print(type(genders))#Printing the type 
print(len(genders))#find the lenm of the tuple
print(genders[1])#accesing the elements in the tuple
print(genders[0:2:2])#slocing in tuple

tuple_1=(1,2,3)
tuple_1[1]="6"#'tuple' object does not support item assignment
print(tuple_1)

#Tuple methods
genders=("male","female","others")
tuple_1=(1,1,1,2,3)
print(tuple_1.count(1))
print(genders.index("female"))

#Tuple Operations
tuple_1=(1,2,3,4)
tuple_2=(5,6,7,8)
print(tuple_1+tuple_2)#Tuple concatenation
print(tuple_1*2)#Tuple repetition

#IN and NOT IN operator in TUPLES
tuple_1=(56,47,67,39)
print(39 in tuple_1)
print(67 not in tuple_1)

#Nested tupled
elements=("bru","coffee",(1,2,3,4))
print(elements)

#Sets in python
set_1={1,2,3}#ordered collection of items which are unordered and unindexed
print(set_1)
print(set_1[2])

#Set can be specified this way also
set_1=set((12,39,57))
print(type(set_1))
#CHECKING WHETHER IT WORKS WITH LIST AND TUPLE
t_2=list((12,39,57))
print(type(t_2))
t_3=tuple((23,47,89))
print(type(t_3))

#UNION , INTERSECTUON AND DIFFRENCE
set_1={1,2,3,4,5}
set_2={8,5,6,7,4}
print(set_1 | set_2)
print(set_1 & set_2)
print(set_1-set_2)
print(set_2-set_1)
print(set_2^set_1)#The symmetric difference returns elements that are in either of the sets but not in both

#Converting from one to another
list_1=[1,2,3,4,5]
print(tuple(list_1))
print(set(list_1))

#Empty Set
set_1={}
print(type(set_1))#It prints 'dict'
#Instead use
set_2=set()
print(type(set_2))

#Different Methods performed on Sets add(),pop(),remove(),discard(),clear() .
set_1={12,45,85,92}
set_1.add(62)
print(set_1)
set_1.pop()#Any element present in the set can be
print(set_1)
set_1.remove(45)
print(set_1)
set_1.discard(85)
print(set_1)
set_1.clear()
print(set_1)

#diffrence between remove nd discard
set_1={1,2,3,4,5,6}
set_1.remove(7)
print(set_1)#KeyError: 7
#Instead if we use this
set_1={1,2,3,4,5,6}
set_1.discard(7)
print(set_1)#It will if the specified element is there it will remove if not it will not raise the error