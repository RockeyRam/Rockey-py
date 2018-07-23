def Fact():
    Num=int(input("Enter the value"))
    fact=1
    while Num>0:
        fact=fact*Num
        Num=Num-1
    print("The Factorial is ",fact)
Fact()
