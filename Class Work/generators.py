'''def number_generator():
    yield 1
    yield 2
    yield 3
for num in number_generator():
    print(num)
def odd_num(n):
    for i in range(1,n,2):
        yield i
n=int(input())
for num in odd_num(n):
    print(num)'''
def fibnocci(n):
    
    if n==0:
        yield 0
    elif n<=1:
        yield 1
    a=0
    b=1
    
    for i in range(2,n):
        
        yield a
n=int(input())
for num in fibnocci(n):
    print(num)
        
        
    
