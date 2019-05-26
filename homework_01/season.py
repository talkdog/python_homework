season = eval(input("請輸入月份:"))
if season in (11, 12, 1):
    print("冬天")
elif season in(2 , 3,  4):
    print("春天")
elif season in(5, 6, 7):
    print("夏天")
elif season in(8, 9, 10):
    print("秋天")
else:
    print("輸入錯誤")