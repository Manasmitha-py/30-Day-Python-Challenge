name=input("Students name: ")
marks_1=int(input("Enter the marks of subject 1: "))
marks_2=int(input("Enter the marks of subject 2: "))
marks_3=int(input("Enter the marks of subject 3: "))
total_marks=marks_1 + marks_2 + marks_3
print(total_marks)
avg_marks=(total_marks/3)
print(avg_marks)
if avg_marks >=85:
    print("Excellent")
elif avg_marks>=60:
    print("Good")
else:
    print("Needs Improvement")
