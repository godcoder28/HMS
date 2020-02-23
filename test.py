n=input("str")
l=n.split()
for i in l:
    l2=list(i)
    if l2[0]=='t' or l2[0]=='T':
        print(i)

