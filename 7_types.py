def function_01(n,st):
    print(st*n)

def function_02(n):
    for i in range(n):
        print('='*(i+1))

def function_03(st):
    d={}
    for i in range(len(st)):
        if (d.get(st[i],0)==0):
            d[st[i]]=1
        else:
            d[st[i]]+=1
    for i in d:
        print (i,d[i])

def function_04(st):
    d={}
    k=st.split()
    for i in range(len(k)):
        if (d.get(len(k[i]), 0) == 0):
            d[len(k[i])]=1
        else:
            d[len(k[i])]+=1
    for i in d:
        print(i,d[i])
