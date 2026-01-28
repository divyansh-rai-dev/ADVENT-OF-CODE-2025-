i = 50
count = 0

with open("aocday1.txt") as f:
    for line in f:
        line = line.strip()
        direction = line[0]
        d = int(line[1:])

        for _ in range(d):
            if direction == 'L':
                i += 1 
                if i == 100:
                    i = 0
            else:
                i -= 1
                if i == -1:
                    i = 99

            if i == 0:
                count += 1

print(count)