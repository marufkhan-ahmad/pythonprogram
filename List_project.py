# invitation
# create a list of guest
Guest = ["Umar","Harshit","Afrid"]
# print the invitation

print(f"Hello {Guest[0].title()} it's my birthday tommorow and I'm inviting you to come at home.")

print(f"Hello {Guest[1].title()} it's my birthday tommorow and I'm inviting you to come at home.")

print(f"Hello {Guest[2].title()} it's my birthday tommorow and I'm inviting you to come at home.")

# change the guest name list
del Guest[0]
print(Guest)
Guest.insert(0,"Faiyaz")
print(Guest)
print(f"Hello {Guest[0].title()} it's my birthday tommorow and I'm inviting you to come at home. ")
Guest.remove("Harshit")
print(Guest)
Guest.insert(1,"Umar")
print(f"Hello {Guest[1].title()} it's my birthday tommorow and I'm inviting you to come at home. ")
Guest.append("Harshit")
print(Guest)
print(f"Hello {Guest[3].title()} it's my birthday tommorow and I'm inviting you to come at home. ")