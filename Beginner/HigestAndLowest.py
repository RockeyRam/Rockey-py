a=int(input("Enter How many Input"))
holder=[]
for i in range(0,a):
  x=int(input())
  holder.insert(i,x)
print("The Highest Number is",max(holder))
print("The Lowest number is",min(holder))
