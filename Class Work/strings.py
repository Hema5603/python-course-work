string="Hema"
string1="Latha"
new_string=string+" " +string1
print(new_string)
print(new_string)
print(new_string*2)
new_string=new_string+" "+"is"+" "+"a"+" "+"good"+" "+"girl"
print(new_string)
print(new_string.capitalize())
print(new_string.lower())
print(new_string.upper())
print(new_string.casefold())
print(new_string.title())
print(new_string.swapcase())
print("Family".center(60,' '))
print("Hema".ljust(40," ")+"latha".rjust(40," "))
print("sravani".ljust(40," ")+"Reddy".rjust(40," "))
print("Vishnu".ljust(40," ")+"vardhan".rjust(42," "))
print("Krishna".ljust(40," ")+"Reddy".rjust(40," "))
print("Rama".ljust(40," ")+"Devi".rjust(39," "))
string="Hema is a good girl"
print(sorted(string))
def centerbanner(s):
    return s.center(50,"*")
s=input()
print(centerbanner(s))



