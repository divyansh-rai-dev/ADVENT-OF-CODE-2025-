import timeit

n = int(input(">"))

t = 0
for i in range(1 , n//2 +1):
    if n % i ==0:
        t +=i 

if n == t:
    print("is perfect")

else:
    print("not perfect")

