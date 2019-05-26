x=eval(input('請輸入一個正整數:'))
'''for i in range(1, x, 1):
    for j in range(x, 0, -1):
        if i*j == x and j>=i:
            print('{0},{1}'.format(i, j),   sep=', ', end=',')
 '''
total = 0
for i in range(1, x+1, 1):
    if x%i==0:


        print(i, end=', ')

