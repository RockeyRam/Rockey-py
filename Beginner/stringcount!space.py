def main():
    length=0
    full_name = str(input("Please enter in a full name: ")).split(" ")
    for x in full_name:
      length+=len(x)
    print(length)
main()
