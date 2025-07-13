def add_student():
    with open("students.txt", "a") as file:  
        while True:
            print("\n===== Student Registration =====")
            print("1. Add Student")
            print("2. Exit")
            
            choice = input("Enter your choice (1/2): ")
            if choice == "1":
                student_id = input("Enter Student ID: ")
                if not student_id.isdigit():
                    print("Error: Student ID must be numeric.")
                    continue
                
                student_name = input("Enter Student Name: ")
                if any(char.isdigit() for char in student_name):
                    print("Error: Name cannot contain numbers.")
                    continue
                
                student_contact = input("Enter Student Contact: ")
                if not student_contact.isdigit():
                    print("Error: Contact must be numeric.")
                    continue

                file.write(f"{student_id},{student_name},{student_contact}\n")
                print("\nStudent details recorded:")
                print(f"ID: {student_id}, Name: {student_name}, Contact: {student_contact}")
            elif choice == "2":
                print("Records Ended.")
                break
            else:
                print("Invalid choice. Please enter 1 or 2.")
