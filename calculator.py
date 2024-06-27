# task 1 CODSOFT
print ("1 addition")
print ("2 subraction")
print("3 multiplication")
print("4 division")

choice = input("Enter your choice: ")
                   
num1= float(input("Enter Number1: "))
num2= float(input("Enter Number2: "))

if choice =="1":
     print(num1,"+",num2,"=",(num1+num2))
elif choice =="2":
     print(num1,"-",num2,"=",(num1-num2))
elif choice =="3":
     print(num1,"*",num2,"=",(num1*num2))
elif choice =="4":
    if num2 == 0.0:
        print("Divide by 0 Error ")
    else:
        print(num1,"/",num2,"=",(num1/num2))
else:
    print("invalic choice")
                                       
                           
                           
                           
