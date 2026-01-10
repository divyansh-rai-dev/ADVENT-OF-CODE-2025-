# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Write a Python program that:

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Asks the user to enter their age.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Converts the input into an integer.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Prints a message saying "You are X years old" where X is the age entered.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 👉 Remember: input() always returns a string, so you’ll need to convert it.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # a = input()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # b = int(a)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(f"You are {b} year old")






# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Write a Python program that:

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Takes a string input from the user.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Prints the first and last characters of that string.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Prints the middle three characters (if the string length is odd, take exact middle 3; if even, take the 3 around the center).

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Prints the string reversed.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Prints every second character from the string using slicing.


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # a = str(input())

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # b = len(a)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(a[0])
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(a[-1])

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # if b % 2 ==0:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     print(a[b//2])

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # else:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     print(a[b//2 + 1])

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(a[:-1])


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Write a Python program that:

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Takes a string input from the user.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Converts it to uppercase and prints it.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Converts it to lowercase and prints it.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Prints the number of characters in the string (excluding leading and trailing spaces).

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Prints whether the string starts with the letter "A" (case-insensitive).


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Replaces all spaces in the string with "-" and prints the new string.



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # a = str(input()).strip

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(a.upper)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(a.lower)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(len(a))
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # for i in (a):
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     print(i)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # b = list(a)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # c = a.replace(" " , "-")






# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Write a Python program that takes a string as input and prints:

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # The number of vowels in it

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # The number of consonants in it


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # a = str(input())

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # v = "aeiou"

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # c = a.lower()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # b = list(c)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # l = list()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # ll = list()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # for i in b:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     if i in v:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         l.append(i)
        
        
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     else:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         ll.append(i)
        
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(l)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # b = a.split()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # c = max(b , key=len)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # d = min(b , key=len)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(c)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(d)







# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Write a Python program that:

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Takes 5 numbers as input from the user (all in one line, separated by spaces).

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Stores them in a tuple.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Prints:

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # The maximum number

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # The minimum number

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # The sum of all numbers



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # z = input("Enter numbers: ").split()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(ll)





# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Write a Python program that takes a sentence from the user and:

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Counts how many words it has.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Prints the longest word in the sentence.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Prints the shortest word in the sentence.





# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # a = input().strip()


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(len(a))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # b = a.split()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # c = max(b , key=len)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # d = min(b , key=len)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(c)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(d)







# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Write a Python program that:

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Takes 5 numbers as input from the user (all in one line, separated by spaces).

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Stores them in a tuple.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Prints:

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # The maximum number

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # The minimum number

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # The sum of all numbers



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # z = input().split()  # takes input as strings

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # a = []  # empty list to store numbers

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # for i in z:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     a.append(int(i))  # convert each input to integer manually

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # b = tuple(a)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # total = 0
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # for i in a:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     total += i

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print("Sum:", total)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print("Max:", max(a))
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print("Min:", min(a))



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Write a Python program that does the following:

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Takes 5 numbers as input from the user (space-separated).

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Stores them in a list.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Then:

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Adds one more number (take it as input).

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Removes one number (take that number as input and remove it from the list).

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Sorts the list in ascending order.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Prints the final list.


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # z= input().strip()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # a = []

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # for i in z:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     a.append(z)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # b = input()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # c = a.append(b)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # d = input()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # e = a.pop(d)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # f = a.sort()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(a)







# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # i







# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # list 



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Question 9: Insert and Pop Practice

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Write a Python program that:

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Takes a list of 5 numbers (space-separated) as input.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Then:

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Ask the user which position (index) they want to insert a new number at, and the number to insert.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Ask the user for an index to remove (use pop() to remove that element).

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Finally, print the updated list.



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # a = []

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # for i in range(5):
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     b = input()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     a.append(b)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # w = input("where u wanna indecx:")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # c = input("what u wanna index")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # a.insert("w" , c )

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # d = input("index to remove")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # a.pop(d)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(a)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Write a program that:

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Takes 5 items (strings or numbers) as input from the user and stores them in a list.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Asks the user which index they want to replace and with what new value.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Then asks which value they want to remove from the list.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Finally, prints the updated list.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # a = []
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # for i in range(5):
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     b = input()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     a.append(i)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # b = input("which stuff u wanna edit")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # c = input("with what value")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # a.replace(b , c)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # d = input("u wanna remove")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # a.remove(d , a)









# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Takes 5 integer inputs from the user and stores them in a list.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Prints the list before sorting.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Sorts the list in ascending order and prints it.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Then reverses the list and prints the result again.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # a = []
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # for i in range(5):
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     b=input()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     a.append(b)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(a)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(a.short())

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(a.short(reverse=True))





# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Write a program that:

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Creates a list of 5 numbers (take input from the user).

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Makes one new list that is just an alias of the first list.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Makes another new list that is a copy of the first list.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Change one element in the original list.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Print all 3 lists and observe the difference.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # s =[]

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # for i in range(5):
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     b = int(input())
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     s.append(b)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # t = s.copy()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # s.pop() #chagning one element


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(s)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(t)



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Write a program to:

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Print the first and last element.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Replace the second element with 99.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Print the reversed list without using .reverse() method



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # a = str(input())

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # b=[]

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # for i in a:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     b.append(i)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(b[0] ,  b[-1])

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # c = b.replace( [1] ,  "99")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # d = [::-1]

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(d)



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Create a list of at least 7 items — can be numbers or strings.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Now write Python code to:

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Print a slice that gives the middle three elements.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Print the list in reverse using slicing (no loops).

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Print every second element from the list.





# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # a = []

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # for i in range (7):
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     b = input()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     a.append(b)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # c = len(a)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # if len(a) %2 ==0:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     print(a [c //2 + (c //2 +1) (c //2 + 2)])


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(a [::-1])

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(a[::2])



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Question 3 (Change — Modify Elements)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Create a list of 5 numbers.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Change the second element to 99.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Replace the last two elements with [77, 88].

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Finally, print the updated list.



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # a = []

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # for i in range(5):
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     b = input()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     a.append(b)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # a[1] = 99

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # a[-1] = 77

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # a[-2] = 88


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(a)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Create a list of 3 colors (for example: "red", "green", "blue").

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Add "yellow" to the end of the list.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Add "pink" at index 1 (between the first and second item).

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Add multiple colors ["black", "white"] at the end in one go.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Remove "green" from the list.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Pop (remove) the last element and print what was removed.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Finally, print the full list after all operations.


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # a = ["red" , "green" , "blue"]

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # a.append("yellow")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # a.insert[1 , "pink"]

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # a.insert[-1 , "black" , "white"]


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # a.remove("green")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # a.pop[-1]




# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(a)



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # You have a list of fruits:

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # fruits = ["apple", "banana", "cherry", "mango"]


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 👉 Task:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Write a for loop to print each fruit name on a new line.


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # for fruit in fruits:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     print(fruit)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # You have a list:

# # # # # # # # # # # # # # # # # # # # # # # # # # # # numbers = [3, 7, 2, 9, 5]


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # 👉 Task:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # Using a for loop, print only the even numbers from this list.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # (No list comprehension, just a basic loop and if statement.)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # for number in numbers:
# # # # # # # # # # # # # # # # # # # # # # # # # # # #     if number % 2 ==0:
# # # # # # # # # # # # # # # # # # # # # # # # # # # #         print(number)

# # # # # # # # # # # # # # # # # # # # # # # # # # # a = [4, 7, 2, 9, 5]

# # # # # # # # # # # # # # # # # # # # # # # # # # # sum = 0 
# # # # # # # # # # # # # # # # # # # # # # # # # # # for i in a:
# # # # # # # # # # # # # # # # # # # # # # # # # # #     sum +=i

# # # # # # # # # # # # # # # # # # # # # # # # # # # print(sum)


# # # # # # # # # # # # # # # # # # # # # # # # # a = [12, 45, 7, 89, 23, 89, 3]

# # # # # # # # # # # # # # # # # # # # # # # # # a.sort()

# # # # # # # # # # # # # # # # # # # # # # # # # print(a[-1])

# # # # # # # # # # # # # # # # # # # # # # # # # print(a.count[-1])

# # # # # # # # # # # # # # # # # # # # # # # # import math

# # # # # # # # # # # # # # # # # # # # # # # # def pascal_value(n, k):
# # # # # # # # # # # # # # # # # # # # # # # #     return math.comb(n, k)  # or: math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

# # # # # # # # # # # # # # # # # # # # # # # # # Example: Row 4

# # # # # # # # # # # # # # # # # # # # # # # # a = int(input())
# # # # # # # # # # # # # # # # # # # # # # # # for k in range(a):
# # # # # # # # # # # # # # # # # # # # # # # #     print(pascal_value(4, k), end=" ")



# # # # # # # # # # # # # # # # # # # # # # # # a = []
# # # # # # # # # # # # # # # # # # # # # # # # for i in range(3):
# # # # # # # # # # # # # # # # # # # # # # # #     b = int(input())
# # # # # # # # # # # # # # # # # # # # # # # #     a.append(b)

# # # # # # # # # # # # # # # # # # # # # # # # target = int(input())

# # # # # # # # # # # # # # # # # # # # # # # # for i in range(len(a)):
# # # # # # # # # # # # # # # # # # # # # # # #     for j in range(i+1 , len(a)):
# # # # # # # # # # # # # # # # # # # # # # # #         if a[i] + a[j] == target:
# # # # # # # # # # # # # # # # # # # # # # # #             print(a[i] , a[j])



# # # # # # # # # # # # # # # # # # # # # # # # a = int(input(""))
# # # # # # # # # # # # # # # # # # # # # # # # b = int(input(""))
# # # # # # # # # # # # # # # # # # # # # # # # flag = input("")

# # # # # # # # # # # # # # # # # # # # # # # # if (a > 0 or b > 0) and flag == "False":
# # # # # # # # # # # # # # # # # # # # # # # #     print("True")

# # # # # # # # # # # # # # # # # # # # # # # # elif (a < 0 and b < 0) and flag == "True":
# # # # # # # # # # # # # # # # # # # # # # # #     print("True")

# # # # # # # # # # # # # # # # # # # # # # # # else:
# # # # # # # # # # # # # # # # # # # # # # # #     print("False")



