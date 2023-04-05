def coomon(lis):
    c=0
    b=[]
    for i in range(len(lis)-2):
        if lis[i]=lis[i+1] and lis[i+1]==lis[i+2]:
            b.append(lis[i])
            c+=1
    if c>0:
        print(f"Consecutive common numbers are {c} as follow:{b}")
    else:
        printf("No consecutive number!!")
def takei():
    vid=[]
    b=int(input("How many number you want to enter in list:"))
    for i in range(b):
        c=int(input("Enter value:"))
        vid.append(c)
    coomon(n)        

takei())    