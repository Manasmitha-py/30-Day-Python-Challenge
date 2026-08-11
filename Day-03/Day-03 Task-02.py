num=int(input("Enter a number: "))
if num>0:
    print(f"The number you entered is {num}.It is Positive.")
elif num<0:
    print(f"The number you entered is {num}.It is Negative.")
elif num==0:
    print(f"The number you entered is {num}.")
else:
    print("Invalid Input")