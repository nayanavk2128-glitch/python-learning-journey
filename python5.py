#LIST IN Python {it is a collection of items which are ordered,mutable and duplication of data and hold different datatypes too}
items=["apple","banana","grapes","pomegranate"]
print(items)
print(items[0]) #accessing first element
print(items[-1])
list=["apple",1,2.5,True] #list can hold the items of different data types
print(list)

#List within the list and accessing the elements of the list
list=[["apple",1,2.5,True],[1,2,3,4]] 
print(list[1][2])

#to remove last element from the list we use pop() method
items=["apple","banana","grapes","pomegranate"]
items.pop()
print(items)
items.pop(2)
print(items)

#To add the elements to the list we use append() method
items.append("apple")
print(items)

#add the items to the specified index in the list
items.insert(2,"kiwi")
print(items)

#remove the elements from the specified position in the list
items.remove("kiwi")
print(items)

#clear the elements of the list
items.clear()
print(items)

#replacing the elements in the list
items=["apple","banana","grapes","pomegranate"]
items[0]="kiwi"
print(items)

#Slicng in the list
my_list=[1,2,3,4,5]
print(my_list[0:5:3])
#To find the length of the string
print(len(my_list))

#To sort the elements present inside the list
my_list1=[52,11,12,90,62,11]
my_list1.sort()
print(my_list1)
print(my_list1.index(52)) #to find the index of the element in the list
print(my_list1.count(11))
my_list1.reverse()
print(my_list1)