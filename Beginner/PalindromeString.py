#Palindrome-beginer-set-8
def Palindrome(S):
    Rev=S[::-1]
    if S == Rev:
        print("It is Palindrome")
    else:
        print("NO")
a=str(input("Enter the String"))
Palindrome(a)
    
