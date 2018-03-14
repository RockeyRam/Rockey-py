def main():
  String=input("Enter String:")
  count=0
  for i in String:
    if i.isdigit() or i.isalpha():
      pass
    else:
      count+=1
  print("The Number of numeric in a String:",count)
main()
