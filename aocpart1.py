#!/usr/bin/env python3
import sys

def count_zero_hits(instructions):
    pos = 50        # starting position
    zero_hits = 0   # how many times we land on 0

    for instr in instructions:
        instr = instr.strip()
        if not instr:
            continue
        direction = instr[0].upper()      # 'R' or 'L'
        steps = int(instr[1:])            # number after it

        if direction == 'R':
            pos = (pos + steps) % 100
        else:  # 'L'
            pos = (pos - steps) % 100

        if pos == 0:
            zero_hits += 1

    return zero_hits

def read_instructions_from_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return [line.rstrip('\n') for line in f]

def read_instructions_from_stdin():
    # read all lines from stdin
    return [line.rstrip('\n') for line in sys.stdin]

def main():
    # Usage:
    # 1) python3 dial.py input.txt         (reads lines from input.txt)
    # 2) cat input.txt | python3 dial.py   (reads from stdin)
    # 3) python3 dial.py                   (then paste lines, Ctrl-D to finish)
    if len(sys.argv) >= 2:
        path = sys.argv[1]
        instructions = read_instructions_from_file(path)
    else:
        # If no filename provided, read from stdin (pipe or interactive)
        print("Paste your instructions (one per line). Press Ctrl-D (or Ctrl-Z then Enter on Windows) when done:")
        instructions = read_instructions_from_stdin()

    result = count_zero_hits(instructions)
    print(result)

if __name__ == "__main__":
    main()
