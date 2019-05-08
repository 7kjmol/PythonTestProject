'''
题目：输入某年某月某日，判断这一天是这一年的第几天？
程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于2时需考虑多加一天：
'''
import time


def isLeapYear(year):
    if((year % 100) != 0 and year % 4 == 0):
        return True
    else:
        return False


date = "2019-03-21"
sumDayNum = 0
monNumList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
i = 0
while i < (time.strptime(date,"%Y-%m-%d").tm_mon - 1):
    sumDayNum += monNumList[i]
    i = i + 1
sumDayNum += time.strptime(date,"%Y-%m-%d").tm_mday

print(sumDayNum)