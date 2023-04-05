
def channame(li):
    name=[]
    a=".c"
    for i in li:
        if a in i: 
            b=i.replace(".c",".py")
            name.append(b)
        else:
            name.append(i)    

    print(name)    

f= ["program.c","stdio.c","sample.c","a.py","math.py","hpp.py"]
channame(fi)