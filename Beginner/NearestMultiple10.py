def NearestMultiple10():
    N=int(input("Enter the Number"))
    a=(N//10)*10
    b=N+10
    if N-a > b-N:
        print(b)
    else:
        print(a)
NearestMultiple10()
