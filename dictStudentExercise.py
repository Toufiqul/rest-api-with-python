student = {
    "name": "Jose",
    "school": "Computing",
    "grade": (66,77,88)
}

def avg_grade(data):
    grades = data["grade"]
    return sum(grades) / len(grades)

def avg_grade_class(studentList):
    total = 0
    count = 0
    for student in studentList:
        total += avg_grade(student)
    return total / len(studentList)