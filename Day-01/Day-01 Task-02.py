first_num=int(input("Enter the first number: "))
second_num=int(input("Enter the second number: "))
choice=int(input("1.Add\n 2.Sub\n 3.Multi\n 4.Divi\n Enter your choice: "))
if choice==1:
    print("Addition is: ",first_num+second_num)
elif choice==2:
    print("Subtraction: ",first_num-second_num)
elif choice==3:
    print("Multiplication: ",first_num*second_num)
elif choice==4:
    print("Division: ",first_num/second_num)
else:
    print("Invalid choice")
