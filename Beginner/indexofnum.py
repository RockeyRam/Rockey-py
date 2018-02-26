a=int(input("Enter how many integer"))
array=[]
for i in range(a):
  x=int(input())
  array.append(x)
for i,j in enumerate(array):
  print("The number {0} is index of {1}".format(j,i))
