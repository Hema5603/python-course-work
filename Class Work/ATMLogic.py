data={
     '1234':{'balance':67889,'pin':5670,'history':[]},
     '5678':{'balance':67849,'pin':5230,'history':[]},
     '8907':{'balance':67829,'pin':5870,'history':[]},
     '4560':{'balance':67819,'pin':4570,'history':[]},
     '5679':{'balance':67809,'pin':3270,'history':[]},
     '4896':{'balance':67859,'pin':8970,'history':[]}  
    }
acc_num=None
login_status=False
def welcome()
 print("Welcome to the ATM'.center(40,'-'))
def menu()
 print("1.Check Balance")
 print("2.Deposit")
 print("3.withdraw")
 print("4.View Transaction")
 print("0.Exit")
       
def login(acc,pin):
    if acc in data:
        if data[acc]['pin']==pin:
         acc_num=acc
         print("Login Successful")
        else:
         print("Login Invalid pin")
    else:
        print("Invalid Account Number")
        
def checkBalance(balance):
    if 
        
