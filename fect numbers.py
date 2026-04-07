import math
n=int(input("Enter a number:"))
root = math.isqrt(n)
if root*root==n:
    print("Perfect Square")
else:
    print("Not a Perfect Square")
    
n=int(input("Enter a number:"))
sum=0
for i in range(1,n):
    if n %i==0:
    sum=sum+i
if sum==n:
 print("Perfect Number")
else:
print("Not a Perfect Number")
