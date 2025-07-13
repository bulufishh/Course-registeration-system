def add_course():
    while True:
        print("\n===== Course Registration =====")
        course_id = input("Enter Course ID: ").strip()
        course_name = input("Enter Course Name: ").strip()
        max_students = input("Enter Maximum Students: ").strip()

        if not course_id or not course_name or not max_students.isdigit():
            print("Error: All fields must be filled. Max students must be a number.")
            continue

        with open("courses.txt", "r") as file:
            existing_courses = file.readlines()
            if any(line.startswith(course_id + ",") for line in existing_courses):
                print(f"Error: Course ID {course_id} already exists.")
                continue

        with open("courses.txt", "a") as file:
            file.write(f"{course_id},{course_name},{max_students}\n")

        print(f"\nCourse added: {course_id}, {course_name}, Max Seats: {max_students}")
        
        if input("Add another course? (yes/no): ").lower() != "yes":
            break