# # # # # # # # # # # # # # # # # # # # # # # Given a positive integer x. Your task is to check, if it is even or odd (Any number that gives zero
# # # # # # # # # # # # # # # # # # # # # # #  as remainder when divided by 2 is an even number).
# # # # # # # # # # # # # # # # # # # # # # # Note: Return "Even" if the number is even; otherwise, return "Odd".


# # # # # # # # # # # # # # # # # # # # # # a = [map(int, input().split())]

# # # # # # # # # # # # # # # # # # # # # # target = int(input())

# # # # # # # # # # # # # # # # # # # # # # for i in range(len(a)):
# # # # # # # # # # # # # # # # # # # # # #     for j in range(i+1 , len(a)):
# # # # # # # # # # # # # # # # # # # # # #         if a[i] + a[j] == target:
# # # # # # # # # # # # # # # # # # # # # #             print(a[i] , a[j])








# # # # # # # # # # # # # # # # # # # # # # Question 1: Python List Commands
# # # # # # # # # # # # # # # # # # # # # # You have an empty list.
# # # # # # # # # # # # # # # # # # # # # # You will receive N commands. Your task is to perform the commands on the list as described below:

# # # # # # # # # # # # # # # # # # # # # # Available commands:

# # # # # # # # # # # # # # # # # # # # # # insert i e : Insert integer e at position i

# # # # # # # # # # # # # # # # # # # # # # remove e : Delete the first occurrence of integer e

# # # # # # # # # # # # # # # # # # # # # # append e : Add integer e at the end of the list

# # # # # # # # # # # # # # # # # # # # # # sort : Sort the list

# # # # # # # # # # # # # # # # # # # # # # pop : Remove the last element

# # # # # # # # # # # # # # # # # # # # # # reverse : Reverse the list

# # # # # # # # # # # # # # # # # # # # # # print : Print the list

# # # # # # # # # # # # # # # # # # # # # a = list(map(int , input()))

 
# # # # # # # # # # # # # # # # # # # # Question 2: Nested Lists – Find Students with the Second Lowest Grade
# # # # # # # # # # # # # # # # # # # # You are given the names and grades for several students.
# # # # # # # # # # # # # # # # # # # # Your task is to find the name(s) of student(s) who have the second lowest grade in the class, and print them in alphabetical order.


# # # # # # # # # # # # # # # # # # # n = int(input())  
# # # # # # # # # # # # # # # # # # # a = []

# # # # # # # # # # # # # # # # # # # for _ in range(n):
# # # # # # # # # # # # # # # # # # #     name = input()
# # # # # # # # # # # # # # # # # # #     score = float(input())
# # # # # # # # # # # # # # # # # # #     a.append([name, score])


# # # # # # # # # # # # # # # # # # # for name, score in a:
# # # # # # # # # # # # # # # # # # #     prin


# # # # # # # # # # # # # # # # # # a = input("> ").strip()

# # # # # # # # # # # # # # # # # # if len(a) > 12:
# # # # # # # # # # # # # # # # # #     print("Invalid plese write less")


# # # # # # # # # # # # # # # # # # c = a.isdigit()

# # # # # # # # # # # # # # # # # # a.strip(c)

# # # # # # # # # # # # # # # # # # print(a)




# # # # # # # # # # # # # # # # # # import time 

# # # # # # # # # # # # # # # # # # b = int(input("> "))

# # # # # # # # # # # # # # # # # # for i in range( b,  -1 , -1):
# # # # # # # # # # # # # # # # # #     print(i)
# # # # # # # # # # # # # # # # # #     time.sleep(1)

# # # # # # # # # # # # # # # # # # print("jo hila vo gay ")

# # # # # # # # # # # # # # # # # a = int(input(">"))
# # # # # # # # # # # # # # # # # b = int(input("> col"))
# # # # # # # # # # # # # # # # # for x in range(a):
# # # # # # # # # # # # # # # # #     for y in range(b):
# # # # # # # # # # # # # # # # #         print( "*")
# # # # # # # # # # # # # # # # #         y+=1
# # # # # # # # # # # # # # # # #     print()




# # # # # # # # # # # # # # # # Task: Write a Python program to get a new string that is made of the first 2 

# # # # # # # # # # # # # # # # and the last 2 characters from a given string.

# # # # # # # # # # # # # # # # Rules:

# # # # # # # # # # # # # # # # If the string length is less than 2, the program should

# # # # # # # # # # # # # # # # return an empty string instead.

# # # # # # # # # # # # # # # a = input("> ").strip()

# # # # # # # # # # # # # # # if len(a) < 2:
# # # # # # # # # # # # # # #     print("")  
# # # # # # # # # # # # # # # else:
# # # # # # # # # # # # # # #     str = a[:2] + a[-2:]
# # # # # # # # # # # # # # #     print(str)

# # # # # # # # # # # # # # # 🧩 Problem 1 — First & Last
# # # # # # # # # # # # # # # Task:
# # # # # # # # # # # # # # # Given a non-empty string s, print the first and last characters concatenated together.
# # # # # # # # # # # # # # # Example:
# # # # # # # # # # # # # # # Input:  python
# # # # # # # # # # # # # # # Output: pn

# # # # # # # # # # # # # # # 🔹 Write your code below

# # # # # # # # # # # # # # s = input("Enter a string: ").strip()

