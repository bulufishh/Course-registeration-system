def view_available_courses():
    print("\n===== Available Courses =====\n")
    try:
        with open("courses.txt", "r") as file:
            print("{:<10} {:<30} {:<15}".format("Course ID", "Course Name", "Seats"))
            print("-" * 60)
            for line in file:
                course_id, name, seats = line.strip().split(",")
                print("{:<10} {:<30} {:<15}".format(course_id, name, seats))
    except FileNotFoundError:
        print("Error: courses.txt not found.")
