# coding=utf-8
import math,os

# file = input("Enter the input file:")
file = 'D:\pythonlearn\inputs\input-day1.txt'
print("--------")

with open(file,"r") as rf:
    lists = rf.readlines()

sum = 0

for i in range(0,len(lists)):
    lists[i] = lists[i].strip('\n')
    inputNum = int(lists[i])
    sum = sum + math.floor(inputNum /3) -2
print("--------")
print(sum)
