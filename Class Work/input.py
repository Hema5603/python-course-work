l=["Hema is a beautiful girl","Sravani is sister is of hema","Vishnu is a good and bad boy","Rama devi is a mother","Krishna is a father"]
c=0
for i in l:
    c=c+1
    for j in i:
        if j.isspace():
            c=c+1
print(c)
d={"Hema":["Hema is a", "good girl"],"Sravani":["Sravani is a"," good and bad girl"]}
for l in d:
    for m in d[l]:
        print(m)
n=[]
m=[]
for i in range(0,4):
    name,message=input().split()
    n.append(name)
    m.append(message)
print(n)
print(m)
        
        
