'''
题目：判断101-200之间有多少个素数，并输出所有素数。
程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。
'''
import math


def isSushu(num):
    flag = True
    for i in range(2,int(math.sqrt(num))):
        if((num % i) == 0):
            flag = False;break
    return flag


for i in range(100,201):
    if(isSushu(i)):
        print(i)
