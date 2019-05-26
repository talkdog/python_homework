x = str(input('請輸入家庭用電(1)或工業用電(2)代號:'))
z=eval(input("請輸入度數:"))
if x == "家庭用電":
    if z<=240:
        print(z*0.15)
    elif 241<= z <=540:
        print(240*0.15+(z-240)*0.25)
    else:
        print(240*0.15+(z-(240+z-540))*0.25+(z-540)*0.45)
else:
    print(z*0.45)