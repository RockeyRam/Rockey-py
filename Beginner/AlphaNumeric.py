def alphanum():
  String=str(input("Enter String"))
  al=0
  num=0
  for i in String:
    if i.isalpha():
      al+=1
    elif i.isdigit():
      num+=1
  if al!=0 and num!=0:
    print("Yes")
  else:
    print("No")
alphanum()
