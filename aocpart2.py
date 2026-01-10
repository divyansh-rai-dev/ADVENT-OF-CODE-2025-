
def count_zero_clicks(instructions):
    pos = 50  # starting position
    total_zero_hits = 0

    for line in instructions:
        line = line.strip()
        if not line:
            continue
        
        direction = line[0]      # 'L' or 'R'
        steps = int(line[1:])    # how many clicks
        
        # step direction
        if direction == 'R':
            step = 1
        else:
            step = -1
        
        # simulate every click
        for _ in range(steps):
            pos = (pos + step) % 100
            if pos == 0:
                total_zero_hits += 1

    return total_zero_hits


if __name__ == "__main__":
    # read input.txt from same folder
    with open("input.txt") as f:
        instructions = f.readlines()

    answer = count_zero_clicks(instructions)
    print("Password (Part 2) =", answer)
