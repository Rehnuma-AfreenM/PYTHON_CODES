#Dictionary: key-value pairs, unordered, Mutable
#defining a dictionary.
#One way
mydict = {"name":"Rehnuma", "age": 22, "city": "Jhansi"}
print(mydict)
#Another way
mydict2 = dict(name ="Simmi",age = 18, city = "Bhopal", email = "simmi@gmail.com")
print(mydict2)

#accesing the value.
value = mydict["name"]
print(value)

#adding value in dictionary.

mydict["email"] = "rehnuma@gmail.com"
print(mydict) 

#overwritng the value.
mydict["email"] = "rehnumaafreen@gmail.com"
print(mydict) 

#deleting an item.
del mydict["email"]
print(mydict)

mydict.pop("age")
print(mydict)

mydict.popitem()
print(mydict)

#check for item in dictionary.
if "name" in mydict:
    print(mydict["name"])

try:
    print(mydict["name"])
except:
    print("Error") 
    
#looping through the dictionary.
mydict = {"name":"Rehnuma", "age": 22, "city": "Jhansi"}
for i in mydict.items():
    print(i)     
    
for i in mydict.keys():
    print(i)           
    
for i in mydict.values():
    print(i)     
    
for key, value in mydict.items():
    print(key, value)     
    
#coping the dictionary.
mydict_copy = mydict   #Both dictionaries point to the same dictionary in the memory.
print(mydict)
print(mydict_copy)

#any change in the copied dictionary will be reflected in the original dictionary. 
mydict_copy["email"] = "rehnuma@gmail.com"    
print(mydict_copy)
print(mydict)

#coping the dictionary without changing the original.
mydict_copy1 = mydict.copy()
mydict_copy1["place"] = "earth"    
print(mydict_copy1)
print(mydict)

#or
mydict_copy2 = dict(mydict)
mydict_copy2["food"] = "cake"    
print(mydict_copy2)
print(mydict)

#merging two dictionaries.

mydict = {"name":"Rehnuma", "age": 22, "city": "Jhansi"}
print(mydict)
mydict2 = dict(name ="Simmi",age = 18, city = "Bhopal", email = "simmi@gmail.com")
mydict.update(mydict2)
print(mydict)

#keys can be of immutable data type like numbers,tuples and strings.
mydict5 = {(2,3):6, (3,4):12}
print(mydict5)
print(mydict5.keys())

mydict6 = {2:4, 3:9, 4:16}
print(mydict6)