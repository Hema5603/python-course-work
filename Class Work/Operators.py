#Arithmetic operators
a=30
b=3
print("addition:",a+b) #addition: 33                                  
print("subraction:",a-b)#subraction: 27
print("division:",a/b) #division: 10.0
print("multiplication:",a*b) #multiplication: 90
print("flordivision:",a//b) #flordivision: 10
print("power:",a**b) #power: 27000

#comparision operators

a="Hema"
b="sravani"
print("equal or not :",a==b) #equal or not : False
print("not equal or not:",a!=b) #not equal or not: True
print("lessthan:",a<b) #lessthan: True
print("greater than or not:",a>b) #greater than or not: False
print("less than or equal:",a<=b) #less than or equal: True
print("greater than or equal:",a>=b) #greater than or equal: False

#for strings it compares ascii values and give true or False

#Assignment Operators
h=130
h-=20
print("a=a-20:",h)#a=a-20: 110
h*=2
print("a=a*20:",h) #a=a*20: 220
h/=20
print("a=a/20:",h) #a=a/20: 11.0
h//=2
print("a=a//2:",h) #a=a//2: 5.
h%=2
print("a=a%2:",h) #a=a%2: 1.0
h**=2
print("a=a**2:",h) #a=a**2: 1.0
h+=2
print("a=a+2:",h)  

#Logical Operators
c=20
b=30
print(c%2==0 and b%2==0)
print(c%2==0 and b%2==0)
print(not(c%2==0 and b%2==0))

#Membership Operators

f="Hemalatha"
print("la" in f)
print(f[:3]=="Hem")
print("la" not in f)

#Identity Operators
a=2
b=2
print(" for int:",a is b)
print(id(a))            
print(id(b))              
f="Hema"
g="Hema"
print(" for string is:",f is g)
print(id(f))
print(id(g))
e=[2,3,4,5]
f=[2,3,4,5]
print(" for list is:",e is f)
print(id(e))
print(id(f))
p=(1,2,3,4)
q=(1,2,3,4)
print("for tupple is:",p is q)
print(id(p))
print(id(q))
r={1:"Hema",2:"Vishnu",3:"Sravani"}
t={1:"Hema",2:"Vishnu",3:"Sravani"}
print("for dictionary is:",r is t)
print(id(r))
print(id(t))
k={6,7,90,100}
l={6,7,90,100}
print(id(k))
print(id(l))
print("for set is:",k is l)
#bitwise Operators
a=4 #100
b=5 #101
print(a & b)
print(a|b)
print(a^b)
print(~a)
print(~b)