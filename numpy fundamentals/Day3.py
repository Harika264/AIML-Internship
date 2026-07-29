import numpy as np

print("NumPy Day 3 Practical")

a=np.array([10,20,30,40,50])

print("Array:",a)

print("First Element:",a[0])

print("Last Element:",a[-1])

print("Slice:",a[1:4])

print("Sum:",np.sum(a))

print("Mean:",np.mean(a))

print("Maximum:",np.max(a))

print("Minimum:",np.min(a))

b=np.array([5,4,3,2,1])

print("Addition:",a+b)

print("Subtraction:",a-b)

print("Multiplication:",a*b)

print("Division:",a/b)

c=np.array([1,2,3,4,5,6])

print("Reshaped Array")

print(c.reshape(2,3))
