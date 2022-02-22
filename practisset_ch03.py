# a=input("enter the name that you want to print ")
# print(a)


# second Question of chapter three section 
letter= '''  Dear    <!name!>    
you are selected  
<date>      '''
name= input("enter your name ")
letter =letter.replace("<!name!>",name)

date=input ("enter your date ")
letter=letter.replace("<date> ",date)
print("here is general format \n ",letter)