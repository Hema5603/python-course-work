l=[x for x in range(5) if x%2==0]
print(l)
l=[x for x in range(1,5)]
print(l)
h=[x for x in l]
print(h)
g=[x*x for x in range(1,10)]
print(g)
h=[x for x in range(1,101) if x%2==0]
print(h)
g=["Hema","Umbrella","Sravani","Vishnu","Anshu"]
j=[x for x in g if x.upper().startswith(("A","E","I","O","U"))]
print(j)
d=[[1,2],[3,4]]
f=[j for x in d for j in x]
print(f)
p=[1,2,3]
q=[3,4,5]
g=[(x,y) for x in p for y in q if x!=y]
print(g)
x=input()
c=""
for i in range(len(x)-1,-1,-1):
    c=c+x[i]
print(c)
d=int(input())
c=0
while d>0:
    c=c*10+d%10
    d=d//10
print(c)
o=input()
c=0
for i in range(0,len(o)):
    o=int(o)
    c=c*10+o%10
    o=o//10
print(c)
c=input()
    
