'''class details:
    def __init__(self,name,email,password):
        self.name=name
        self._email=email #protected
        self.__password=password #private
    def getpassword(self):
        return self.__password
    def setpassword(self,newpassword):
        self.__password=newpassword
        return newpassword
vishnu=details("vishnu","vishnu@gmail.com","vishnu@123")
print(vishnu.name)
vishnu.name="Hema"
print(vishnu.name)
print(vishnu._email)
vishnu._email="hema@gmail.com"
print(vishnu._email)
print(vishnu.getpassword())
print(vishnu.setpassword("hema@123"))
class Bank:
    def __init__(self):
        self._balance=0
    @property
    def accessbalance(self):
        return self._balance
    @accessbalance.setter
    def credit(self,amount):
        self._balance+=amount
b=Bank()
print(b.accessbalance)
b.credit=4000
print(b.accessbalance)


class employee:
    name=input()
    age=int(input())
    branch=input()
    def display(self,n,a,b):
        self.n=n
        self.a=a
        self.b=b
        return f"name:{n} age:{a} branch:{b}"
e=employee()
print(
print(employee.name)
print(empoyee.age)'''
class family:
    number=5
    income=50000
    def __init__(self,father,mother,sister,brother):
        self.father=father
        self.mother=mother
        self.brother=brother
        self.sister=sister
    def display(self,name,salary):
        self.name=name
        self.salary=salary
        return name,salary,self.income,self.father,self.brother
f=family("Krishna","Sravani","Ramadevi","Vishnu")

print(f.display("Hema",900000))
print(f.father)
print(f.sister)
class family1:
    father="Krishna Reddy"
    mother="Rama Devi"
    Sister="Sravani"
    Brother="Vishnu"
    def display(self):
        return f"father:{self.father},mother:{self.mother},Sister:{self.Sister},brother:{self.Brother}"
g=family1()
print(g.display())










