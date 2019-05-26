def power(x, y):
    total = 1
    for i in range(1, y+1, 1):
        total *= x

    return total
def main():
    x = eval(input('請輸入數值:'))
    y = eval(input('請輸入次方數值:'))

    print('{}的{}次方等於{}'.format(x, y, power(x, y)))
main()
