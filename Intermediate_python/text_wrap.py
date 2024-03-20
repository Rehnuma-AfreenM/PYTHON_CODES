string = input("enter the string: ")
max_wrap = int(input("enter the number: "))
while string :
    st = string[:max_wrap]
    string = string[max_wrap-1:]
    print(st)
