import random
num = random.randint(0,100) 

def is_integer(input_str):
    if input_str.startswith('-'):
        return input_str[1:].isdigit()
    return input_str.isdigit()

while True:
    user_num = input("Guess a number between (0 - 100): ")
    if is_integer(user_num):
        user_num =int(user_num)  
        if user_num < 0:
            print("Your number should not be less than zero")
        elif user_num > 100:
            print(" Your number should not be greater than 100")    
        elif user_num > num:
            print(" Your number is higher than the target number")
        elif user_num < num:
            print("Your number is lower than the target number") 
        elif user_num == num:
            print(str(user_num) + " you are correct")
            quit()   
    else:
        print("Please enter a number!")          
quit()      