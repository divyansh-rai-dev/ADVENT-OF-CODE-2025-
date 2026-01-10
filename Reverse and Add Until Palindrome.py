# 🔢 Question 4: Reverse and Add Until Palindrome  
# Difficulty: Medium  
# Concept: while loop, string manipulation, integer addition  
# Source: Inspired by HackerRank logic challenges  
# Problem:
# Given a number n, perform the following steps until you reach a palindrome number:
#   1. Reverse the digits of n.
#   2. Add the reversed number to the original.
#   3. If the result is not a palindrome, repeat the process.
#
# Finally, print:
#   - The palindrome obtained.
#   - The number of steps it took to reach it.
#
# Example:
# Input: 87
# Process:
#   87 + 78 = 165
#   165 + 561 = 726
#   726 + 627 = 1353
#   1353 + 3531 = 4884 ← palindrome
# Output:
#   4884
#   Steps: 4

n = int(input("enter a num: "))
 
l = 0 
while n > 0:
    l += 1
    a= str(n)
    c = a[::-1]
    d = int(c)

    n = n + d

    f = n
    y = 0

    while f > 0:
       

        x = f % 10

        y = y * 10 + x

        f = f // 10 
    if y == n:
        print(l)
        break
    
    else:
        continue

print(y)