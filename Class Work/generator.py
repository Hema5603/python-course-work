def family_count(n):
    for i in range(0,n):
        yield i
for i in family_count(5):
    print(i)
def even_count(n):
    for i in range(2,n):
        if i%2==0:
            yield i
n=int(input())
for i in even_count(n):
    print(i)
def ch(str):
    for i in str:
        yield i
str=input()
for i in str:
    print(i)
def count_down(n):
    for i in range(n,0,-1):
        yield i
n=int(input())
gen=count_down(n)
print(list(gen))
print(list(gen))
print(list(gen))
print(list(gen))
def lst_ele(lst):
    for i in lst:
        yield i
lst=list(map(int,input().split()))
print(lst)
for i in lst_ele(lst):
    print(i)
#printing odd numbers
def odd_gen(n):
    for i in range(1,n):
        if i%2!=0:
            yield i
n=int(input())
for i in odd_gen(n):
    print(i)
#printing two numbers
def prin(a,b):
    yield a,b
a=int(input())
b=int(input())
for i in prin(a,b):
    print(i)
#fibnocci series
def fibnocci(n):
    a=0
    b=1
    yield a
    yield b
    for i in range(2,n):
        a,b=b,a+b
        yield b
n=int(input())
for i in fibnocci(n):
    print(i)
#prime numbers
def prime(n):
    for i in range(2,n):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            yield i
n=int(input())
for i in prime(n):
    print(i)
#reverse list generator
def rev_list(l):
    for i in range(len(l)-1,-1,-1):
        yield l[i]
l=list(map(int,input().split()))
for i in rev_list(l):
    print(i)
    
#factorial Generator
def factorial(n):
    for i in range(1,n):
        c=1
        for j in range(i,0,-1):
            c=c*j
        yield c
n=int(input())
for i in factorial(n):
    print(i)
            
#flatten list
def flatten_list(l):
    g=[]
    for i in l:
        for j in i:
            g.append(j)
    yield g
l=[[1,2,3],[4,5,6],[7,8,9]]
for i in flatten_list(l):
    print(i)
numbers = [1, 2, 3, 4]
result = map(lambda x: x * x, numbers)
print(list(result))
    
