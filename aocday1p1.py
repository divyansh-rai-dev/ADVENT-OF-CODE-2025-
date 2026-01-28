i = 50
count = 0
with open('aocday1.txt', "r") as file:
    for line in file:
        b = line[0]
        c = line[1:]

        d = int(c)
        if b == 'L':
            x = (i + d) % 100
            i = x
            if i == 0:
                count +=1
        else:
            x = (i - d) % 100
            i = x
            if i == 0:
                count += 1

print(count)
