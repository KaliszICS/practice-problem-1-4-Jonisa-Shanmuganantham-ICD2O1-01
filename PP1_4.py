'''
    Lesson: Input and F strings
    Author: Jonisa Shanmuganantham
    Date Created: Sept 19, 2024
    Date Last Modified: Spet 19, 2024
'''

def q1():
  word = input("Input a word: ")  
  print(word)

def q2():
  name = input("Input your first name: ")
  print("Hello " + name)

def q3():
  name = input("Input your first name: ")
  lastName = input("Input your last name: ")
  word = f"{name} {lastName}"
  print(word)

def q4():
  student1 = input("Input a student: ") 
  student2 = input("Input a student: ")
  students = f"Your students are {student1} and {student2}"
  print(students)

#Do not edit code below this comment

q1()
q2()
q3()
q4()
