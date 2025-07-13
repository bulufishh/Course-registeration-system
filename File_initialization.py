import os

students = "students.txt"
courses = "courses.txt"
enrollments = "enrollments.txt"

for file in [students, courses, enrollments]:
    if not os.path.exists(file):
        open(file, "w").close()
