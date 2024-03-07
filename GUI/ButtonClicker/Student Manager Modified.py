from tkinter import *


class Student:
   
   
    def __init__(self, name):
        self.first_name = name
       
    def display_name(self):
        print(self.first_name)
       
    def set_grade(self, grade):
        self.grade = grade
       
    def get_grade(self):
        return self.grade
       
def show_grade():
    grade_label.config(text=csc_2(1). get_grade())
       
       
csc_2 = []




csc_2.append(Student("Kajah"))
csc_2[0].set_grade("Not Achieved")


csc_2.append(Student("Boaz"))
csc_2[0].set_grade("Developing")


window = Tk()
window.geometry("300x300")


grade_label = Label()
grade_label.pack()




show_grade_btn = Button(text="Show grade")
