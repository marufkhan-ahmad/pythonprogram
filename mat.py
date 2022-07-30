# matplotlib training tutoril
from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
a=pd.read_csv(r"C:\Users\mk744\Downloads\iris.csv")
data = pd.read_csv(r"C:\Users\mk744\Downloads\iris.csv",names=["SL","SW","PL","PW","Class"])
print(a)
print(data)
x= data["SL"]
y= data["SW"]
a= data["PW"]
b= data["PL"]
#x = np.array([1,2,3,4,5,6,7,8,9])
#y = np.array([1,2,3,4,5,6,7,8,9])
# plt.plot(x,y,color="red",ls = "-.")
plt.xlabel("X - axis")
plt.ylabel("Y - axis")
plt.title("Simple Line Graph")
# plt.scatter(x,y,color="red",ls="-.")
plt.scatter(x,y,color="green",marker='D',s=30,alpha=0.5)
plt.scatter(a,b,color="red",marker='*',s=30,alpha=0.5)
plt.show()