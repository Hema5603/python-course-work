'''class cow():
    def sound(self):
        return "amba"
class Goat():
    def sound(self):
        return "meh"
def animal_sound(animal):
    print(animal.sound())
animal_sound(Goat())
animal_sound(cow())
class book():
    def __init__(self,string):
        self.string=string
    
    def pages(self):
        return f"book has {len(self.string)} pages"
class Magazine():
    def __init__(self,string):
        self.string=string
    def pages(self):
        return f"Magazine has {len(self.string)} pages"
def get_pages(item):
    print(item.pages())
b1=book("solo leveling is for inspiration and learn self growth")
m1=Magazine("This magazine highlights th author of sololeveling")
get_pages(b1)
get_pages(m1)

class book():
    string1="solo leveling is for inspiration and learn self growth"
    def pages(self):
        self.string1=self.string1
        return f"book has {len(self.string1)} pages"
class Magazine():
    string2="This magazine highlights th author of sololeveling"
    def pages(self):
        self.string2=self.string2
        return f"book has {len(self.string2)} pages"
def get_pages(item):
    print(item.pages())
get_pages(book())
get_pages(Magazine())
class Vehicle():
    def move(self):
        return "Vehicle is moving"
class Car(Vehicle):
    def move(self):
        return "Car is moving"
class Bike(Vehicle):
    def move(self):
        return "Bike is moving"
list1=[Vehicle(),Car(),Bike()]
for i in list1:
    print(i.move())
class Employee():
    def role(self):
        return "role is employee"
class Developer():
    def role(self):
        return "I am a Developer"
class Designer():
    def role(self):
        return "I am a Designer"
list2=[Employee(),Developer(),Designer()]
for i in list2:
    print(i.role())
class Circle():
    def __init__(self,r):
        self.r=r
    def area(self):
        return f"area of Circle is {3.14*(self.r)**2}"
class Square():
    def __init__(self,a):
        self.a=a
    def area(self):
        return f"area of Square is {self.a*self.a}"
class Triangle():
    def __init__(self,base=None,height=None,side1=None,side2=None,side3=None):
        self.base=base
        self.height=height
        self.side1=side1
        self.side2=side2
        self.side3=side3
    def area(self):
        if self.side1 and self.side2 and self.side3:
            return f"area of Triangle is {self.side1*self.side2*self.side3}"

        elif self.base and self.height:
            return f"area of Triangle is {0.5*self.base*self.height}"
        else:
            return "Insufficient data"
list1=[Circle(5),Square(6),Triangle(10,20),Triangle(10,30,40)]
for i in list1:
    print(i.area())
class addition:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        return addition(self.x+other.x,self.y+other.y)
    def __str__(self):
        return f"({self.x},{self.y})"
p1=addition(2,3)
p2=addition(4,5)
p3=p1+p2
print(p3)'''
class comparision():
    def __init__(self,name,marks):
        self.marks=marks
    def __add__(self,other):
        return self.marks+other.marks
    def __lt__(self,other):
        return self.marks<other.marks
    def __str__(self):
        return f"{self.name} and {self.marks}"
c1=comparision("Hema",90)
c2=comparision("sravani",100)
print(c1+c2)


    

    

    


    
