#write a script to create a list with 5 string and count total number of length with string using UDF.
def evstr(a):
    v=[]
    s=0
    for i in a:
        if(len(i)%2==0):
            v.append(i)
            c=c+1
    if(c>0):
        print('number of even string is {} and string :{}'.format(c,s))
    else:
        print("No even string")

lis=[]
for i in range(5):
    b=input("Enter string:{}:".format(i+1))
    lis.append(b)    
evstr(lis)    