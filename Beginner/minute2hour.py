import sys
minute=int(input("Enter How many minutes"))
ma=round((minute/60),2)
hour=str(ma)
ans=hour.split(".")
for i in ans:
  sys.stdout.write(i)
  sys.stdout.write(" ")
