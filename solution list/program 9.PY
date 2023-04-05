def dictor(list1):

    dics={}

    for i in range(0,len(list1),3):

        dic[list1[i]]=list1[i+1:i+3]

    print(dics)


def takein():
    vis=[]
    a="y"
    while a=="y" or a=="Y":
        
        b1=int(input("Student id:"))
        vis.append(b1)
        
        b2=input("Student name:")
        vis.append(b2)
        
        b3=float(input("Student percentage:"))
        vis.append(b3)
        
        a=input("Do you add more ?(y/Y):")
    print(m)
    dictor(m)

takein()