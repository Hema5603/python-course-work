marks = list(map(int, input("Enter marks: ").split()))
print(marks)
print(marks[::-1])
n=10
while n>0:
    if n==6:
        print("dead")
        break
    n=n-1
    print("Shoot")
else:
    print("End of the Game")
# n natural numbers
'''n=int(input("enter the number:"))
for i in range(1,n):
    print(i) '''

#n even numbers
g= int(input("Enter the number"))
for i in range(2,g,2):
    print(i)

#sum of natural numbers
h=int(input("Enter the number"))
c=0
for i in range(1,h):
    c=c+i
print(f"sum of numbers is {c}")

#Odd Numbers
for i in range(1,h,2):
    print(i)

#factorial    
d=1
for i in range(1,h):
    d=d*i
print(f"factorial is {d}")

#multiplication of a table
n=int(input("Enter the number:"))
for i in range(1,n):
    print(f"{n}*{i}=={n*i}")

#checking prime or not
f=int(input("Enter the number:"))
for i in range(1,f):
    if f%i==0:
        print(f"{f} is not a prime number")
        break

#sum of digits
g=int(input("Enter the number:"))
c=0
while g>0:
    d=g%10
    c=c+d
    g=g//10
print(f"sum of the digits is {c}")

#Count numbers divisible by 3
n=int(input())
for i in range(1,n):
    if i%3==0:
        print(i)

n=input("enter the string:")
str=""
for i in range(len(n),0):
    str=str+n[i]
if str==n:
    print("palindrome")
else:
    print("Not palindrome")
