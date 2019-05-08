'''
题目：暂停一秒输出。
程序分析：使用 time 模块的 sleep() 函数。
'''
import time
while True:
    localtime = time.localtime(time.time())
    print(time.strftime("%Y-%m-%d %H:%M:%S", localtime))
    time.sleep(1)
