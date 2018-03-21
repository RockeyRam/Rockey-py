n=int(input("Enter Number"))
li=[]
while n>1:
  mod=n%10
  li.append(mod)
  n=n//10
print(sum(li))
