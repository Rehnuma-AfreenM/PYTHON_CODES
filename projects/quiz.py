answer = input("Do you want to play the Capital quiz Game!: ")
if answer.upper() == "YES":
    print("Ok let's play") 
else:
    quit()
        
marks = 0   
    
answer = input("what is the capital of India: " ) 
if answer.lower() == "delhi":
    print("Correct Answer!")
    marks+=1
else:
    print("Wrong answer")        
        
answer = input("what is the capital of Uttar Pradesh: " ) 
if answer.lower() == "lucknow":
    print("Correct Answer!")
    marks+=1
else:
    print("Wrong answer")        
                
answer = input("what is the capital of Madhya Pradesh: " ) 
if answer.lower() == "bhopal":
    print("Correct Answer!")
    marks+=1
else:
    print("Wrong answer")        
              
answer = input("what is the capital of Bihar: " ) 
if answer.lower() == "patna":
    print("Correct Answer!")
    marks+=1
else:
    print("Wrong answer")   
    
print("You got "+ str(marks)+ " Correct amswers")
print("Your percentage is "+ str((marks/4)*100) + "%")         
                        