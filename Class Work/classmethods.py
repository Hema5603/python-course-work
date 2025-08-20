'''class School:
    name="Hema"
    marks=90
    school="Sanskriti Vidyalaya"
    def __init__(self):
        print(f"{self.name} got {self.marks} studied in {self.school}")
    @classmethod
    def Changeinfo(cls,name,marks,school):
        cls.name=name
        cls.marks=marks
        cls.school=school
        return f"{cls.name} got {cls.marks} studied in {cls.school}"
s=School()
print(s.Changeinfo("Vishnu",100,"Chaithanya"))
hema=School()
print(hema.Changeinfo("Sravani",90,"Gowthami"))
class Student:
    school = "ABC School"
    print(school)
    @classmethod
    def change_school(cls, name):
        if not isinstance(name, str):
            raise ValueError("School name must be a string")
        cls.school = name
        return cls.school
hema=Student()
print(hema.change_school("Sanskrit"))
vishnu=Student()
Hema=Student()
print(vishnu.change_school("Gowthami"))
class Name:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    @classmethod
    def change_data(cls,data):
        name,marks=data.split("-")
        return cls(name,int(marks))
Anvi=Name("Hema",90)
print(f"{Anvi.name} {Anvi.marks}")
Sravani=Anvi.change_data("Sravani-100")
print(f"{Sravani.name} {Sravani.marks}'''
class Employee:
    c=0
    def __init__(self):
        self.employee=input()
        self.c+=1
    def create_employee(self):
        return self.employee
    @classmethod
    def count_employee(cls):
        cls.c=self.c
        return cls.c
e=Employee()
e.create_employee()
print(e.count_employee())
f=Employee()
f.create_employee()
print(f.count_employee)
        
        


