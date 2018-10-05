import numpy as np
l=np.random.randint(2,10)
a=np.zeros(l)
for i in range(l):
    a[i]=np.random.random()
print(a)

print(np.average(a))