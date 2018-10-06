def function_01(N):
    first=1
    second=1
    for step in range(N-1):
        second+=first
        first=second-first
    print(second)

def function_02(N):
    first=1
    second=1
    third=1
    print(first,second,third)
    for step in range(N-2):
        third=second + first + third
        second=third-first-second
        first= third - second - first
    print(third)


def function_03_version_1(N):
    list=[]
    z=1
    for i in range(N//2):
        list.append((i*2+1)**2)
    print(list)

def function_04_version_1(a,b):
    for i in range(b):
        print('*'*a)

def function_03_version_2(N):
    print([i**2 for i in range(N) if i%2==1])

def function_04_vversion_2(a,b):
    for i in range(b):
        if i!=0 and i!=b-1:
            print('*'+' '*(a-2)+'*')
        else:
            print('*' * a)

def function_05(a,b):
    sum=0
    pr=1
    for i in range(b-a+1):
        sum+=a+i
        pr*=a+i
    print("Сумма=",sum,", произведение=",pr)

def function_06(a,b):
    print([a+i for i in range(b-a+1) if i%2==0])
    print([a+i for i in range(b-a+1) if i%2!=0])

def function_07(list):
    print([i for i in list if i>0])
    print([i for i in list if i<0])



