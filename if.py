name=input("please enter your name \n ")
gender=input("please enter your Gender  \n ")
age=int(input("please enter your age  \n "))
print("Dear " , name) 
if(age>=18):
   
    print(" congratulation you are eligible for cnic  ")
elif(age>=12):
    print("just testing purpose ")
else:
    print("you are eligible for B Form not for CNIC ")