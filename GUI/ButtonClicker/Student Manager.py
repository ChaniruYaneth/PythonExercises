class Student:
   
   
    def __init__(self):
        self.first_name = "John"
       
    def display_name(self):
        print(self.first_name)
       
    def set_grade(self, grade):
        self.grade = grade
       
    def display_grade(self):
        print(self.grade)
       
       
csc_level_2.append = (Student("Bilal"))
csc_level_2.append = (Student("Anna"))
csc_level_2.append = (Student("Melissa"))
csc_level_2.append = (Student("Priya"))


csc_level_2[0].display_name()
csc_level_2[0].set_grade("Excellence")
csc_level_2[1].display_grade()
