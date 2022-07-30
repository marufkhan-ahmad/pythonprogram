from re import U


Username = ["Maruf", "Umar", "Sohaib", "Sahid", "Afrid", "Admin"]
for Username in Username:
    print(f"Hello {Username}")
    if(Username=="Admin"):
        print(f"Hello Admin, would you like to see a status report?")
    else:
        print(f"Thank you for login again {Username}")