# using individual value in a list
names=["Masum","Aftab","Sahid","Sohaib","Umar"]
print(names[4].title())
greetings=f"I met Umar during my internship and he's one of the best person I met him ever{names[4].title()}."
print(greetings)
greetings=f"Sahid is my cousin brother and he's very innocent{greetings[2].title()}"
print(greetings)

# changing, adding and removing elements into the list
motorbike=["Suzuki","KTM","Yamaha","Kawasaki"]
print(motorbike)
motorbike[1]="Ducati"
print(motorbike)

# to use append method
# create an empty list and use append function to insert elements into it
Animals=[]
Animals.append('Dog')
Animals.append('Lion')
Animals.append('Cat')
Animals.append('Goat')
print(Animals)

# TO INSERT ELEMENTS
names=["khan","Ahmad","Sayyad"]
names.insert(1,"Sheikh")
print(names)

# To delete elements from the list
del Animals[1]
print(Animals)

# use pop() method and last element from the list will come out
print(motorbike)
popped_motorbike= motorbike.pop()
print(motorbike)
print(popped_motorbike)

print(names)
pop_name=names.pop()
print(pop_name)


# poping element from any position
first_owned=names.pop(0)
print(first_owned.title())

second_owned=names.pop(1)
print(second_owned.title())


# Removing an item by value
Cars=["Toyota","Audi","BMW","Ferrarri"]
print(Cars)
too_expensive="Ferrarri"
Cars.remove(too_expensive)
print(Cars)
print(f"\nA {too_expensive.title()} is too expensive for me")