# # # # # # # # # # # # # # a = s[0] + s[-1]

# # # # # # # # # # # # # # print(a)


# # # # # # # # # # # # # # 🧩 Problem 2 — Reverse It
# # # # # # # # # # # # # # Task:
# # # # # # # # # # # # # # Take a string s and print it reversed. 
# # # # # # # # # # # # # # (Use slicing, not loops)
# # # # # # # # # # # # # # Example:
# # # # # # # # # # # # # # Input:  hello
# # # # # # # # # # # # # # Output: olleh

# # # # # # # # # # # # # # 🔹 Write your code below

# # # # # # # # # # # # # s = input("Enter a string: ")


# # # # # # # # # # # # # 🧩 Problem 3 — Count Substring Occurrences
# # # # # # # # # # # # # Task:
# # # # # # # # # # # # # Given two strings (text and pattern), 
# # # # # # # # # # # # # print how many times 'pattern' occurs in 'text'.
# # # # # # # # # # # # # (Count overlapping occurrences too.)
# # # # # # # # # # # # #
# # # # # # # # # # # # # Example:
# # # # # # # # # # # # # Input:
# # # # # # # # # # # # # ABCDCDC
# # # # # # # # # # # # # CDC
# # # # # # # # # # # # # Output:
# # # # # # # # # # # # # 2
# # # # # # # # # # # # #
# # # # # # # # # # # # # 🔹 Hints:
# # # # # # # # # # # # # - You can use a loop with str.find(substring, start_index)
# # # # # # # # # # # # # - Or do it manually with slicing and indexing for logic practice.

# # # # # # # # # # # # # 🔹 Write your code below

# # # # # # # # # # # # # a = input("Enter the main text: ")
# # # # # # # # # # # # # b = input("Enter the pattern to search: ")

# # # # # # # # # # # # # c = len(a)

# # # # # # # # # # # # # d = len(b)

# # # # # # # # # # # # # for i in range 












# # # # # # # # # # # # # 🧩 Problem 4 — Split & Join
# # # # # # # # # # # # # Task:
# # # # # # # # # # # # # Given a sentence, split it on spaces and join it back using hyphens (-).

# # # # # # # # # # # # # Example:
# # # # # # # # # # # # # Input:  this is a string
# # # # # # # # # # # # # Output: this-is-a-string

# # # # # # # # # # # # # 🔹 Write your code below

# # # # # # # # # # # # s = input("Enter a sentence: ").strip()


# # # # # # # # # # # # print(s.replace(" " , "-" ))



# # # # # # # # # # # # 🧩 Problem 5 — Mutate a Character
# # # # # # # # # # # # Replace the character at index i in s with c.

# # # # # # # # # # # # Example:
# # # # # # # # # # # # Input:
# # # # # # # # # # # # abcde
# # # # # # # # # # # # 2
# # # # # # # # # # # # Z
# # # # # # # # # # # # Output:
# # # # # # # # # # # # abZde

# # # # # # # # # # # # 🔹 Write your code below

# # # # # # # # # # # s = input("Enter a string: ")
# # # # # # # # # # # i = int(input("Enter index to replace: "))
# # # # # # # # # # # c = input("Enter new character: ")

# # # # # # # # # # # print(s.replace(s[i] , c))


# # # # # # # # # # # 🧩 Problem 6 — Palindrome Checker
# # # # # # # # # # # Check if a string reads the same forward and backward (ignore spaces and case)

# # # # # # # # # # # s = input("Enter a string: ").strip()

# # # # # # # # # # # # Your logic here 👇


# # # # # # # # # # # c = s[::-1].strip()

# # # # # # # # # # # if c == s:
# # # # # # # # # # #     print("True") 

# # # # # # # # # # # else:
# # # # # # # # # # #    print("False")  




# # # # # # # # # # # 🧩 Problem 7 — Anagram Checker

# # # # # # # # # # # a = input("Enter first string: ").strip().lower().sort()
# # # # # # # # # # # b = input("Enter second string: ").strip().lower().sort()

# # # # # # # # # # # # Your logic here 👇


# # # # # # # # # # # if a == b:
# # # # # # # # # # #     print("true")

# # # # # # # # # # # else:
# # # # # # # # # # #     print("false")







# # # # # # # # # # # 🧩 Challenge: Mirror Words
# # # # # # # # # # # ------------------------------------
# # # # # # # # # # # Task:
# # # # # # # # # # #   Write a program that takes a sentence as input.
# # # # # # # # # # #   Reverse each word individually, but keep the order of words the same.
# # # # # # # # # # #
# # # # # # # # # # # Example:
# # # # # # # # # # #   Input:  I love Python
# # # # # # # # # # #   Output: I evol nohtyP
# # # # # # # # # # #

# # # # # # # # # # s = str(input("Enter a sentence: ")).strip().split()

# # # # # # # # # # c = list(s)


# # # # # # # # # # a = []

# # # # # # # # # # for i in c:
# # # # # # # # # #     b= i[::-1]
# # # # # # # # # #     a.append(b)


# # # # # # # # # # for i in a:
# # # # # # # # # #     print(i , end = " ")

# # # # # # # # # # print()

