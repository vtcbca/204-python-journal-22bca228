def symme(vi):
    h=(len(lvi)//2)
    f=lis[:h]
    s=lis[h:]
    if f==s:
        print("String {} is symmetric!!!!".format(lis))
    else:
        print("String {} is not symmetric!!!".format(lis))



v=input("Enter a string:")
symme(v)
          