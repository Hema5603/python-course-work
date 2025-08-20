#check if a input is valid identifier
string=input()
def check_identifier(g):
    if g.isidentifier():
        print("Valid")
        g=g.lower()
        print(g)
    else:
        print("Invalid")
check_identifier(string)
#trim and count words in paragraph
