from tkinter import *


class Student:
   
    def __init__(self, name):
        self.name = name
        self.grade = "" 
   
    def get_grade(self):
        return self.grade
       
    def set_grade(self, grade):
        self.grade = grade
       
       
def show_grade():
    global grade_label 
    selected_index = students_listbox.curselection()[0]
    selected_student = csc_2[selected_index]
    grade_label.config(text=selected_student.get_grade())
       
       
csc_2 = []


csc_2.append(Student("Boaz"))
csc_2[0].set_grade("Achieved")

csc_2.append(Student("Rehaan"))
csc_2[1].set_grade("Excellence")

csc_2.append(Student("Aaron"))
csc_2[2].set_grade("Merit")


window = Tk()
window.geometry("300x300")


students_listbox = Listbox(window)
students_listbox.pack()

students_listbox.insert(0, "Boaz")
students_listbox.insert(0, "Rehaan")
students_listbox.insert(0, "Aaron")


grade_label = Label(window) 
grade_label.pack()


show_grade_btn = Button(window, text="Show Grade", command=show_grade)
show_grade_btn.pack()

window.mainloop()
