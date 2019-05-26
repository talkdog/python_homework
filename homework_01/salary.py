time = eval(input("請輸入工作時數:"))
x= time-60
y=time-80
z=time-(60+y)
if time <= 60:
    print(120*time)
elif 61<=time<=80:
    print(120*60+x*120*1.25)
elif time>=81:
    print (60*120+z*120*1.25+y*120*1.5)
