s="Hema is a good girl"
c=1
for i in s:
    if i.isspace():
        c=c+1

print(c)
l=["Hema is a good girl","sravani is a bad girl"]
for i in l:
    print(i)










n=int(input())
f={}
for i in range(0,n):
    name,message=input().split(":")
    if name not in f:
        f[name]=[]
    f[name].append(message)
print(f) #{'Hema': ['Hii', 'Hello'], 'Sravani': ['Hii', 'Fine']}
print(len(f)) #2
print(len(f['Hema']))#2
c=1
for i in f:
    for j in f[i]: #Hii Hello Hii Fine
        print(j)
        if j.isspace():
            c=c+1
print(c)
    
    
        

    
    
    
