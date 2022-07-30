# removing key-value pairs from a dictionary and key-value will be deleted for forever
# create a dictionary
Fine={"Hello":"Maruf", "Your Point is ":60, "Good morning":"Maruf"}
print(Fine)
del Fine["Your Point is "]
print(Fine)

# create even number from 1 to 20
number = {"Number": 2, "Number1": 4,"Number2":6, "Number3":8, "Number4":10, 
"Number5":12,"Number6":14,"Number7":16,"Number8":18,"Number9":20}
print(number)
del number["Number9"]
print(number)
