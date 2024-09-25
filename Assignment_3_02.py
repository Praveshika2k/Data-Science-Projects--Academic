import numpy as np
n = int(input("Enter the size:"))
l = []
c = 0
j = 0
i = 0
while i < n:
    x = int(input())
    if x > 0:
        l.append(x)
        i += 1
    else:
        print("Enter a positive integer.")
l1 = np.array(l)
for i in range(n):
    if(i!=n-1):
        if(l1[i]%2==0 and l1[i+1]%2==0):
            c = c+1
print(c)