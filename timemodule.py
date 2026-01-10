import time

n = int(input(">"))

for i in range (n , 0 , -1):
    x = i /  3600
    y = int(i / 3600) % 60 
    z = int(i % 3600)
    print(f"{z:.2}:{y:.2f}:{x:.2f}")
    time.sleep(1)

print(" ")