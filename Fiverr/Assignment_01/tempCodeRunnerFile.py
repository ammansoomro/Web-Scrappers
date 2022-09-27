class Student:
    
    total_enrolled_students = 0
    total_student = 0
    def __init__(self, name, major, enrolled_status, credits, points):
        Student.total_student += 1
        self.name = name
        self.major = major
        self.enrolled_status = enrolled_status
        self.credits = credits
        self.points = points
        self.g_num = Student.total_student
        if self.is_enrolled():
            Student.total_enrolled_students += 1