def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)
n=int(input())
print(factorial(n))

m=input()
s=0
for i in m:
    s=s+int(i)
print(s)
n=int(input())
c=0
while n>0:
    d=n%10
    c=c+d
    n=n//10
print(c)
def s(n):
    if n==0:
        return 0
    return n%10+s(n//10)
n=int(input())
print(s(n))
0,1,1,2,3,5,8,13
n=int(input())
a=0
b=1
print(a,b,end=" ")
for i in range(0,n):
    c=a+b
    a=b
    b=c
    print(c,end=" ")
    


