class Student_ATU:      
    # Constructor special method      
    def __init__(self, name, student_number:int):      
        print("This is constructor")      
        self.name = name  
        self.student_number = student_number
    # method  
    def show(self):      
        print("Hello",self.name, ",Your student number is:", self.student_number)      
student1 = Student_ATU ("Konrad Jeziorski", "L00169649")
student2 = Student_ATU ("Daniel Snow", "L00112233")

#calling the method  
student1.show()   
student2.show()

# some ideas from:
# https://www.c-sharpcorner.com/article/object-oriented-programming-in-python-with-examples-part-1/