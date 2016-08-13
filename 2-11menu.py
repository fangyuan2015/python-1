#!/usr/bin/env python
#File name : menu.py  
while True:
    alist=[1,2,3,4,5]
    print """The five num is:
1,2,3,4,5
Please choice:
1 get the five num sum
2 get the five num avg
x exit the program"""
    cho=raw_input("Please input you choice: ")
    if cho is '1':
        sum = 0
        for i in alist:
            sum += i
        print "The sum is %s :" % sum
    if cho is '2':
        sum = 0
        for i in alist:
            sum += i
        print "The avg is %f:  " % (sum/5)
    if cho is 'x':
       break
