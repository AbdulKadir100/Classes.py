class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def display(self):
        print(self.name,self.marks)
    def __add__(self, S):
        Temp = Student(S.name,[])
        for i in range(len(self.marks)):
            Temp.marks.append(self.marks[i]+S.marks[i])
        return Temp

s1 = Student("Abdul", [87,90,99])
s2 = Student("Kadir", [87,65,75])
s1.display()
s2.display()
s =  s1 + s2
s.display()