import random

print()

print("welcome dude wanna play a guessing game? , gimme two num i will choose one num btw them  ")

print()

x = int(input("num1> "))

y = int(input("num2> "))

guess = random.randint(x , y)

step  = 0 

print("okay guess the num ")

while True:

    a = int(input(">"))

    step += 1
    if a > guess:
        print("too high")
    
    elif a < guess:
        print("too low baby")

    else:
        print(f"congo bitch you guessed the num {guess} in {step} steps")
        
        break
