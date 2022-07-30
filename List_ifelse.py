# using if else statements in list
# Create a list
from matplotlib.style import available


Fast_Food = ["Samosa" , "Momos", "Panipoori" ,"Chowmin", "Chholabhatoora", "Kachori"]
for Fast_Food in Fast_Food:
    if Fast_Food=="Momos":
        print("Sorry, we are out of Momos right now.")
    else:    
       print(f"Adding {Fast_Food}")
print("Finished your chicken chilli! \n")

available_alphabate = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
requested_alphabate = ["a", "e", "g", "k"]
for requested_alphabate in requested_alphabate:
    if (requested_alphabate in available_alphabate):
       print(f"Adding {requested_alphabate} \n")
    else:
        print(f"Sorry, we don't have {requested_alphabate}")

print("Fininshed your request:")