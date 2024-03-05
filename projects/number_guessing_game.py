import random
num = random.randint(0,10) 
while True:
    user_num = int(input("Guess a number between (0 - 10): "))
    if user_num<0:
        print("Your number is less than zero")
    elif user_num>10:
        print(" Your number is greater than 100")    

    elif user_num > num:
        print(" Your number is higher than the target number")
    
    elif user_num < num:
        print("Your number is lower than the target number") 
      
    elif user_num == num:
        print(str(user_num) + " is the Correct number") 
        quit()
quit()
