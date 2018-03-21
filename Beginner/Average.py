a=int(input("Enter How many Input"))
holder=[]
for i in range(0,a):
  x=int(input())
  holder.insert(i,x)
print("The Average is",round(sum(holder)/a))
