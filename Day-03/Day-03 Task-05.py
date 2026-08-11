age=int(input("Enter you Age: "))
id_card=int(input("1.YES\n2.NO\nEnter your choice: "))
if age<=18 and id_card==1:
    print("You get a Student discount.")
else:
    print("No student discount.")