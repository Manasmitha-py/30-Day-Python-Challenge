#largest of three numbers use >= TO GET ACURATE ANSWER 
num_1=int(input("Enter the first number: "))
num_2=int(input("Enter the second number: "))
num_3=int(input("Enter the value of third number: "))
if num_1>num_2 and num_1>num_3:
    print(f"The largest number is {num_1}.")
elif num_2>num_1 and num_2>num_3:
    print(f"The largest number is {num_2}.")
else:
    print(f"The largest number is {num_3}.")