'''l=[2,3,4,5,6,7]
t=list(filter(lambda x:x%2,l))
print(t)
def even(n):return n%2==0
g=list(filter(even,l))
print(g)
def odd(n):return n%2!=0
h=list(filter(odd,l))
print(h)
values = ["apple", "", 0, None, "banana"]
cleaned = list(filter(None, values))  # ["apple", "banana"]
print(cleaned)
def remove_space(r):
    
g=["Hema","","Latha","Sravani","Krishna",""]
i=list(filter(None,g))
print(g)
print(i)
l=list(map(int,input().split()))
temperature=list(filter(lambda x:x>45,l))
print(temperature)
def hightemp(h,t):
    if h>t:
        return h
g=list(map(int,input().split()))
t=int(input())
temperature=list(filter(lambda x:hightemp(x,t) ,g))
print(temperature)
def lowtemp(j,t):
    if j<=t:
        return j
list1=list(map(int,input().split()))
t=int(input())
lowtemperature=list(filter(lambda x:lowtemp(x,t),list1))
print(lowtemperature)
def uppercase(l):
    if l.isupper():
        return l
letter=input().split()
upperletter=list(filter(uppercase,letter))
print(upperletter)
def vowel(l):
    if l.startswith("a") or l.startswith("e") or l.startswith("i") or l.startswith("o") or l.startswith("u") or l.startswith("A") or l.startswith("E") or l.startswith("O") or l.startswith("U"):
        return l
s=input().split()
vowelwords=list(filter(vowel,s))
print(vowelwords)
def consonant(s):
    l=[]
    t="aeiou"
    if s not in t:
        l.append(s)
    return l
s=input()
consonantletter=list(filter(consonant,s.lower()))
print(consonantletter)
s="aeiou"
letter=input()
consonants=list(filter(lambda x: x if x.lower() not in s else " ",letter))
print(consonants)
d=eval(input())
f={}
for i in d:
    if d[i]>45:
        f[i]=d[i]
print(f)'''
def filterdictionary(d):
    for x,y in d:
        print(y)
        
r={"Hema":43,"Sravani":45,"Vishnu":40,"Krishna":70,"Ramadevi":70}
h=list(filter(filterdictionary,r.items()))
print(h)



             
            
