
def function_01(i):
    j=2
    step=1
    while (j<i):
        j += 2**step
        print(j, 2 ** step)
        step+=1
    print(step)

def function_02(i):
    list=[1]
    j=2
    sum=j
    while (sum<i):
        j_prost=True
        for k in list[1:]:
            if j%k==0:
                j_prost=False
                continue
        if j_prost:
            list.append(j)
            sum+=j
        j+=1
    print(len(list))
    print(list)

def function_03(days):
    start=10
    way=start
    for i in range(days):
        way+=start
        if i%2==0:
            start*=1.15
    print(way)

def function_04a(lim_day_way):
    day=1
    day_way=10
    way=day_way
    while day_way<=lim_day_way:
        day_way*=1.1
        day+=1
    print(day)

def function_04b(lim_sum_way):
    day=1
    day_way=10
    way=day_way
    while way<lim_sum_way:
        day_way*=1.1
        day+=1
        way+=day_way
    print(day)
