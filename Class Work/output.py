l=["Hema is good girl she do things for time passs","Latha","Sravani","Reddy"]
c=0
for i in l:
    if len(i)>c:
        c=len(i)
print(c)

for i in l:
    if len(i)==c:
        print(i)
for i in l:
    print(i)

f={"Hema":["hii","how are you","hello"],"Latha":["Fine","What about you","How are yoy doing"]}
l=["hii","how are you","hello","Fine","What about you","How are you doing"]
s=[]
for i in l:
    
    s.append(i.split())
print(s)
print(s.count("you"))   
print(s.count("hii"))
print(s.count("how"))
g=[j for x in s for j in x]
print(g)
print(g.count("you"))   
print(g.count("hii"))
print(g.count("how"))
c=0
for i in g:
    if g.count(i)>c:
        c=g.count(i)
print(c)
for i in g:
    if g.count(i)==c:
        print(i)
        break

