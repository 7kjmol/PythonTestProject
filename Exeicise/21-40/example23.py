'''
打印出如下图案（菱形）:
   *
  ***
 *****
*******
 *****
  ***
   *
'''

for i in range(1, 5):
    for j in range(0, 5 - i):
        print(' ', end="")
    for j in range(0, (i * 2) - 1):
        print('*', end="")
    print('\n', end="")

for i in range(1, 4):
    for j in range(0, i + 1):
        print(' ', end="")
    for j in range(0, (4 - i) * 2 - 1):
        print('*', end="")
    print('\n', end="")
