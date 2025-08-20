'''#1
class student:
    name="Hema"
    marks=40
    def display(self):
        return f"Student Name:{self.name},Marks:{self.marks}"
s=student()
print(s.display())
#2
class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
a=rectangle(20,40)
print(a.area())
#3
class Car:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
    def start(self):
        return "Car started"
f=Car("Tata","Xyz",2022)
print(f.start())
#4
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*((self.radius)**2)
c=Circle(4)
print(c.area())
#5
class Counter:
    def __init__(self):
        self.counter=0
    def increment(self):
        self.counter+=1
        return self.counter
d=Counter()
print(d.increment())
print(d.increment())
print(d.increment())
print(d.increment())
#6
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greet(self):
        return f"Hello, {self.name}! You are {self.age} years old."
p=Person("Hema",22)
print(p.greet())
#7
class Book:
    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages
    def discription(self):
        return f"Author:{self.author},title:{self.title},pages:{self.pages}"
b=Book("life","Hema","100")
print(b.discription())
#8
class Temperature_Converter:
    def __init__(self,celsius):
        self.celsius=celsius
    def convert_faurenheit(self):
        return (self.celsius*(9/5)+32)
    def convert_kelvin(self):
        return self.celsius+273
c=Temperature_Converter(56)
print(c.convert_faurenheit())
print(c.convert_kelvin())
#9
class Prime_checker:
    def __init__(self,number):
        self.number=number
    def check_prime(self):
        if self.number<=1:
            print("not prime")
            return
        for i in range(2,self.number):
            if self.number%i==0:
                print("not prime")
                return
        else:
            print("prime")
f=Prime_checker(100)
f.check_prime()
#10
class Shopping_Cart:
    def __init__(self):
        self.name=input().split(",")
        self.price=list(map(float,input().split(",")))
    def add_item(self):
        self.c=0
        for i in self.price:
            self.c=self.c+i
        return self.c
    def display(self):
        return f"items:{self.name} total price:{self.c}"
s=Shopping_Cart()
s.add_item()
print(s.display())
#11
class Even_number_Generator:
    def __init__(self,n):
        self.n=n
    def generator(self):
        c=[]
        for i in range(2,self.n+1):
            if i%2==0:
                c.append(i)
        return c
n=int(input())
e=Even_number_Generator(n)
print(e.generator())
#12
class Student_Mark_Statistics:
    def __init__(self,marks):
        self.marks=marks
    def average(self):
        a=(sum(self.marks)/len(self.marks))
        return a
    def highest(self):
        return max(self.marks)
    def lowest(self):
        return min(self.marks)
marks=list(map(int,input().split(",")))
s=Student_Mark_Statistics(marks)
print(s.average())
print(s.highest())
print(s.lowest())
#13
class Bank_Account:
    def __init__(self,balance):
        self.balance=balance
    def deposit(self,amount):
        self.amount=amount
        self.balance+=self.amount
    def withdraw(self,cash):
        self.cash=cash
        if self.balance>=self.cash:
            self.balance-=self.cash
        else:
            print("Insufficient balance")
    def display(self):
        return self.balance
balance=int(input())
amount=int(input())
cash=int(input())
b=Bank_Account(balance)
print(b.deposit(amount))
print(b.withdraw(cash))
print(b.display())
#14
class validate_password:
    def __init__(self,password):
        self.password=password
    def validate(self):
        
        if len(self.password)>=8:
            d=s=u=a=s=0
            for i in self.password:
                if i.isdigit():
                    d=d+1
                elif i.isupper():
                    u=u+1
                elif i.isalnum():
                    a=a+1
                else:
                    s=s+1
            if d+u+s>3:
                return "Validate"
            else:
                return "Invalid"
        else:
            return "Not Valid"
password=input()
v=validate_password(password)
print(v.validate())
            
#15
class Bank_Customer:
    def __init__(self,name,acc_no):
        self.name=name
        if len(acc_no)==10:
            self.acc_no=acc_no
        else:
            self.acc_no="invalid"
    def welcome_message(self):
        return f"Welcome {self.name}, your account number is {self.acc_no}"
name=input()
acc_no=input()
bc=Bank_Customer(name,acc_no)
print(bc.welcome_message())'''
#16
class Calculator:
    def __init(self):
        
    
        
        

    
        
        
    
    
        
        
        
        
    

