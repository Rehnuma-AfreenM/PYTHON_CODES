#Tuples are ordered, immutable and allows duplicate elements

#varaible containing string.
mytuple = "rehnuma"
print(type(mytuple))
print(mytuple)

#tuple with one element without parenthesis.
mytuple1 = "rehnuma",
print(type(mytuple1))
print(mytuple1)

#tuple with one element.
mytuple2 = ("rehnuma",)
print(type(mytuple2))
print(mytuple2)

#tuples can have different type of elements.
mytuple3 = ("rehnuma",34,"boston")
print(type(mytuple3))
print(mytuple3)

#tuples can be defined without parenthesis.
mytuple4 = "red",32,"blue"
print(type(mytuple4))
print(mytuple4)

#converting iterable into a tuple.
mytuple5 = tuple(["max", "well",45])
print(mytuple5)
#or
mylist = ["max", "well","egg",45, 45]
print(mylist)
print(type(mylist))

mytuple6 = tuple(mylist)
print(mytuple6)
print(type(mytuple6))

#accessing the elements of tuple.
item = mytuple6[-2]
print(item) 

#iterating a tuple.
for i in mytuple6:
    print(i)

#Check if an item exists in tuple.
if "banana" in mytuple6:
    print("yes")
else:
    print("no")   
    
#length of a tuple.
print(len(mytuple6))

#counting the no. of times an item occur in tuple.
print(mytuple6.count(45))

#get the index of an element.
print(mytuple6.index(45)) #if element occur more than once then it will give the first occurence index.

#convert tuple to a list.
b = ("a","p", "p", "l", "e")
print(b)
print(type(b))
a= list(b)
print(a)
print(type(a))

#slicing with tuple.
c = b[0:3] 
print(c) 
d = b[::-1]  
print(d) 

#tuple unpacking .
name,age,city = mytuple3
print(name)          
print(age) 
print(city) 

id1,*id2,id3 = b
print(id1)
print(id2)
print(id3)

import sys
print(sys.getsizeof(mylist),"bytes")
print(sys.getsizeof(mytuple6),"bytes")

import timeit
print(timeit.timeit(stmt="[0,1,2,3,4,5]", number = 100))
print(timeit.timeit(stmt="(0,1,2,3,4,5)", number = 100))