def Prime():
    Num=int(input("Enter the Number"))
    if Num > 1:
        for i in range(2,Num):
            if(Num % i==0):
                print("It is not a prime number")
                break
            else:
                print("It is prime number")
    else:  
       print(num,"is not a prime number")  
Prime()
