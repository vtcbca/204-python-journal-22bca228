#python script to check string is palindrome or not
v=input("Enter string :")
s=v[::-1]
if(v==s):
    print("String  is palindrome !")
else:
    print("String is not palindrome !")
