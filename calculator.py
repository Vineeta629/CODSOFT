print("1addition")
print("2subraction")
print("3multiplication")
print("4division")
choice =input("enter your choice:")
num1= float(input("enter num 1:"))
num2= float(input("enter num 2:"))
if choice =="1":
    print(num1,"+",num2,"=",(num1+num2))
elif choice =="2":
    print(num1,"-",num2,"=",(num1-num2))
elif choice=="3":
    print(num1,"*",num2,"=",(num1*num2))
elif choice=="4":
     if num2 == 0.0:
        print ("divid eby 0 error")
     else:
        print(num1,"/",num2,"=",(num1/num2))
else:
    print("invalic choice")
