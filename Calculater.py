#full calculator 
a= input("What Operation You Want:+ - */")
b=int(input("enter 1st number:"))
c=int(input("enter 2nd number"))
if a=="+" :
print("your sum is:",b+c)
elif a=="-":
print("you subtraction is:",b-c)
elif a=="*":
print("multiplication is:",b*c)
elif a=="/":
print("division is:",b/c)
   else:
    print ("check your operator")

