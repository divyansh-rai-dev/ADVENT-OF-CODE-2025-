n = int(input("enter the n: "))
a = 0
b = 1
next = b  
step = 1
list = []
while step <= n:
    print(next)
    step += 1
    a, b = b, next
    next = a + b
    list.append(next)


print()
print(f" total:   {sum(list)} ")

# print fibo and sum of it 