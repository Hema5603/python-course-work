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