'''
题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。
请参照程序Python 练习实例14。
'''
import math


def isWanShu(num):
    sum = 0
    i = 1
    for i in range(1, num):
        if(0 == (num % i)):
            sum = sum + i
    if(num == sum):
        return num
    else:
        return 0
for num in range(1,1000):
    if(0 != isWanShu(num)):
        print("%d" % num)