import os
n = int(os.getenv("n")) 
x = int(os.getenv("x")) 

sum1 = 1

for i in range(2,n+1):
    sum1 = sum1 + (((x**i)-i)/i)
print("The sum of series is ",round(sum1,2))
