# simple project bank manage ment system
first_name = {"First_name": "Maruf"}
name = first_name["First_name"]
last_name = {"Last_name": "Khan"}
lname = last_name["Last_name"]
age = {"Age": 23}
agez = age["Age"]
print(f"your first_name is : {name}")

print(f"your last_name is : {lname}")

print(f"your age is : {agez}")

Account_number = int(input("Enter your account number: "))
print(Account_number)
Pin_Number = int(input("Enter your pin number: "))
print(Pin_Number)
Available_Balance = int(input("Enter your Balance:"))
print(f"your Balance is: {Available_Balance}")
Account_type= str(input("Enter your Account type: "))
if(Account_type=="Saving"):
    print("Saving Account")
else:
    print("Current Account")
withdrawal = int(input("Enter the Amount to withdrawal: "))
print(f"Withdrawal amount is {withdrawal}")
current_balance = Available_Balance - withdrawal
print(f"your current Balance is {current_balance}")
Deposit_Amount = int(input("Enter the amount you want to deposit: "))
New_balance = Deposit_Amount + current_balance
print(New_balance)

