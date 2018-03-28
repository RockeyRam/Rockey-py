def main():
  li=[]
  print("Enter 10 Numbers")
  for i in range(0,10):
    x=int(input())
    li.append(x)
  print("Greatest among 10 numbers",max(li))
main()
