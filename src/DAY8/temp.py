import numpy as np
a=np.array([1,2,3])
b=np.array([2,4,6])
print(a+b)

a = np.arange(12)   
reshaped = a.reshape(3,4)
print(reshaped)


a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
result = np.vstack((a, b))
print(result)


data=np.array([[10,20,30],[40,50,60]])
print(np.mean(data))
print(np.mean(data,axis=0))


arr = np.linspace(0, 10, 5)
print(arr)


