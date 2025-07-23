a,b=5,4
c=d=e=5
print(a,b,c,d,e,end=" ")
a=5.4
print(int(a))
a="She is beautiful"
d={}
for i in range(0,len(a)):
    d[a[i]]=a.count(a[i])
print(d)
d={}
n=int(input())
for i in range(0,n):
    sname,marks=input().split()
    marks=int(marks)
    d[sname]=marks
    c=marks
    if marks>c:
        c=marks
print(d)
print(d.keys())
