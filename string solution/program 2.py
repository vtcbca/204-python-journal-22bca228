#write a script to enter any sentence and print those word which is palindrome also print total number of palindrome word.
vinput("Enter sentece:")
s=sr.split(" ")
a=0
d=[]
for i in s:
    if (i==i[::-1]):
        a=a+1
        d.append(i)
if a>0:
    print('number of palindrome word in sentence is {} and palindrome words are:{}.'.format(a,d))              
else:
    print(" no palindrome word in sentence!!!")    

   