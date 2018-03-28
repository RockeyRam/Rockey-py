def main():
  a=int(input("Enter Range"))
  x=0
  y=1
  for i in range(0,a):
    print(x)
    nextn=x+y
    x=y
    y=nextn
main()
