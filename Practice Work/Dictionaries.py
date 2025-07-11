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


#how to create a dictionary
d={}
print(d)
f=dict()
print(f)
d[0]="Hema"
d[1]="Sravani"
d[2]="Vishnu"
print(d)
for i in range(0,5):
    f[i]=i*i
print(f)
h={}
h["Hema"]="Second Child"
h["Sravani"]="First Child"
print(h)
h[True]="Correct Value"
print(h)
print(h[True])
print(h.get("Vishnu","NA"))
h["Vishnu"]="Third Child"
print(h)
h["Krishna"]="Father"
h["Rama Devi"]="Mother"
print(h)
h.pop(True)
print(h)
del h["Hema"]
print(h)
h.clear()
print(h)
d.popitem()
print(d)
g=d.keys()
print(g)
print(f.keys())
s=d.values()
print(s)
print(f.values())
print(d)
print(d.items())
print(d)
d.update(f)
print(d)
h=f
print(h)
print(len(h))
c=h.setdefault(6,36)
print(c)
print(len(h))
print(h)
print(max(h))
print(min(h))
print(sorted(h))
j={"h":"i","a":"n","k":"v"}
print(sorted(j))
friends={"valli":{"class":8,"school":"Chaithanya","age":21},"Sree":{"class":"Inter","school":"Narayana","age":21}}
print(friends)
print(friends.keys())
print(friends.values())
print(friends["valli"])
print(friends["Sree"])
print(friends["valli"]["class"])     

#dictionaries using conditional statements
stu_marks={"hema":75,"sravani":95,"Vishnu":100,"krishna":100,"Rama":100}
for i in stu_marks:
    if stu_marks[i]>75:
        print(i)
        