students={}
n=int(input("Enter the number of subjects="))
for i in range(n):
    sub=input(f"Enter the subject{i+1}=")
    marks=int(input(f"Enter the marks{i+1}="))
    students[sub]=marks
print("\n----------STUDENT MARKS DICTIONARY------------\n")
total=0
for sub,marks in students.items():
    print(sub,":",marks)
total+=marks
print("Total=",total)
print("Average=",total/n)
