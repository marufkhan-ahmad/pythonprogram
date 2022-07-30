# create a dictionary

Bank_details = {"Name": "Maruf khan", "Account_Number": 444123645,
                "IFSC_code": "BOI000444", "Bank_Name": "Bank of India",
                "Branch": "Bettiah west champaran Bihar",
                "Account_type": "Savings", "Account_Balance": "$ 1000"}

#  create a variable and store the data into it

information = Bank_details["Name"]
information_1 = Bank_details["Account_Number"]
information_2 = Bank_details["IFSC_code"]
information_3 = Bank_details["Bank_Name"]
information_4 = Bank_details["Branch"]
information_5 = Bank_details["Account_type"]
information_6 = Bank_details["Account_Balance"]

# display the information

print(f"Your name is : {information} \n")
print(f"Your Account Number is : {information_1} \n")
print(f"Your IFSC code is : {information_2} \n")
print(f"Your Bank name is : {information_3} \n")
print(f"Your Branch is : {information_4} \n")
print(f"Your Account type is : {information_5} \n")
print(f"Your Available Account Balance is : {information_6} \n")
