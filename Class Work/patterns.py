'''n=int(input())
for i in range(0,n):
    for j in range(0,n):
        print("*",end=" ")
    print()
print()
for i in range(0,n):
    for j in range(0,n):
     if i+j<=n-1:
         print("*",end=" ")
     else:
         print(" ",end=" ")
    print()
print()
for i in range(0,n):
    for j in range(0,n):
        if i+j>=n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print()
for i in range(0,n):
    for j in range(0,n):
        if i>=j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print()
for i in range(0,n):
    for j in range(0,n):
        if i<=j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print()'''
n=int(input())
for i in range(0,n):
    for j in range(0,n):
        if i+j<=n:
            print(" ",end=" ")
    for k in range(0,2*i):
        print("*",end=" ")
    print()
     
        
         
