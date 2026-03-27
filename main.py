import struct
class Student:
def __init__(self):
self.rollno = 0
self.name = ""
self.p_marks = 0
self.c_marks = 0
self.m_marks = 0
self.e_marks = 0
self.cs_marks = 0
self.per = 0.0
self.grade = ''
self.std = 0
def calculate(self):
self.per = (self.p_marks + self.c_marks +
self.m_marks + self.e_marks + self.cs_marks) /
5.0
if self.per >= 60:
self.grade = 'A'
elif 50 <= self.per < 60:
self.grade = 'B'
elif 33 <= self.per < 50:
self.grade = 'C'
else:
self.grade = 'F'
def get_data(self):
self.rollno = int(input("\nEnter The roll
number of student: "))
self.name = input("\nEnter The Name of
student: ")
self.p_marks = int(input("\nEnter The
marks in physics out of 100: "))
self.c_marks = int(input("\nEnter The
marks in chemistry out of 100: "))
self.m_marks = int(input("\nEnter The
marks in maths out of 100: "))
self.e_marks = int(input("\nEnter The
marks in english out of 100: "))
self.cs_marks = int(input("\nEnter The
marks in computer science out of 100: "))
self.calculate()
def show_data(self):
print("\nRoll number of student:",
self.rollno)
print("Name of student:", self.name)
print("Marks in Physics:", self.p_marks)
print("Marks in Chemistry:", self.c_marks)
print("Marks in Maths:", self.m_marks)
print("Marks in English:", self.e_marks)
print("Marks in Computer Science:",
self.cs_marks)
print("Percentage of student is:",
"{:.2f}".format(self.per))
print("Grade of student is:", self.grade)
def show_tabular(self):
print(f"{self.rollno:<10}{self.name:<15}{self.p_
marks:<3}{self.c_marks:<3}{self.m_marks:<3}
"
f"{self.e_marks:<3}{self.cs_marks:<3}{'{:.2f}'.f
ormat(self.per):<6} {self.grade}")
def ret_rollno(self):
return self.rollno
def write_student(self):
with open("student.dat", "ab") as fp:
st = Student()
st.get_data()
fp.write(st.__dict__)
print("\n\nstudent record has been created
")
def display_all(self):
print("\n\n\n\t\tDISPLAY ALL RECORD
!!!\n\n")
try:
with open("student.dat", "rb") as fp:
while True:
st_data = fp.read(172) # Assuming
172 bytes is the size of the serialized Student
object
if not st_data:
break
st = Student()
st.__dict__ = st_data
st.show_data()
print("\n\n===========================
=========\n")
input("Press Enter to continue...")
except FileNotFoundError:
print("File not found.")
except Exception as e:
print("An error occurred:", e)
def display_sp(n):
flag = 0
try:
with open("student.dat", "rb") as fp:
while True:
st_data = fp.read(172)
if not st_data:
break
st = Student()
st.__dict__ = st_data
if st.ret_rollno() == n:
st.show_data()
flag = 1
except FileNotFoundError:
print("File not found.")
except Exception as e:
print("An error occurred:", e)
if flag == 0:
print("\n\nrecord not exist")
input("Press Enter to continue...")
def modify_student():
no, found = 0, 0
print("\n\n\tTo Modify ")
no = int(input("\n\n\tPlease Enter The roll
number of student: "))
try:
with open("student.dat", "rb+") as fp:
while True:
st_data = fp.read(172)
if not st_data:
break
st = Student()
st.__dict__ = st_data
if st.ret_rollno() == no:
st.show_data()
print("\nPlease Enter The New
Details of student")
st.get_data()
pos = -172
fp.seek(pos, 1)
fp.write(st.__dict__)
print("\n\n\t Record Updated")
found = 1
break
except FileNotFoundError:
print("File not found.")
except Exception as e:
print("An error occurred:", e)
if found == 0:
print("\n\n Record Not Found ")
input("Press Enter to continue...")
def delete_student():
no = 0
print("\n\n\n\tDelete Record")
no = int(input("\n\nPlease Enter The roll
number of student You Want To Delete: "))
try:
with open("student.dat", "rb+") as fp:
with open("Temp.dat", "wb") as fp2:
fp.seek(0)
while True:
st_data = fp.read(172)
if not st_data:
break
st = Student()
st.__dict__ = st_data
if st.ret_rollno() != no:
fp2.write(st_data)
fp2.close()
fp.close()
import os
os.remove("student.dat")
os.rename("Temp.dat", "student.dat")
print("\n\n\tRecord Deleted ..")
except FileNotFoundError:
print("File not found.")
except Exception as e:
print("An error occurred:", e)
input("Press Enter to continue...")
def class_result():
try:
with open("student.dat", "rb") as fp:
print("\n\n\t\tALL STUDENTS RESULT
\n\n")
print("==============================
======================")
print("Roll No. Name P C M E
CS %age Grade")
print("==============================
======================")
while True:
st_data = fp.read(172)
if not st_data:
break
st = Student()
st.__dict__ = st_data
st.show_tabular()
except FileNotFoundError:
print("File not found.")
except Exception as e:
print("An error occurred:", e)
input("Press Enter to continue...")
def result():
ans, rno = 0, 0
ch = ''
print("\n\n\nRESULT MENU")
print("\n\n\n1. Class Result\n\n2. Student
Report Card\n\n3.Back to Main Menu")
ans = int(input("\n\n\nEnter Choice (1/2): "))
if ans == 1:
class_result()
elif ans == 2:
while True:
print("\n\nEnter Roll Number Of
Student: ")
rno = int(input())
display_sp(rno)
print("\n\nDo you want to See More
Result (y/n)?")
ch = input().lower()
if ch != 'y':
break
def entry_menu():
ch2 = ''
print("\n\n\n\tENTRY MENU")
print("\n\n\t1.CREATE STUDENT
RECORD")
print("\n\n\t2.DISPLAY ALL STUDENTS
RECORDS")
print("\n\n\t3.SEARCH STUDENT RECORD
")
print("\n\n\t4.MODIFY STUDENT
RECORD")
print("\n\n\t5.DELETE STUDENT
RECORD")
print("\n\n\t6.BACK TO MAIN MENU")
ch2 = input("\n\n\tPlease Enter Your Choice
(1-6): ")
if ch2 == '1':
Student().write_student()
elif ch2 == '2':
Student().display_all()
elif ch2 == '3':
num = int(input("\n\n\tPlease Enter The roll
number: "))
display_sp(num)
elif ch2 == '4':
modify_student()
elif ch2 == '5':
delete_student()
while True:
print("\n\n\n\tMAIN MENU")
print("\n\n\t01. RESULT MENU")
print("\n\n\t02. ENTRY/EDIT MENU")
print("\n\n\t03. EXIT")
ch = input("\n\n\tPlease Select Your Option
(1-3): ")
if ch == '1':
result()
elif ch == '2':
entry_menu()
elif ch == '3':
break
else:
print("\a")
