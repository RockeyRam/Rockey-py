#SET-3,Q-30
a=str(input("Enter time"))
b=str(input())
a=a.split()
b=b.split()
x=int(a[0])
y=int(b[0])
m=int(a[1])
n=int(b[1])
hour=abs(x-y)
minute=abs(m-n)
print(str(hour)+" "+str(minute))
