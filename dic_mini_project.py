Enemy = {"color": "green", "Name": "alien"}
Enemy["Speed"]="Fast"
Enemy["Speed"]="Medium"
Enemy["Speed"]="Slow"
Enemy["x_position"]=0
Enemy["y_position"]=5
Enemy["z_position"]=10
print(Enemy)

# Find the enemy position
print(f"Original position of the enemy : {Enemy['x_position']},{Enemy['y_position']},{Enemy['z_position']}")

# Move the Enemy to the right
if(Enemy["Speed"] == "Fast" or Enemy["x_position"] == 0):
    x_increment = 1

elif(Enemy["Speed"] == "Slow" or Enemy["y_position"] == 5):
    y_increment =2


elif(Enemy["Speed"] == "medium" or Enemy["z_position"] == 10):
    z_increment =3

else:
    x_increment =0
    y_increment =0
    z_increment =0
# The new position is the old position plus the increment.
Enemy["x_position"] = Enemy["x_position"] + x_increment
Enemy["y_position"] = Enemy["y_position"] + y_increment
Enemy["z_position"] = Enemy["z_position"] + z_increment
print(f"New position of the enemy : {Enemy['x_position']},{Enemy['y_position']},{Enemy['z_position']}")
