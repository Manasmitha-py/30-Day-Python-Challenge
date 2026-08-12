#discount checker 
name=input("Enter your name: ")
age=int(input("Enter your age: "))
if age<18 and "a" in name:
    print("Eligible for student discount.")
else:
    print("Not eligible for student discount.")
