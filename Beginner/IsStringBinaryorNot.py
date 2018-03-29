def main():
  String=input("Enter String")
  count=0
  for i in String:
    if int(i)==1 or int(i)==0:
      pass
    else:
      count+=1
  if count>0:
    print("No")
  else:
    print("Yes")
main()
