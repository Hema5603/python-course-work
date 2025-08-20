d={1:"Selfie.jpg",2:"Birthday.jpg",3:"beach.jpg",4:"Sunrise.jpg",5:"Sunset.jpg"}
n=set(map(int,input("Enter the picture number you want to display").split()))
print("sharing photos you want to display")
for i in n:
    for j in d:
        if i==j:
            print(d[i])
d={}
n=int(input())
for i in range(0,n):
    fname,lname=input().split()
    d[fname]=lname
print(d)
d={"Hema":{"Physics":30,"Chemistry":50,"Maths":40},"Sravani":{"Physics":40,"Chemistry":60,"Maths":70}}
print(d)
d["Hema"]["Biology"]=50
print(d)
f={}
k=int(input())

for i in range(0,k):
    sname=input()
    f[sname]={}
    for j in range(0,2):
        f[sname]["physics"]=50
        f[sname]["chemistry"]=60
        f[sname]["Maths"]=70

print(f)