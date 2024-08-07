#Student_client.py

from student_class import Student

s1 = Student("bob benavides", 65)
s2 = Student("mellisa gonzales", 17)

print("Report - Student Information: " )

s1.describe_student()
s2.describe_student()

s1.set_age(-10)
s2.set_age(13)

#s2.set_name("")
s2.set_name("melisa cantu")

s1.describe_student()
s2.describe_student()

print()