# # # # # # # # # # 🧩 Problem 1: List Basics — Sum of Elements
# # # # # # # # # # -------------------------------------------
# # # # # # # # # # Task:
# # # # # # # # # #   Write a program that takes space-separated integers as input,
# # # # # # # # # #   stores them in a list, and prints the sum of all elements.
# # # # # # # # # #
# # # # # # # # # # Example:
# # # # # # # # # #   Input:  2 4 6 8
# # # # # # # # # #   Output: 20
# # # # # # # # # #
# # # # # # # # # # Hints:
# # # # # # # # # #   - Use input().split() to take space-separated numbers.
# # # # # # # # # #   - Use map() or a loop to convert them to integers.
# # # # # # # # # # #   - Use sum() or a loop to find the total.

# # # # # # # # # # nums = input("Enter numbers separated by space: ").split()
# # # # # # # # # # a =[]

# # # # # # # # # # s = 0
# # # # # # # # # # for i in nums:
# # # # # # # # # #     a.append(int(i))


# # # # # # # # # # print(a)


# # # # # # # # # # for _ in a:
# # # # # # # # # #     s += _

# # # # # # # # # # print(s)
# # # # # # # # # # # Print the sum


# # # # # # # # # a = int(input(">"))

# # # # # # # # # for i in range(a  , -1 , -1):
# # # # # # # # #      print(i , end =" ")
     
# # # # # # # # # 🧩 Problem 4 — Reverse Digits of an Integer
# # # # # # # # # 🌐 Source: LeetCode (Reverse Integer problem)
# # # # # # # # # 🟠 Difficulty: Medium
# # # # # # # # #
# # # # # # # # # 👉 Task:
# # # # # # # # # Given an integer n (it can be positive or negative),
# # # # # # # # # reverse its digits and print the result.
# # # # # # # # #
# # # # # # # # # Examples:
# # # # # # # # # Input: 1234     → Output: 4321
# # # # # # # # # Input: -120     → Output: -21
# # # # # # # # #

# # # # # # # # # n = int(input(">"))

# # # # # # # # # m = 0

# # # # # # # # # while n > 0:
# # # # # # # # #     a = n % 10 

# # # # # # # # #     m = m * 10 + a

# # # # # # # # #     n = n // 10
    
# # # # # # # # # print(m)


# # # # # # # # # 🧩 Problem 5 — Remove Duplicates from Sorted List
# # # # # # # # # 🌐 Source: LeetCode (Remove Duplicates from Sorted Array)
# # # # # # # # # 🔵 Difficulty: Medium-Hard
# # # # # # # # #
# # # # # # # # # 👉 Task:
# # # # # # # # # Given a sorted list of integers, remove the duplicates **in-place**
# # # # # # # # # using a while loop (no built-in functions like set() or unique()).
# # # # # # # # # Finally, print the new length of the list and the elements up to that length.
# # # # # # # # #
# # # # # # # # # Example:
# # # # # # # # # Input:  1 1 2 2 3 4 4 5
# # # # # # # # # Output:
# # # # # # # # # New length: 5
# # # # # # # # # Modified list: 1 2 3 4 5

# # # # # # # # nums = list(map(int, input("Enter sorted numbers: ").split()))

# # # # # # # # a = []

# # # # # # # # for d in nums:
# # # # # # # #     if len(a) == 0 or d != a[-1]:
# # # # # # # #         a.append(d)

# # # # # # # # print( len(a))
# # # # # # # # print(a)

# # # # # # # # 🧠 Source: HackerRank
# # # # # # # # 💪 Difficulty: Easy
# # # # # # # # 🎯 Topic: Loops, Logic, Math

# # # # # # # # Q: Check whether a given number is a prime number or not.
# # # # # # # # A prime number is a number greater than 1 that has no divisors other than 1 and itself.

# # # # # # # # Input:
# # # # # # # #   A single integer n
# # # # # # # # Output:
# # # # # # # #   "Prime" if n is prime, otherwise "Not Prime"

# # # # # # # # Example:
# # # # # # # # Input: 7
# # # # # # # # Output: Prime


# # # # # # # # a = int(input(">"))

# # # # # # # # for i in range (2 , a):
# # # # # # # #     if a % i == 0:
# # # # # # # #         print("prime")
# # # # # # #         #   break
# # # # # # # # else:
# # # # # # # #     print('not prime')

# # # # # # # # 🔢 Print all prime numbers up to a given number n using a while loop.
# # # # # # # # Example:
# # # # # # # # Input: 10
# # # # # # # # Output: 2 3 5 7

# # # # # # # n = int(input("Enter the limit: "))

# # # # # # # for i in range(2 , n):
# # # # # # #     for j in range (2 , i):
# # # # # # #         if i % j ==0:
# # # # # # #             break
    
# # # # # # #     else:
# # # # # # #         print(i)


# # # # # # # 💡 Write a program to find the sum of digits of a number.
# # # # # # # Example:
# # # # # # # Input: 1234
# # # # # # # Output: 10  (1 + 2 + 3 + 4)

# # # # # # n = int(input("Enter a number: "))

# # # # # # sum =0

# # # # # # while n > 0:
# # # # # #     a = n % 10
# # # # # #     sum+=a
# # # # # #     n = n // 10

# # # # # # print(sum)

