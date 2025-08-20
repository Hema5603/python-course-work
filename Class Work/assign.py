n=int(input())
f={}
me=[]
for i in range(0,n):
    name,message=input().split(":")
    if name not in f:
        f[name]=[]
    f[name].append(message)
    me.append(message)
print(f)
#1.unique users
for i in f:
    print(i)
    
#2.total words in message
c=0
for i in f:
    for j in f[i]:
        c=c+1
        for k in j:
            if k.isspace():
                c=c+1
print("Total words in the message:",c)
#3.average message
average=((c)/len(me))
print(f"Average is: {average}")
#4.longest message in the chat
c=0
d=""
for i in me:
    if len(i)>0:
        c=len(i)
print(c)
e=""
for i in me:
    if len(i)==c:
        print(i)
#5.most active user in the chat
l=0
for i in f:
    if len(f[i])>l:
        l=len(f[i])
print(l)
for i in f:
    if len(f[i])==l:
        print(f"most active user in chat is {i}")
#6.message count of a user
c=input()
for i in f:
    if i==c:
        print(len(f[i]))
#7.first and last message in the chat
e=input()
for i in f:
    if i==e:
        print(f[i][0])
        print(f[i][-1])
#8.user present or not
g=input()
if g in f:
    print("User Is Present")
else:
    print("User is not present")
#9.for unique messages
me=set(me)
s=len(me)
print(f"unique message count {s}")
#10.for sorting messages in alphabetical order
print(f"after sorting {sorted(me)}")
#11.checking for deleted messages
c=0
for i in me:
    if i=="This message was deleted":
        c=c+1
        print(f"Delete message found {c}")
#12.checking if they are questions
for i in me:
    if '?' in i:
        print(i)
#13.messages containing the specified user
j=input()
c=0
for i in me:
    if j in i:
        c=c+1
        print(f"messages mentioning {j}: {c}")
#14.total messages in chat
print(f"total messages in chat is: {len(me)}")
#15.Reply ratio from user1 to user2
u1=input()
u2=input()
g=0
for i in f:
     if i==u1:
         for j in f[i]:
              if u2 in j:
                  g=g+1
              
print(f"reply ratio from {u1} to {u2} is {g}")                     
#16.Commonly related words
h=[]
for i in me:
    h.append(i.split())
print(h)
j=[ele for x in h for ele in x]
print(j)
c=0
for i in j:
    if j.count(i)>c:
              c=j.count(i)
print(c)
d=set()
for i in j:
     if j.count(i)==c:
              d.add(i)
              
print(f"most commonly repeated words are {d}")             

#17.most frequently used word by a specific user
x=input()
z=[]
for i in f:
    if i==x:
        for j in f[i]:
            z.append(j.split())
            
print(z)
d=[ele for i in z for ele in i]
v=0
for i in d:
    if d.count(i)>v:
        v=d.count(i)
s=set()
for i in d:
    if d.count(i)==v:
        s.add(i)
print(f"Most frequent word used by {x} is {s}")
#18.Longest average message length
Avg=0
for i in f:
    h=[]
    for j in f[i]:
        n=len(f[i])
        h.append(j.split())
        g=[x for i in h for x in i]
        d=len(g)
        a=d/n
        if a>Avg:
            Avg=a
        print(f"highest average length is {Avg}")
        
        
        
    
    
    
