g=int(input("Enter the number:"))
c=0
while g>0:
    d=g%10
    c=c+d
    g=g//10
print(f"sum of the digits is {c}")

n=int(input())
for i in range(1,n):
    if i%3==0:
        print(i)

#checking prime or not
f=int(input("Enter the number:"))
for i in range(1,f):
    if f%i==0:
        print(f"{f} is not a prime number")
        break

n=input()

f=""
for i in range(len(n),0):
    f=f+n[i]
    print(f)
    
d={1:"Selfie.jpg",2:"Birthday.jpg",3:"beach.jpg",4:"Sunrise.jpg",5:"Sunset.jpg"}
n=set(map(int,input("Enter the picture number you want to display").split()))
print("sharing photos you want to display")
for i in n:
    for j in d:
        if i==j:
            print(d[i])
            


              