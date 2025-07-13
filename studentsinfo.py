def students_information():
    try:
        with open("students.txt", "r") as file:
            lines = file.readlines()
        if not lines:
            print("No students found.")
            return

        print("\n===== List of All Students =====")
        print("{:<15} {:<30} {:<20}".format("Student ID", "Student Name", "Contact"))
        print("-" * 65)

        for line in lines:
            sid, name, contact = line.strip().split(",")
            print("{:<15} {:<30} {:<20}".format(sid, name, contact))
    except FileNotFoundError:
        print("Error: students.txt not found.")
