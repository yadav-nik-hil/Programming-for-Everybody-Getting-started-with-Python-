# -*- coding: utf-8 -*-
"""
Created on Sat May 16 14:48:20 2020

@author: Nikhil Yadav
"""

def computepay(h,r):
	if h<=40:
		pay = h*r
	elif h>40:
		pay = 40*r + (h-40)*r*1.5
	return pay

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter rate:")
r = float(rate)
p = computepay(h,r)
print("Pay",p)