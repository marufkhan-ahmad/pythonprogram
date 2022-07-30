#create variable
x=7
y="Sally"
print(x)
print(y)
#type casting
x = str(3)
y = int(2)
z = float(4)
print(x)
print(y)
print(z)


#get the type of data type
x = 4
print(type(x))

y = 9.0
print(type(y))
 
z = 'a'
print(type(z))


#single or double quotes
a = "john"
a = 'john'
print(a)
print(a)

#Case-sensitive
a=4
A="Sally"
print(a)
print(A)

# len function in  data type

num_char = len(input("What is your name?"))
new_num_char = str(num_char)
print("your name has " + new_num_char + " characters.")
print(type(num_char))

# operation on data type

a = float(123)
print(type(a))
# concatenate integer and float value result will be in float
print(70 + float("100.5"))
# concatenate two string results will be string
print(str(70)+str(100))


# BMI calculator
# BMI = weight (kg)/height(meter*meter)
height = input("Enter your height in m:")
weight = input("Enter your mass in kg:")
BMI = int(weight)/float(height)**2
print(int(BMI))
