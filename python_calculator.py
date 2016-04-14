from time import sleep
from datetime import datetime
from math import pi

now =  datetime.now()
print "The calculator is starting up"
month_now = now.month
day_now = now.day
year_now = now.year
hour_now= now.hour
minute_now = now.minute
print " %s/%s/%s %s:%s" % (month_now, day_now, year_now, hour_now, minute_now)
sleep(1)
hint = "Don't forget to include the correct units! \nExiting..."
option = raw_input("Enter C for Circle or T for Triangle:")
option = option.upper()


if option == "C":
    radius = float(raw_input("Put radius number"))
    area = pi*radius**2
    print "The pie is baking..." 
    sleep(1)  
    print("Area: %.2f. \n%s" % (area, hint))                 
elif option =="T":
    base = float(raw_input("Put base number"))             
    height = float(raw_input("Put heigh number"))
    area = height*base 
    print "Uni Bi Tri..."
    sleep(1) 
    print "Area %.2f. \n%s" % (area, hint) 
else:
    print "You was puting garbage and program will exist"      
                   
