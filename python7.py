#Dictonaries.Methods and operators
#dict specifing 
my_dict={"Nayana": "21-11-2006",
         "Yojith": "28-02-2019"}
my_dict1=dict(Nayana="21-11-2006",
         Yojith="28-02-2019")
print(my_dict)
print(my_dict1)
karnataka_food = {
    "Bengaluru": "Bisi Bele Bath",
    "Mysuru": "Mysore Pak",
    "Mangaluru": "Neer Dosa"
}
print(type(karnataka_food))

#Accesing the dictonary
print(karnataka_food["Mangaluru"])
print(my_dict["Yojith"])
print(my_dict.get("Namratha","not there")) #if the key is not there it will return the default value

#Adding the new elements to the dict
karnataka_food["Darwada"]="Dharwad peda"
print(karnataka_food)

#Updating the dictionary
karnataka_food["Darwada"]="peda"
print(karnataka_food)

#Removing the elements from the dict
karnataka_food.pop("Darwada")
print(karnataka_food)

#Removing the dict
del karnataka_food["Mysuru"]
print(karnataka_food)

#Clearing the dict
karnataka_food.clear()
print(karnataka_food)

#dict methods
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())           

#Updating the dict
new_dishes = {"Hubballi": "Girmit"}
karnataka_food.update(new_dishes)

#dict can hold different data types
items={"Sugar":1,"bru":1.2,"Bru":True}
print(items)

#Multiple dict in list
item_1={"Sugar":1,"bru":1.2,"Bru":True}
item_2={"Sugar":3,"bru":1.2,"Bru":True}
items=[item_1,item_2]
print(items)
print(f"{item_1["Sugar"]+item_2["Sugar"]}KGS")

