'''def addition(a,b):
    return a+b
print(addition(345,345))
def square(a):
    return a*a
print(square(12))
def area(r):
    return 3.14*(r**2)
print(area(4))
def area1(r,pi=3.14):
    return pi*(r**2)
r=int(input())
print(area1(r))
def greet(name):
    return f"Hello, {name}"
string=input()
print(greet(string))
def convert_cel(c):
    return (c*1.8)+32
c=float(input())
print(convert_cel(c))
def convert_far(f):
    return (f-32)*(5/9)
f=float(input())
print(convert_far(f))
def product(a,b,c):
    return a*b*c
a,b,c=list(map(int,input().split()))
print(product(a,b,c))
#simple interest
def interest(p,t,r):
    SI=(p*t*r)/100
    print(SI)
principal,time,rate=list(map(int,input().split()))
interest(principal,time,rate)
#string Length
def str_len(string):
    print(len(string))
p=input()
str_len(p)
#Adding an element to a list
def appending(l,ele):
    l.append(ele)
    return l
l=list(map(int,input().split()))
ele=int(input())
print(appending(l,ele))
#double the list elements
def double(l):
    g=[]
    for i in l:
        g.append(i*2)
    return g
l=list(map(int,input().split()))
print(double(l))
#sorting a list
def sort(l):
    return sorted(l)
f=list(map(int,input().split()))
print(sort(f))
def clearing(d):
    d.clear()
    return d
f=tuple(map(int,input().split()))
print(clearing(f))
print(f)
#updating dictionary value
def update(d):
    k=input("enter the key to update")
    v=int(input("Enter the new value"))
    d[k]=v
    return d
d=eval(input("Enter the dictionary you want to update"))
print(update(d))
#updating a list
for i in range(0,len(l)):
    if 3 in l:
        l.remove(3)
l=[1,6,3,5,3,7,3,8]
print(l)
#Adding a new key to dictionary
def adding(f,n):
    for i in range(0,n):
        k=input("enter the key you want to update")
        v=input("enter the value you want to add")
        f[k]=v
    return f
f={}
print(adding(f,5))
#incrementing values in dictionary
def incre_value(f):
    for i in f:
        f[i]=f[i]+1
    return f
g=eval(input())
print(incre_value(g))
#factorial of a number
def factorial(n):
    c=1
    for i in range(1,n+1):
        c=c*i
    return c
n=int(input())
print(factorial(n))
#fibnocci of nth term
def fibnocci(n):
    a=0
    b=1
    if n==0:
        return 0
    if n==1:
        return 1
    for i in range(2,n+1):
        a,b=b,a+b
        if n==i:
            return b
n=int(input())
print(fibnocci(n))
#sum of first n natural numbers
def natural(n):
    c=0
    for i in range(1,n+1):
        c=c+i
    return c
n=int(input())
print(natural(n))
#reverse a string
def addition(n):
    if n==0:
        return 0
    return n+addition(n-1)
n=int(input())
print(addition(n))'''
#power of a number
def power(a,b):
    for i in range(0,b):
        return n*n
a=int(input())
b=int(input())
print(power(a,b))


        
    

    

   
    
    

    
    

