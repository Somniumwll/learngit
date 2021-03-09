import numpy as np
import matplotlib.pyplot as plt
alpha = 5
#alpha=1
#alpha=0.5 ,alpha=0.2
x = 1
#x=2, x=3,x=4
def f(x):
    y=np.sqrt((5+4*np.cos(x))/4)+np.sqrt((5-4*np.cos(x))/4)
    return y


def myf(x):
    return (-4 * np.sin(x) / np.sqrt(5 + 4 * np.cos(x)) + 4 * np.sin(x) / np.sqrt(5 - 4 * np.cos(x)))

x1=[]
x1.append(1)
y1=[]
for t in range(0,100):
     x=x-alpha*myf(x)
     print("第%d次迭代：x=%f,y=%f"%(t+1,x,f(x)))
     #plt.xlabel("x")
     #plt.ylabel("f(x)"#
     #plt.plot(x)
    # plt.show()
     x1.append(x)
     y1.append(f(x))

print(x1,y1)
plt.plot(x1,)
plt.plot(y1)
plt.show()
