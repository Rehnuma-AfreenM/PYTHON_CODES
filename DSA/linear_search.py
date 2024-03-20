def linearSearch(list, target): 
    for i in range(0,len(list)):
        if list[i]== target:
            print(i)
    print(None)  

numbers = [i for i in range(0,12)]

linearSearch(numbers, 12)