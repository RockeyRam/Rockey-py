#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Administrator
#
# Created:     23-02-2018
# Copyright:   (c) Administrator 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
year=int(raw_input("Enter Year"))
if year%400==0:
    print("{0} is leap Year".format(year))
elif year%4==0:
    print("{0} is leap Year".format(year))
elif year%100==0:
    print("{0} is not leap Year".format(year))
else:
    print("{0} is not a leap Year".format(year))