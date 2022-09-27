class Student:
    
    total_enrolled_students = 0
    total_student = 0

    # Setting the values of the object
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

    # Function to print the object
    def __str__(self):
        return f"Student: {self.name}, G{str(self.g_num).zfill(5)}, {self.major}, Active = {self.enrolled_status}, Credits = {self.credits}, GPA = {self.get_gpa():.2f}"
        
    # Check if the student is enrolled or not
    def is_enrolled(self):
        return self.enrolled_status == 'y'

    # Function to Check if Both Students are same
    def same_student(self, other):
        if self.g_num == other.g_num and self.name == other.name:
            return True

    # Function to Calculate GPA
    def get_gpa(self):
        # Division by Zero Error Handled Here
        if self.credits == 0:
            return 0
        else:
            return self.points / self.credits

    # Check if the student is Senior, Junior, Sophomore or Freshman based on the credits
    def get_status(self):
        if self.credits >= 90:
            return 'Senior'
        elif self.credits >= 60:
            return 'Junior'
        elif self.credits >= 30:
            return 'Sophomore'
        else:
            return 'Freshman'

    # Print Total Number of Enrolled Students
    @staticmethod
    def get_total_enrolled_students():
        return Student.total_enrolled_students
    
    # Print Total Number of Students
    @staticmethod
    def get_total_students():
        return Student.total_student
    


# Main Function
if __name__ == '__main__':
    # Creating the Objects
    s1 = Student('David Miller', 'Hist', 'y', 0, 0)
    s2 = Student('Sonia Fillmore', 'Math', 'y', 90, 315)
    s3 = Student('A. Einstein', 'Phys', 'y', 0, 0)
    s4 = Student('W. A. Mozart', 'Mus', 'n', 29, 105)
    s5 = Student('Sonia Fillmore', 'CSci', 'y', 60, 130)
    s5.g_num = s2.g_num
    s6 = Student('Pierre Renoir', 'Art', 'y', 120, 315)
    s7 = Student('Test Student 01', 'History', 'n', 29, 105)
    s8 = Student('Test Student 02', 'Art', 'n', 29, 105)

    # Printing the Objects
    print(s1)
    print(s2)
    print(s3)
    print(s4)
    print(s5)
    print(s6)
    print(s7)
    print(s8)
    
    # Printing the Total Number of Students
    print('\n \nTotal Students: ', Student.get_total_students())

    # Printing the Total Number of Enrolled Students
    print('Total Enrolled Students: ', Student.get_total_enrolled_students())

    # Printing the GPA of the Student
    print('GPA of ', s1.name, ' is ', s1.get_gpa())

    # Printing the Status of the Student
    print('Class standing of ', s4.name, ' is ', s4.get_status())
    print('Class standing of ', s2.name, ' is ', s2.get_status())
    
    # Checking if the Students are same or not
    if s1.same_student(s2):
        print (s1.name, ' and ', s2.name, ' are the same student')
    else:
        print (s1.name, ' and ', s2.name, ' are not the same student')
    if s2.same_student(s5):
        print (s2.name, ' and ', s5.name, ' are the same student')
    else:
        print (s2.name, ' and ', s5.name, ' are not the same student')

    # Checking is the Student is enrolled or not
    if s1.is_enrolled():
        print (s1.name, ' is currently active')
    else:
        print (s1.name, ' is not currently active')
    if s4.is_enrolled():
        print (s4.name, ' is currently active')
    else:
        print (s4.name, ' is not currently active')

    print('\nEnd of A2 Student class demo')