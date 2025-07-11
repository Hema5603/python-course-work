# n natural numbers
n=int(input("enter the number:"))
for i in range(1,n):
    print(i) 

#n even numbers
g= int(input("Enter the number"))
for i in range(2,g,2):
    print(i)

#prime number
count=0
n=int(input("Enter the number"))
for i in range(1,n+1):
  if n%i==0:
     count+=1
if count==2:
   print("prime number")
else:
   print("not prime")


fact=0
n=int(input("Enter the number"))
for i in range(2,(n//2)+1):
   if n%i==0:
     fact+=1
if fact==0:
   print(f"{n} is prime number\nFcators count={fact}")
else:
   print(f"{n} is not prime number\nFcators count={fact}")
l=['veg','non veg','starters','cold drinks']
for i in range(len(l)):
   print()
#Positive or Negative
f=int(input())
if f>0:
    print("positive number")

#Even or Odd
g=int(input())
if g%2==0:
    print("Even Number")
else:
    print("Odd Number")

#divisibility
h=int(input())
if h%5==0:
    print(f"{h} is divisible by 5")
else:
    print(f"{h} is not divisible by 5")

#divisibility by 3 and 5
a=int(input("Enter the number:"))
if a%3==0 and a%7==0:
    print(f"{a} is divisible by both 3 and 5")
elif a%3==0:
    print("f{a} is divisible by 3")
elif a%5==0:
    print(f"{a} is divisible by 5")
else:
    print(f"{a} is not divisible by any of them")

#Leap Year
y=int(input())
if y%4==0 or y%400==0:
    print(f"{y} is a leap year")
else:
    print(f"{y} is not a leap year")

#pass or fail
m=int(input("Enter the marks of a student:"))
if m>90:
    print("A grade")
elif m>80 and m<=90:
    print("B grade")
elif m>70 and m<=80:
    print("C grade")
elif m>60 and m<=70:
    print("D grade")
elif m>50 and m<=60:
    print("E grade")
elif m>40 and m<=50:
    print("F garde")
elif m>=35 and m<=40:
    print("Just Pass")
else:
    print("Fail")

#3 digit number
h=int(input("Enter the number you want to check"))
if len(h)==3:
    print(f"{h} is a 3 digit number")
else:
    print(f"{h} is not a 3 digit number")

#vowel
c=input("Enter the character you want to check")
if c=='a' or c=='e' or c=='i' or c=='o' or c=='u' or c=='A' or c=='E' or c=='I' or c=='O' or c=='U':
    print(f"{c} is vowel")
else:
    print(f"{c} is not a vowel")

#Greatest Number
b=int(input("Enter the First Number:"))
c=int(input("Enter the Second Number:"))
if b>c:
    print(f"{b} is greater number")
else:
    print(f"{c} is greater number")

#digit or not
d=int(input("Enter the digit to check:"))
if d.isdigit():
    print(f"{d} is a digit")
else:
    print(f"{d} is not a digit")

#palindrome
f=input("Enter the string to check:")
if f==f[::-1]:
    print(f"{f} is a palindrome")
else:
    print(f"{f} is not a palindrome")

#comparing string lengths
e=input("Enter the first string")
f=input("Enter the second string")
if len(e)>len(f):
    print(f" length of {e} is greater than length {f}")
elif len(f)>len(e):
    print(f"length of {f} is greater than length of{e}")
else:
    print("Both are equal")

#Check if a number is with in range and divisible by 5
d=int(input("Enter the number"))
if d>=50 and d<=100 and d%5==0:
    print("it is in range and divisible by 5")
else:
    print("not in range or not divisible by 5")

#check temperature
temp= int(input("Enter the temperature:"))
if temp<15:
    print("Cold")
elif temp>=15 and temp<=30:
    print("Moderate")
else:
    print("Hot")

#Checking perfect square or not
num=int(input("Enter the Number:"))
if num%num==0:
    print(f"{num} is a perfect square")
else:
    print(f"{num} is not a perfect square")

#checking angle
angle=int(input("Enter the angle you want to check"))
if angle>0 and angle<90:
    print("Acute angle")
elif angle==90:
    print("Right angle")
elif angle>90 and angle<180:
    print("Obtuse angle")
else:
    print("Invalid angle")
   