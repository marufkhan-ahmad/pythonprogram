# use of for loop in the list
from cmath import log
from re import A
from matplotlib.pyplot import title


magic=["A","B","C","D"]
for magic in magic: 
     print(magic)

Maths_topic=["Algebra","Calculus","Trigonometry","Vector"]
for Maths_topic in Maths_topic:
     print(f"{Maths_topic.title()}, that's my favorite!")
     print(f"I can't wait to solve all the topics ,{Maths_topic.title()}\n")
     print("I am thankful to my teacher to help me in a better to use better approach to solve every topic \n")

# use a range() function
# range() function with numeric value
for value in range(1,10):
    print(value)

# using range to make a list of number
# to print numbers in a list using range() function from 1 to 10
numbers=list(range(1,20))
print(numbers)

# to print numbers from 1 to 100 in a list using range() function
A=list(range(1,100))
print(A)

# find the even and odd number using range() function
even_numbers=list(range(2, 20, 2))
print(even_numbers)

odd_numbers=list(range(3,20,3))
print(odd_numbers)

# How to find the square of a number using range() function
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)

# find cube
cubes = []
for value in range(1,11):
    cube = value**3
    cubes.append(cube)
print(cubes)

# Simple statics with a list of Numbers
digits = [1,2,3,4,5,6,7,8,9,10]
print("The Sum is:",sum(digits))
print("The minimum number is: ", min(digits))
print("The maximum number is: ", max(digits))

# print("The maximum number is: ", log(digits))

 



