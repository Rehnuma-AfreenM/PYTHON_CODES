def getthestring():
    s = input()
    characters = list(s)
    L = ""
    for i in characters:
        if i.isupper() == True:
            i=i.lower()
            L +=i 
        else:
           i=i.upper() 
           L +=i 
    print(L)
    
getthestring()