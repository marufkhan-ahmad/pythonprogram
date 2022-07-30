from math import remainder


num=int(input("Enter a number:"))
#initialize sum with 0
sum =0
#store num value in temp
temp = num
while temp>0:
    remainder = temp%10
    sum += remainder**2
    temp//=10
    if num==sum:
        print(sum,"Number is Armstrong :")
    else:
        print(sum,"Number is not Armstrong:")
        