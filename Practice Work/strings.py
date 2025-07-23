f="Hema"
g=""
print(len(f))
print(len(f)-1)
for i in range(3,-1,-1):
    g=g+f[i]
print(g)
g="Hema123$%^&*"
for i in g:
    if g.isalnum():
        print(i)

g=" HEma123$%^& 756*^*&^&^%*( "
c=""
d=""
for i in g:
    if i.isalnum():
        c=c+i
    else:
        d=d+i
print(c)
print(d)
print(g)
print(g.strip("^"))
#Strings
a="Hemalatha"
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[5])
print(a[6])
print(a[7])
print(a[8])
print(a[0:9])
print(a[0:])
print(a[-9:])
print(a[4:])
print("latha" in a)
a.capitalize()
print(a)


g="Hema is a Good Girl.Srvani is a Bad girl.Sree and Navya are freinds of Hema.Maha and Krishna are Sravani freinds"
c=g.capitalize()
print(g) #Hema is a Good Girl.Srvani is a Bad girl.Sree and Navya are freinds of Hema.Maha and Krishna are Sravani freinds'''
print(c) #Hema is a good girl.srvani is a bad girl.sree and navya are freinds of hema.maha and krishna are sravani freinds'''
g.upper()
print(g) #Hema is a Good Girl.Srvani is a Bad girl.Sree and Navya are freinds of Hema.Maha and Krishna are Sravani freinds'''
g.lower()
print(g)  #Hema is a Good Girl.Srvani is a Bad girl.Sree and Navya are freinds of Hema.Maha and Krishna are Sravani freinds'''
g.title()
print(g) #Hema is a Good Girl.Srvani is a Bad girl.Sree and Navya are freinds of Hema.Maha and Krishna are Sravani freinds'''
g.swapcase()
print(g)  #Hema is a Good Girl.Srvani is a Bad girl.Sree and Navya are freinds of Hema. Maha and Krishna are Sravani freinds'''
g.casefold()
print(g) #Hema is a Good Girl.Srvani is a Bad girl.Sree and Navya are freinds of Hema. Maha and Krishna are Sravani freinds'''
# Here these string methods are not going to change the original it will create a copy by converting the original string we have to create another variable to observe the chage
