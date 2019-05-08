'''
题目：斐波那契数列。
程序分析：斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
在数学上，费波那契数列是以递归的方法来定义：
'''
'''
def fibonacci(num1):
    print(num1)
    fibonacci(num2, num1 + mum2)
'''
count = 10
num1 = 0;num2 = 1
for i in range(1, count):
    print(num1)
    temp = num1 + num2
    num1 = num2
    num2 = temp

