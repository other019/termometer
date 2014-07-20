import time
import csv

while True:
    with open("/sys/bus/w1/devices/28-000003ead460/w1_slave","r") as f:
        tem=f.read()
    
    tem = tem.split("\n")
    tem = tem[1]
    tem = tem.split(" ")
    tem = tem[9]
    tem = tem[2:]
    tem=float(tem)/1000
    
    tim= time.localtime()
    tim=time.mktime(tim)
    tim= time.strftime("%Y/%m/%d %H:%M " )
    with open('data.csv','a') as csvf:
        csvw=csv.writer(csvf, delimiter=',',quotechar=' ', quoting=csv.QUOTE_MINIMAL)
        csvw.writerow([tim, tem])
    tem="{0:.3f}".format(tem)
    time.sleep(600)


