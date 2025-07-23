p=input("Enter the product names").split(",")
q=input("Enter the quantity").split(",")
pr=input("Enter the price").split(",")
print("Product","Quantity".rjust(30," "),"price".rjust(35," "))
for n in p:
    print(n)
for i in q:
    print(i.rjust(30," "))
for k in pr:
    print(k.rjust(35," "))



