import ATMLogic
print("Welcome to ATM")
acc=input("Enter the accno")
pin=int(input("Enter the pin"))

ATMLogic.login(acc,pin)
