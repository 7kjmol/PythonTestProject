'''
题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
'''

height = 100
sum = 0 + 100
for time in range(0,9):
    height = height / 2
    sum = sum + height * 2
print("sum:%f. height:%f" %(sum,height / 2))#第10次反弹多高,第十次未弹起，应该再除以2