
class Warehouse:
    square=100
    floor=1
    row=6
    placeinrow=5

class Equipment:
   vendor="Huawei"
   voltage=220
   place=2
   color="white"
   weight=5
   serial_number="qwwqe1223131lkjasdp"
   prod_date=20-03-2020

class Printer(Equipment):
    pr_speed=12
    doubleside=True
    printtype="Laser"
    printcolor="Color"
    interface="wi-fi"
    maxsheetsize="A4"

class Scaner(Equipment):
    sensortype="CIS"
    resolution="2400x2400"
    format="PDF"

class Xerox(Equipment):
    maxsheetspermonth= 80000
    colordepth=24
    scale="25-400 %"
