#Beginer-set8-2
def StringVowel(vo):
    count=0
    for i in vo:
        if i=='a' or i=='A' or i == 'E' or i == 'e' or i == 'I' or i == 'i' or i=='o' or i=='O' or i=='u' or i=='U':
            count=count+1
    if count>0:
        print("Vowel")
    else:
        print("Not Vowel")
a=str(input("Enter String"))
StringVowel(a)
