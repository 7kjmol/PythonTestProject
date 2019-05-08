'''
题目：利用递归方法求5!。
程序分析：递归公式：fn=fn_1*4!
'''

def factorial(num):
    if(1 == num):
        return 1
    else:
        return (factorial(num - 1) * num)

print(factorial(5))

