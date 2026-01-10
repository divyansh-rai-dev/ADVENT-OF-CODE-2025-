# total = 0
# with open("inputday3.txt") as f:
#     for line in f:
#         a = line.strip()
#         s= set(a)
#         max_joltage = 0

#         for i in range(len(s) - 1):
#             value = int(s[i] + s[i +1])
#             if value > max_joltage:
#                 max_joltage = value
#         total += max_joltage

# print(total)


import time 

for x in range(10): 
    print(f"\r{x}", end="")
    time.sleep(1)