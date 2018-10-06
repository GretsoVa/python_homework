import numpy as np
l=np.random.randint(2,10)
a=np.zeros(l)
for i in range(l):
    a[i]=np.random.random()
print("Массив: ",a)

a_avr=np.average(a)
print("Среднее значение: ",a_avr)

S=sum((a-a_avr)**2)/len(a)
print("Стандартное отклонение массива: ",S)

a=[[3,1],[1,2]]
b=[9,8]
solution = np.linalg.solve(a,b)
print("Решение уравнения ",a,"x=",b," :",solution)