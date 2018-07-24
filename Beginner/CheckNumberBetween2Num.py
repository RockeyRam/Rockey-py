#Beginner-set-8-73
def CheckNumberBetween2Num(Number,Number2,Number3):
    if (Number>Number2 and Number < Number3):
        print("Yes")
    else:
        print("No")
a=int(input("Enter number"))
b=int(input("Enter 2 numbers"))
c=int(input())
CheckNumberBetween2Num(a,b,c)
