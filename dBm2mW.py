#!/usr/bin/python
# -*- coding: utf-8 -*-​
# dBm to mW and mw to dBm converter
import sys
from math import log10

# Function to extract numbers from string
def getdigits(ch):
    if "," in ch:
	ch = ch.replace(',','.')

    if '.' in ch:
        return float(''.join(ele for ele in ch if ele.isdigit() or ele == '.'))
    else:
        return int(''.join(ele for ele in ch if ele.isdigit()))

# Function to convert from mW to dBm
def mW2dBm(mW):
    return 10.*log10(mW)

# Function to convert from dBm to mW
def dBm2mW(dBm):
    return 10**((dBm)/10.)



# Main thread
# if there's space between argument and "dBm"
if len(sys.argv) > 2:
    sys.argv[1] = sys.argv[1] + sys.argv[2]

if len(sys.argv) > 1:
    if "MW" in sys.argv[1].upper():
	mW = getdigits(sys.argv[1])
	dBm = mW2dBm(mW)
	print "%d mW = %0.2f dBm" %(mW,dBm)
    elif "DBM" in sys.argv[1].upper():
	dBm = getdigits(sys.argv[1])
        if "-" in sys.argv[1]:
            dBm = -dBm
            mW = dBm2mW(dBm)
	    print "%0.2f dBm = %0.10f mW" %(dBm,mW)
	else:
            mW = dBm2mW(dBm)
	    print "%0.2f dBm = %d mW" %(dBm,mW)
    else:
	# bad syntax
        print "Usage: Enter input value as 9.99dBm or 999mW"
else:
    # print table for 100-2000 mW to dBm
    print "Usage: Enter input value as 9.99dBm or 999mW"
    print "-"*20
    for mW in range(2000, 0, -100):
	dBm = mW2dBm(mW)
	print "%d mW = %0.2f dBm" %(mW,dBm)
    print "-"*20
    # print table for 10-34 dBm to mW
    for dBm in range(10, 34, 1):
	mW = dBm2mW(dBm)
	print "%0.2f dBm = %d mW" %(dBm,mW)
    print ""
