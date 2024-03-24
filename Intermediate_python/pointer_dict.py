dict1 = {'value': 11}
dict2 = dict1
print("before dict2 value is updated:")
print("dict1=", dict1)
print("dict2=", dict2)

print("\ndict1 points to: ", id(dict1))
print("\ndict2 points to: ", id(dict2))

dict2['value'] = 12

print("after dict2 value is updated:")
print("dict1=", dict1)
print("dict2=", dict2)

print("\ndict1 points to: ", id(dict1))
print("\ndict2 points to: ", id(dict2))