# # # # # # 🧩 Strong Number
# # # # # # A number is a Strong number if the sum of factorials of its digits equals the number itself.
# # # # # # Example: 145 -> 1! + 4! + 5! = 145  (Strong)
# # # # # #
# # # # # # Task:
# # # # # # Read an integer n from input and print "Strong" if it is a strong number, otherwise print "Not Strong".
# # # # # #
# # # # # # Examples:
# # # # # # Input: 145
# # # # # # Output: Strong
# # # # # #
# # # # # # Input: 123
# # # # # # Output: Not Strong

# # # # # n = int(input("Enter a number: "))

# # # # # x = n 



# # # # # sum = 0 
# # # # # while  n > 0:
# # # # #     a = n % 10
# # # # #     n = n // 10

# # # # #     fac = 1
# # # # #     for j in range(1 , a+1):
# # # # #         fac *= j
    
# # # # #     sum += fac

# # # # # if sum == x:
# # # # #     print('strong')


# # # # # else:
# # # # #     print('not')

# # # # # 🔢 Question: Sum of Digits of a Power
# # # # # Difficulty: Medium (based on HackerRank logic level)
# # # # # Topic: For loop + logic building

# # # # # Problem:
# # # # # Take two integers as input: a and b.
# # # # # 1. Compute a raised to the power of b (a ** b).
# # # # # 2. Find the sum of all digits in the result (without using sum()).
# # # # # 3. Print that sum.

# # # # # Example:
# # # # # Input:
# # # # # 2 10
# # # # #
# # # # # Output:
# # # # # 7
# # # # #
# # # # # Explanation:
# # # # # 2^10 = 1024 → 1 + 0 + 2 + 4 = 7

# # # # # 🧠 Write your code below 👇

# # # # # a, b = map(int, input("Enter two numbers (a and b): ").split())

# # # # # c = (a ** b)


# # # # # s = 0
# # # # # while c > 0:
# # # # #     x = c % 10
# # # # #     s += x
# # # # #     c //= 10


# # # # # print(s)


# # # # # 💡 Question: Digital Root Finder
# # # # # Difficulty: Medium
# # # # # Source: Inspired by HackerRank + Logical Thinking Drills
# # # # #
# # # # # Problem:
# # # # # The digital root of a number is obtained by repeatedly summing its digits
# # # # # until a single-digit number is left.
# # # # #
# # # # # Example:
# # # # # Input: 9875
# # # # # 9 + 8 + 7 + 5 = 29
# # # # # 2 + 9 = 11
# # # # # 1 + 1 = 2
# # # # #
# # # # # Output: 2
# # # # #
# # # # # Write a program to calculate the digital root of a number.

# # # # # n = int(input("Enter a number: "))


# # # # # while n > 10:
# # # # #     t = 0   
# # # # #     for i in str(n):
# # # # #         t += int(i)
# # # # #     n = t


# # # # # print(n)


# # # # # 💥 Question: Multiplicative Persistence
# # # # # Difficulty: Medium–Hard
# # # # # Source: Based on Project Euler & HackerRank-style logic
# # # # #
# # # # # Problem:
# # # # # The multiplicative persistence of a number is the number of times
# # # # # you must multiply its digits until you reach a single-digit number.
# # # # #
# # # # # Example:
# # # # # Input: 39
# # # # # Process:
# # # # #   3 * 9 = 27
# # # # #   2 * 7 = 14
# # # # #   1 * 4 = 4
# # # # # Output: 3   ← (because it took 3 steps to reach a single digit)
# # # # #
# # # # # Another Example:
# # # # # Input: 999
# # # # # Process:
# # # # #   9 * 9 * 9 = 729
# # # # #   7 * 2 * 9 = 126
# # # # #   1 * 2 * 6 = 12
# # # # #   1 * 2 = 2
# # # # # Output: 4
# # # # #
# # # # # Write a program that prints how many steps it takes.

# # # # # n = int(input("Enter a number: "))

# # # # # a= 0 
# # # # # while n > 10:
# # # # #     a += 1
# # # # #     t = 1
# # # # #     for i in str(n):
# # # # #         t *= int(i)
        
# # # # #     n = t
    

# # # # # print(a)

# # # # #Q-1
# # # # # ⚡ Question: Dual Persistence Tracker  
# # # # # Difficulty: Medium  
# # # # # Concept: Digit sum and multiplication logic
# # # # #
# # # # # Problem:
# # # # # You are given a number 'n'.
# # # # # 1️⃣ Keep summing its digits until you reach a single-digit number.
# # # # #     Count how many times this happens.
# # # # # 2️⃣ Keep multiplying its digits until you reach a single-digit number.
# # # # #     Count how many times this happens.
# # # # #
# # # # # Print both counts as:
# # # # # Sum steps: X
# # # # # Product steps: Y
# # # # #
# # # # # Example:
# # # # # Input: 999
# # # # # Process (Sum):
# # # # #   9+9+9 = 27
# # # # #   2+7 = 9 → (2 steps)
# # # # #
# # # # # Process (Product):
# # # # #   9*9*9 = 729
# # # # #   7*2*9 = 126
# # # # #   1*2*6 = 12
# # # # #   1*2 = 2 → (4 steps)
# # # # #
# # # # # Output:
# # # # # Sum steps: 2
# # # # # Product steps: 4

