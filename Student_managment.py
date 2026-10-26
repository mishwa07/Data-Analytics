students = []

def add_student():
    rollno = input("Enter your rollno :-")

    for st in students:
        if st["rollno"] == rollno:
            print("student rollno already exists")
            return
    
    name = input("Enter student Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")

    student= {
        "rollno":rollno,
        "name": name,
        "age": age,
        "course": course,
        
    }
    students.append(student)
    print("Student added successfully!")
    

def view_students():

    print("\n===== Student Records =====")

    for st in students:
        print("\nRoll Number:",st["rollno"])
        print("Name:", st["name"])
        print("Age:", st["age"])
        print("Course:",st["course"])


def search_student():

    rollno = input("Enetr your rollno :-")

    for st in students:
        if st["rollno"] == rollno:
            print("Rollno",st["rollno"])
            print("name:",st["name"])
            print("age:",st["age"])
            print("course:",st["course"])
            return
        else:
            print("Student not found !!!!!")

def update_student():
    rollno = input("Enter your rollno :-")

    for st in students:
        if st["rollno"] == rollno:
            name = input("Enter new name:- ")
            age = input("Enetr new age:-")
            course = input("Enter new course:-")

            if name:
                st["name"]=name

            if age:
                st["age"]=age

            if course:
                st["course"]=course

            print("Student Details Update Sucessfully")
            return

        else:
            print("Student Not found")               


def delete_student():

    rollno = input("Enter your rollno:-")

    for st in students:
        if st["rollno"] == rollno:

            choice = input("do you want to delete student ?yes /no :-").lower()

            if choice == "yes":
                students.remove(st)
                print("Student deleted successfully!")
                return
            else:    
                print("Student is not found")



while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter Your Choice:- ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("Thank you for using the system!")
        break
    else:
        print("Invalid choice! Please try again.")