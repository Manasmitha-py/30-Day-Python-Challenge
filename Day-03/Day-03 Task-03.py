#Even or Odd + Positive/Negative.
num=int(input("Enter the Integer: "))
if num>0:
    print(f"The number {num} is positive")
    if num%2==0:
        print(f"The number {num} is Even.")
    elif num%2!=0:
        print(f"The number {num} is Odd.")
elif num<0:
    print(f"The number {num} is negative.")
    if num%2==0:
        print(f"The number {num} is Even.")
    elif num%2!=0:
        print(f"The number {num} is Odd.")
else:
    print(f"The number {num} is Zero.")