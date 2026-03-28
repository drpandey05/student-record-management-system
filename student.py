import os
import pickle

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

    def calculate(self):
        self.per = (self.p_marks + self.c_marks +
                    self.m_marks + self.e_marks + self.cs_marks) / 5.0
        if self.per >= 60:
            self.grade = 'A'
        elif 50 <= self.per < 60:
            self.grade = 'B'
        elif 33 <= self.per < 50:
            self.grade = 'C'
        else:
            self.grade = 'F'

    def get_data(self):
        self.rollno = int(input("\nEnter The roll number of student: "))
        self.name = input("\nEnter The Name of student: ")
        self.p_marks = int(input("\nEnter The marks in physics out of 100: "))
        self.c_marks = int(input("\nEnter The marks in chemistry out of 100: "))
        self.m_marks = int(input("\nEnter The marks in maths out of 100: "))
        self.e_marks = int(input("\nEnter The marks in english out of 100: "))
        self.cs_marks = int(input("\nEnter The marks in computer science out of 100: "))
        self.calculate()

    def show_data(self):
        print("\nRoll number of student:", self.rollno)
        print("Name of student:", self.name)
        print("Marks in Physics:", self.p_marks)
        print("Marks in Chemistry:", self.c_marks)
        print("Marks in Maths:", self.m_marks)
        print("Marks in English:", self.e_marks)
        print("Marks in Computer Science:", self.cs_marks)
        print("Percentage of student is:", "{:.2f}".format(self.per))
        print("Grade of student is:", self.grade)

    def show_tabular(self):
        print(f"{self.rollno:<10}{self.name:<15}{self.p_marks:<5}{self.c_marks:<5}"
              f"{self.m_marks:<5}{self.e_marks:<5}{self.cs_marks:<5}"
              f"{'{:.2f}'.format(self.per):<10}{self.grade}")

    def ret_rollno(self):
        return self.rollno


def write_student():
    with open("student.dat", "ab") as fp:
        st = Student()
        st.get_data()
        pickle.dump(st, fp)
    print("\n\nStudent record has been created")


def display_all():
    print("\n\n\n\t\tDISPLAY ALL RECORD !!!\n\n")
    try:
        with open("student.dat", "rb") as fp:
            while True:
                try:
                    st = pickle.load(fp)
                    st.show_data()
                    print("\n\n" + "=" * 35 + "\n")
                except EOFError:
                    break
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
                try:
                    st = pickle.load(fp)
                    if st.ret_rollno() == n:
                        st.show_data()
                        flag = 1
                except EOFError:
                    break
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", e)
    if flag == 0:
        print("\n\nRecord not found")
    input("Press Enter to continue...")


def modify_student():
    found = 0
    print("\n\n\tTo Modify")
    no = int(input("\n\n\tPlease Enter The roll number of student: "))
    students = []
    try:
        with open("student.dat", "rb") as fp:
            while True:
                try:
                    students.append(pickle.load(fp))
                except EOFError:
                    break
        for st in students:
            if st.ret_rollno() == no:
                st.show_data()
                print("\nPlease Enter The New Details of student")
                st.get_data()
                found = 1
                break
        if found:
            with open("student.dat", "wb") as fp:
                for st in students:
                    pickle.dump(st, fp)
            print("\n\n\tRecord Updated")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", e)
    if found == 0:
        print("\n\nRecord Not Found")
    input("Press Enter to continue...")


def delete_student():
    print("\n\n\n\tDelete Record")
    no = int(input("\n\nPlease Enter The roll number of student You Want To Delete: "))
    students = []
    try:
        with open("student.dat", "rb") as fp:
            while True:
                try:
                    st = pickle.load(fp)
                    if st.ret_rollno() != no:
                        students.append(st)
                except EOFError:
                    break
        with open("student.dat", "wb") as fp:
            for st in students:
                pickle.dump(st, fp)
        print("\n\n\tRecord Deleted ..")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", e)
    input("Press Enter to continue...")


def class_result():
    try:
        with open("student.dat", "rb") as fp:
            print("\n\n\t\tALL STUDENTS RESULT\n\n")
            print("=" * 54)
            print(f"{'Roll No.':<10}{'Name':<15}{'P':<5}{'C':<5}{'M':<5}{'E':<5}{'CS':<5}{'%age':<10}{'Grade'}")
            print("=" * 54)
            while True:
                try:
                    st = pickle.load(fp)
                    st.show_tabular()
                except EOFError:
                    break
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", e)
    input("Press Enter to continue...")


def result():
    print("\n\n\nRESULT MENU")
    print("\n\n1. Class Result\n\n2. Student Report Card\n\n3. Back to Main Menu")
    ans = int(input("\n\n\nEnter Choice (1-3): "))
    if ans == 1:
        class_result()
    elif ans == 2:
        while True:
            rno = int(input("\n\nEnter Roll Number Of Student: "))
            display_sp(rno)
            ch = input("\n\nDo you want to See More Result (y/n)? ").lower()
            if ch != 'y':
                break


def entry_menu():
    print("\n\n\n\tENTRY MENU")
    print("\n\n\t1. CREATE STUDENT RECORD")
    print("\n\n\t2. DISPLAY ALL STUDENTS RECORDS")
    print("\n\n\t3. SEARCH STUDENT RECORD")
    print("\n\n\t4. MODIFY STUDENT RECORD")
    print("\n\n\t5. DELETE STUDENT RECORD")
    print("\n\n\t6. BACK TO MAIN MENU")
    ch2 = input("\n\n\tPlease Enter Your Choice (1-6): ")
    if ch2 == '1':
        write_student()
    elif ch2 == '2':
        display_all()
    elif ch2 == '3':
        num = int(input("\n\n\tPlease Enter The roll number: "))
        display_sp(num)
    elif ch2 == '4':
        modify_student()
    elif ch2 == '5':
        delete_student()


# Main loop
while True:
    print("\n\n\n\tMAIN MENU")
    print("\n\n\t01. RESULT MENU")
    print("\n\n\t02. ENTRY/EDIT MENU")
    print("\n\n\t03. EXIT")
    ch = input("\n\n\tPlease Select Your Option (1-3): ")
    if ch == '1':
        result()
    elif ch == '2':
        entry_menu()
    elif ch == '3':
        break
    else:
        print("\a")