'''
题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
'''

str = 'abcde'

def output(str):
    if(len(str) > 0):
        print(str[len(str) - 1])
        output(str[0:len(str) - 1])
    else:
        return

output(str)
