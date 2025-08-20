'''def sum(n):
    c=n%10
    if n==0:
        return 0 
    else:
        return c+sum(n//10)
n=int(input())
print(sum(n))
def power(n,p):
    if p==0:
        return 1
    else:
        return n*power(n,p-1)
n=int(input())
p=int(input())
print(power(n,p))
def power(n, p):
    if p == 0:
        return 1
    elif p < 0:
        return 1 / power(n, -p)
    else:
        return n * power(n, p - 1)
n=int(input())
p=int(input())
print(power(n,p))
def reverse(n):
    if n<=0:
        return [] 
    else:
        return [n]+reverse(n-1)
      
n=int(input())
print(reverse(n))
def fibnocci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fibnocci(n-1)+fibnocci(n-2)
n=int(input())
print(fibnocci(n)
def factorial(n):
    if n==0 or n==1:
        return 1
    
    
    return n*factorial(n-1)
n=int(input())
print(factorial(n))
def listsum(l,n):
    if n<1:
        return 0
    return l[n-1]+listsum(l,n-1)
l=list(map(int,input().split()))
n=len(l)
print(listsum(l,n))
def reverse(string1,n):
    if n==0:
        return string1[0]
    return string1[n]+reverse(string1,n-1)
string1=input()
n=len(string1)-1
print(reverse(string1,n))
def sum_array(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + sum_array(arr[1:])
arr=list(map(int,input().split()))
print(sum_array(arr))
import random
def palindrome(word):
    if len(word)<=1:
        return True
    if word[0]!=word[-1]:
        return False
    else:
        return palindrome(word[1:-1])
def listele(list1,size):
    t=[]
    for i in range(0,size):
        r=random.randint(0,len(list1)-1)
        t.append(list1[r])
    return t
list1=input().split()
size=int(input())
print(listele(list1,size))
def naturalsum(n):
    if n==1:
        return 1
    return n+naturalsum(n-1)
n=int(input())
print(naturalsum(n))
def binarysearch(l,target,i=0):
    if l[i]==target:
        return i
    return binarysearch(l,target,i+1)
l=list(map(int,input().split()))
target=int(input())
print(binarysearch(l,target))'''

    

    
    
    

        
        

