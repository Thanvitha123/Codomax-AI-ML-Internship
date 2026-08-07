# Student Grade Calculator

print("===== Student Grade Calculator =====")

name = input("Enter Student Name: ")

sub1 = float(input("Enter marks for Subject 1: "))
sub2 = float(input("Enter marks for Subject 2: "))
sub3 = float(input("Enter marks for Subject 3: "))
sub4 = float(input("Enter marks for Subject 4: "))
sub5 = float(input("Enter marks for Subject 5: "))

total = sub1 + sub2 + sub3 + sub4 + sub5
percentage = total / 5

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print("\n===== Result =====")
print("Student Name :", name)
print("Total Marks  :", total, "/ 500")
print("Percentage   :", round(percentage, 2), "%")
print("Grade        :", grade)


Output:

===== Student Grade Calculator =====
Enter Student Name: Thanvitha
Enter marks for Subject 1: 95
Enter marks for Subject 2: 88
Enter marks for Subject 3: 91
Enter marks for Subject 4: 84
Enter marks for Subject 5: 90

===== Result =====
Student Name : Thanvitha
Total Marks  : 448.0 / 500
Percentage   : 89.6 %
Grade        : A
