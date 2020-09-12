# coding=utf-8
import math,os

# file = input("Enter the input file:")
file = 'D:\pythonlearn\inputs\input-day1.txt'
print("--------")

with open(file,"r") as rf:
    lists = rf.readlines()


sumTotal = 0

for i in range(0,len(lists)):
# for i in range(0, 2):
    lists[i] = lists[i].strip('\n')
    sum = inputNum = int(lists[i])
    print("sum1:" + str(sum))
    print("loop:" + str(i))
    fuel = math.floor(inputNum /3) -2
    while (fuel >= 0):
        print("--------")
        print('fuel:'+str(fuel))
        sum = sum + fuel
        fuel = math.floor(fuel/3) -2

        print("sum:"+str(sum))
        print("--------")
    sumTotal = sumTotal+sum
    print("--------")
    print('sumTotal:' + str(sumTotal))

print("--------")
print(sumTotal-3349352)
