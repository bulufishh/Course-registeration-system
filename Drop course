def drop_course_system():
    print("\n===== Drop a Course =====")
    student_id = input("Enter your Student ID: ")
    course_id = input("Enter the Course ID to drop: ")

    updated_enrollments = []
    found = False

    with open("enrollments.txt", "r") as file:
        for line in file:
            sid, _, cid = line.strip().split(",")
            if sid == student_id and cid == course_id:
                found = True
            else:
                updated_enrollments.append(line)

    if not found:
        print("Enrollment not found.")
        return

    with open("enrollments.txt", "w") as file:
        file.writelines(updated_enrollments)

    print("Course successfully dropped.")
