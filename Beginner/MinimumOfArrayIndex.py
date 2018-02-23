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
TotalInt=[]
a=input("Enter How many Integers")
for i in range(0,a):
    x=int(x=input("Enter No"))
    TotalInt.insert(i,x)
    i+=1
print("The Minimum Number is "+str(min(TotalInt)))