
    
n=int(input())
for i in range(2,n+1):
    if n%i==0:
        print(f"{n} is not a prime number")
        break
name,email='hema','hema@gmail.com'
attempt_count=0
while attempt_count<3:
    n=input("enter the name")
    e=input("enter the email")
    if(name==n and email==e):
        print("Login Successful")
    else:
        print("Invalid Login")
    attempt_count=attempt_count+1
h={}
for i in range(0,6):
    h[i]=i**2
print(h)
n=int(input())
for i in range(0,11):
    c=n*i
    print(f"{n} * {i}={c}")
c=0
for i in range(0,11):
    c=c+i
print(f"sum of numbers is {c}")
    
