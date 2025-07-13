def enroll_in_course():
    print("\n===== Course Enrollment =====")
    student_id = input("Enter Student ID: ").strip()
    student_name = input("Enter Student Name: ").strip()
    course_id = input("Enter Course ID to Enroll In: ").strip()

    if not student_id or not student_name or not course_id:
        print("Error: All fields are required.")
        return

    # Check if course exists and seats are available
    updated_courses = []
    course_found = False
    with open("courses.txt", "r") as file:
        for line in file:
            existing_id, name, max_seats = line.strip().split(",")
            if existing_id == course_id:
                course_found = True
                max_seats = int(max_seats)
                enrolled = sum(1 for l in open("enrollments.txt") if l.split(",")[2].strip() == course_id)
                if enrolled >= max_seats:
                    print(f"Error: Course '{name}' is full.")
                    return
            updated_courses.append(line)

    if not course_found:
        print(f"Error: Course ID '{course_id}' not found.")
        return

    # Check if already enrolled
    with open("enrollments.txt", "r") as file:
        for line in file:
            s_id, _, c_id = line.strip().split(",")
            if s_id == student_id and c_id == course_id:
                print("Error: Student already enrolled in this course.")
                return

    # Append enrollment
    with open("enrollments.txt", "a") as file:
        file.write(f"{student_id},{student_name},{course_id}\n")
    
    print("Enrollment successful.")
