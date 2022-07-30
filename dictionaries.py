# create a dictionary
method = {"color":"blue", "point":10}
print(method)
method["x_position"] = 0
method["y_position"] = 25
print(method)

# create a dictionary and show the axis 
Test = {"color": "red", "cloth": "T-shirt", "Money": "$125"}
print(Test)
Test["a_position"] = 5
Test["b_position"] = 15
print(Test)

# create an empty dictionary and show the data inside it
sample = {}
sample["color"] = "green"
sample["points"] = 5
print(sample)

# create another dictionary and show the data inside it
Demo = {}
Demo["Name"]="Maruf Khan"
Demo["Age"]=23
Demo["Occupation"]="Engineer as an intern"
print(Demo)

# create a simple running boat program
boat = {"x_position": 0, "y_position": 20, "z_position": 30, "Speed": "medium"}
print(f"Original position : {boat['x_position']}")
print(f"Original position : {boat['y_position']}")
print(f"Original position : {boat['z_position']}")

# move the boat to the right
if boat["Speed"]=="slow":
    x_increment = 1

elif boat["Speed"]=="medium":
    x_increment = 2

else:
    x_increment = 3

# the new position is the old position plus the increment
boat["x_position"] = boat["x_position"] + x_increment
print(f"New position:{boat['x_position']}")