# # # # # n= int(input("Enter a number: "))

# # # # # b = n

# # # # # s = 0
# # # # # while n >=10:
# # # # #     s += 1
# # # # #     summ = 0
# # # # #     for i in str(n):
# # # # #         summ += int(i)
# # # # #     n = summ

# # # # # print(s)
# # # # # m = 0 

# # # # # while b >= 10:
# # # # #     m +=1
# # # # #     mum = 1
# # # # #     for i in str(b):
# # # # #         mum *= int(i)
        
# # # # #     b = mum

# # # # # print(m)

# # # # # 🔢 Question 3: Alternating Digit Operations  
# # # # # Difficulty: Medium–Hard  
# # # # # Concept: Math logic, loop control, digit manipulation  
# # # # #
# # # # # Problem:
# # # # # Given a number 'n', perform these alternating steps until it becomes a single digit:
# # # # #   Step 1 → Replace it with the *sum* of its digits.  
# # # # #   Step 2 → Replace it with the *product* of its digits.  
# # # # #   Step 3 → Again the *sum*, then *product*, and so on...
# # # # #
# # # # # Count how many total steps it takes to reach a single digit.
# # # # #
# # # # # Example:
# # # # # Input: 59
# # # # # Process:
# # # # #   5 + 9 = 14   (sum)
# # # # #   1 * 4 = 4    (product)
# # # # # Output: 2
# # # # #
# # # # # Input: 678
# # # # # Process:
# # # # #   6 + 7 + 8 = 21
# # # # #   2 * 1 = 2
# # # # # Output: 2

# # # # # n = int(input("Enter a number: "))

# # # # # y = 0

# # # # # while n >= 10:

# # # # #     y += 1
# # # # #     a = 0
# # # # #     for i in str(n):
# # # # #         a += int(i)
        


# # # # #     if  a>= 10:
# # # # #         b= 1
# # # # #         y += 1
# # # # #         for j in str(a):
# # # # #             b *= int(j)
# # # # #         n = b
# # # # #     else:
# # # # #         n = a
            
# # # # # print(y)

# # # # import time
# # # # def countdown(n):
# # # #     if n == 0:      # base case
# # # #         print("Done!")
# # # #         return

# # # #     print(n)
# # # #     time.sleep(1)
# # # #     countdown(n - 1)   # recursive call

# # # # countdown(5)

# # # # import os
# # # # os.system('spd-say "Time up"')


# # # import time

# # # # pomodoro_step = int(input("How many pomodoro you want dude ? : "))
# # # # ptrue = 0     

# # # # while ptrue <= pomodoro_step:
# # # #         for x in range (1500 , 0 , -1):
# # # #            second = int(x % 60)
# # # #            minute = int(x / 60) % 60 
# # # #            print(f"{minute}:{second}:00")
# # # #            time.sleep(1)


# # # # def pomodoro():
# # # #      import time
# # # #      pomodoro_step = int(input("How many pomodoro you want dude ? : "))

# # # #      ptrue = 0     
# # # #      while ptrue < pomodoro_step:
# # # #         ptrue += 1
# # # #         for x in range (10 , 0 , -1):
# # # #             second = x % 60
# # # #             minute = int(x / 60) % 60 
# # # #             print(f"{minute}:{second}:00")
# # # #             time.sleep(1)


        
# # # #         print("your breaks start now ")
# # # #         print()

# # # #         import os
# # # #         os.system('spd-say "your break starts now enjoy buddy"')

# # # #         for y in range (3 , 0, -1 ):
# # # #             secondd = y % 60
# # # #             minutee = int(y / 60) % 60
# # # #             print(f"{minutee}:{secondd}:00")
# # # #             time.sleep(1)
            
# # # #         print("Time's up")
# # # #         print()


# # # #         import os
# # # #         os.system('spd-say "get to work"')
        

# # # # pomodoro()

# # # #  for gpa 

# # # # Your program will:

# # # # Ask how many subjects

# # # # Ask the grade (A/B/C/D/F) or marks for each subject

# # # # Convert each grade → points

# # # # Add all points

# # # # Divide by number of subjects

# # # # Show the final GPA

# # # # def gpa():
# # # #     subjectlist = {}
# # # #     gpa_input = int(input(" how many subjets you to enter:   "))
# # # #     print()

# # # #     for i in range (gpa_input):
# # # #         key = input(f"name of the subjet {i + 1}:         ")
# # # #         value = input(f"score of the subject{key}:        ")
# # # #         print()

# # # #         subjectlist[key] = value

# # # #     vd = subjectlist.values()
# # # #     total_score = 0

# # # #     for val in vd:
# # # #         total_score += int(val)

# # # #     print(f"total score of your subjet is = {total_score}" )
# # # #     print()

# # # #     print(f"your GPA IS = {total_score / gpa_input} %")
# # # #     print()
    

# # # # gpa()



# # # #  qutoes


