# -*- coding: utf-8 -*-
from random import randint
import random

"""
Spyder Editor

This is a temporary script file.
"""

"""
aList = [3, 1, 0, 0, 3]

print ("Count for 3 : ", aList.count(3))
print ("Count for 2 : ", aList.count(2))
"""

"""


for i in range(8): #抓8次數值到list裡面
    L1=random.randint(0,3) #隨機產生0~2的數值100
    print(L1, end= ' ')
"""
    
"""
用while做累加
n=1
sum=0

while n<=10:
    sum=sum+n
    n+=1
print(sum)
"""

#用for做累加
# sum=0
# for i in range(1,100):
#     sum=sum+i
# print(sum)

#輸入一整數，得到整數平方根

n=int(input("請輸入一整數: "))
for i in range (n):
    if i*i==n:
        print("得到整數平方根",i)
        break #用break強制結束迴圈時，不會執行else部分
else:
    print("沒有整數平方根")
    






