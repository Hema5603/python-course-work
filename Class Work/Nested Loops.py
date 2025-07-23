for i in range(0,5):
    for j in range(0,5):
        print(i,end=" ")
    print()
print()
for i in range(0,5):
    for j in range(0,5):
        print(j,end=" ")
    print()
print()
for i in range(0,5):
    for j in range(0,i):
        print('*',end=" ")
    print()
print()
for i in range(5,0,-1):
    for j in range(0,i):
        print("*",end=" ")
    print()
print()
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print('*',end=" ")
    print()
print()
for i in range(5,0,-1):
    for j in range(5,i):
        print("*",end=" ")
    print()
print()
for i in range(0,5):
    for j in range(3,5):
        print("*",end=" ")
    print()
for i in range(0,5):
    for j in range(0,5):
        if i<=j:
            print("*",end=" ")
    print()
n=int(input())
for i in range(0,n):
    for j in range(0,n):
        if i+j==n//2 or i-j==-(n//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
