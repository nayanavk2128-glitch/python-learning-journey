#String Manipulation
#1.String operation {Concatenation}
First_name=input("Enter your first name:")
second_name=input("Enter your second name:")
print(First_name+" "+second_name);#this will print the string itself

#String repetition
message="Warning !"
print(message*10)

#String methods 
message=" Hello world "
print(message.upper())
print(message.lower())
print(message.strip()*2)#Removing the space from leading and trailing
print(message.replace("world","python"))#Replacing old with new string

#Single line string
greetings='Nayana said "hi"to her friend'
print(greetings)
#Multi line string
greeting='''Nayana said "hi"to her friend
            and also said
            How they are doing
            '''
print(greeting)

#To find the length of teh string
name=input("Enter the name:")
print(len(name))


#String indexing
name="Nayana"
print(name[0])  # Prints the first character
print(name[1])  # Prints the second character
print(name[-4]) # Prints the third character from the end
#Slicing
print(name[2:6])#{Start:stop+1}
print(name[::2])#{Start:stop+1:step}
print(name[1:7:2])

#Escape sequence
greeting="hi\tthere \n. How are you ? \\"
print(greeting)