# # # # def random_motiv():
# # # #     import random
# # # #     quotes = [
# # # #     "Small steps every day lead to big results.",
# # # #     "Discipline will take you places motivation can't.",
# # # #     "If you get tired, learn to rest - not to quit.",
# # # #     "Your only limit is your mind.",
# # # #     "Do it for the future you.",
# # # #     "Success is built on consistency, not intensity.",
# # # #     "One hour of focus can change your whole day.",
# # # #     "Don't wait for the perfect moment - start now.",
# # # #     "The only bad study session is the one you didn't do.",
# # # #     "You're closer than you think. Keep going."
# # # # ]


# # # #     quote = random.choice(quotes)

# # # #     print()

# # # #     print(f"Bro ,{quote}")

# # # #     print()

# # # #  
# # # #  
# # # # -------------------Enter your notes------------------

# # # def calculator():
# # #     print()
# # #     import math
# # #     while True:
# # #             solve = input("Type + , - , * , %  for doing the basic calculations type s , c , t for finding sin , cos , tan " \
# # #         " when you done press q to exit : ").lower()
# # #             print()

# # #             if solve == "q":
# # #                 break
# # #             num1 = int(input("enter 1st number: "))
# # #             print()
# # #             num2 = int(input ("enter 2nd number: "))
# # #             print()
# # #             print()

# # #             if solve == "q":
# # #                 cal_true = 10
        
# # #             elif solve == "-":
# # #                 print(num1 - num2)
# # #                 print()
# # #                 print()
# # #             elif solve == "+":
# # #                 print(num1 + num2)
# # #                 print()
# # #                 print()

# # #             elif solve =="*":
# # #                 print(num1 * num2)
# # #                 print()
# # #                 print()
# # #             elif solve =="%":
# # #                 print(num1 / num2)
# # #                 print()
# # #                 print()

# # #             elif solve =="s":
# # #                 print(math.sin(num1))
# # #                 print(math.sin(num2))
# # #                 print()
# # #                 print()
                
# # #             elif solve =="c":
# # #                 print(math.cos(num1))
# # #                 print(math.cos(num2))
# # #                 print()
# # #                 print()
# # #             elif solve =="t":
# # #                 print(math.tan(num1))
# # #                 print(math.tan(num2))
# # #                 print()
# # #                 print()
# # #             else:
# # #                 print("cant be done dude get help: ")
            
# # # calculator()
    

# # def to_do_list():
# #     print()
# #     print("------------------- welcome to  your do to list ------------------")
# #     print()
# #     menu = (""" 
            
# #                 1. Add task
# #                 2. View tasks
# #                 3. Remove task
# #                 4. Back to main menu """)
# #     print(menu)
# #     print()
# #     print()
# #     tasks = []
# #     print()

# #     while True:

# #         task_input = int(input(">>> what you wanna do right now , type one of those number given  : "))
# #         print()
# #         if task_input == 1:
# #             truee = True
# #             while truee:
# #                 add_task = input("     Write your tasks when done press exit to exit: ")

# #                 print()


# #                 if add_task == "exit":
# #                     truee = False
# #                 else:
# #                     tasks.append(add_task)

# #             print(f"Your task are {tasks}")
# #             print()
        
# #         elif task_input == 2:
# #             x = 1
# #             print("Your task are: ")
# #             print()
# #             for task in  tasks:
# #                 print(f"{x}:     {task}")
# #                 x += 1
        
# #         elif task_input ==3:
# #             x = 1
# #             for task in  tasks:
# #                 print(f"{x}:     {task}")
# #                 x += 1
            
# #             print()
# #             print()
# #             while True:
# #                remove_task = input("   enter the task number you want to remove , press q to exit: ")
# #                print()
# #                if remove_task == "q":
# #                    break
# #                else:
# #                 c = int(remove_task)
# #                 b = tasks[c - 1]
# #                 print(b)
# #                 tasks.remove(b)
# #                 print(f"Your task are {tasks}")
# #                 print()

# #         elif task_input == 4:
# #             break

# # to_do_list()
# # input = [
# #     (385350926, 385403705),(48047, 60838),(6328350434, 6328506208),(638913, 698668),
# #     (850292, 870981),(656, 1074),(742552, 796850),(4457, 6851),(138, 206),
# #     (4644076, 4851885),(3298025, 3353031),(8594410816, 8594543341),(396, 498),
# #     (1558, 2274),(888446, 916096),(12101205, 12154422),(2323146444, 2323289192),
# #     (37, 57),(101, 137),(46550018, 46679958),(79, 96),(317592, 341913),
# #     (495310, 629360),(33246, 46690),(14711, 22848),(1, 17),(2850, 4167),
# #     (3723700171, 3723785996),(190169, 242137),(272559, 298768),(275, 365),
# #     (7697, 11193),(61, 78),(75373, 110112),(425397, 451337),(9796507, 9899607),
# #     (991845, 1013464),(77531934, 77616074)
# # ]

# # list1 = []

# # for i, j in input:
# #     for k in range(i, j + 1):
# #         s = str(k)
# #         for l in range(1, len(s) // 2 + 1):
# #             if len(s) % l == 0:
# #                 if s[:l] * (len(s) // l) == s:
# #                     list1.append(k)
# #                     break

# # print(sum(list1))   

# import string

# a = string.ascii_uppercase
# dict1 = {}
# for i in range(1 , 27):
#     dict1.keys


import math
a = float(input())

b = math.radians(a)

c = round(b, 2)

d = math.sin(c)

print(round(d, 2))