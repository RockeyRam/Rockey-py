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
no=int(input("Enter Integer"))
count=0
while no>0:
    rem=no%10
    no=no/10
    count=count+1
print("There are {0} digits".format(str(count)))
