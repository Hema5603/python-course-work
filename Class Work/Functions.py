#
def display(c,d,e):
    print(c,d,e)
    return 1
    
name="Hema"
pasword="Hema@123"
email="Hema@gmail.com"
print(display(name,pasword,email))
def parents(fname="Krishna Reddy",mname="Rama Devi"):
    print(fname,mname)
    
parents()

def children(*i):
    i=str(i)
    print(i[2])

children("Hema","Sravani","Vishnu")
#for swapcase
def alter(s):
    t=""
    for i in range(0,len(s)):
        if s[i].isupper():
            t=t+s[i].lower()
        elif s[i].islower():
            t=t+s[i].upper()
        else:
            t=t+s[i]
    return t
s="Sravani family consits 5 Numbers"
print(alter(s))
#factorial for numbers up to n
def factorial(n):
    for i in range(1,n+1):
        c=1
        for j in range(1,i+1):
            c=c*j
        print(f"{i}!={c}")
n=int(input())
factorial(n)
#even or odd
def even(a):
    if a%2==0:
        return "Even"
    else:
        return "Odd"
a=int(input())
print(even(a))
#prime or not
def prime(a):
    for i in range(2,a):
        if a%i==0:
            return "Not Prime"
            break
    else:
        return "Prime"
print()
a=int(input())
print(prime(a))
#len function
def length(a):
    return len(a)
a=list(map(int,input().split()))
print(len(a))
#swapcase
def swap(a):
    s=""
    for i in range(0,len(a)):
        if a[i].isupper():
            s=s+a[i].lower()
        elif a[i].islower():
            s=s+a[i].upper()
        else:
            s=s+a[i]
    return s
a=input()
print(swap(a))

#sum of numbers
def sum(n):
    c=0
    for i in range(0,n+1):
        c=c+i
    return c
n=int(input())
print(sum(n))
#prime numbers within the specified range
def primt_num(n):
    for i in range(0,n):
        for j in range(0,i):
            if i%j==0:
                break
        else:
            print(f"{i}")
n=int(input())
primt_num(n)


    
            
            
            

