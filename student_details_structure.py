# student_details_structure.py
# Student details using dictionary
student1 = {
    "first_name": "Feyza",
    "last_name": "Balaban",
    "index_number": "35458",
    "nationality": "Turkish",
    "starting_date": "2023-09-01",
    "courses": ["Mathematics", "Computer Science"]
}

# Display student's data
print("Student Details:")
print("First Name:", student1["first_name"])
print("Last Name:", student1["last_name"])
print("Index Number:", student1["index_number"])
print("Nationality:", student1["nationality"])
print("Starting Date:", student1["starting_date"])
print("Courses:", ", ".join(student1["courses"]))
