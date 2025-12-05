import random 

c  , y = 0 , 0 

while True:

    you = input("choose r p or s press q to quit : ")

    choic = ("r" , "p" ,  "s")

    compt = random.choice(choic)


    print(f"you choose '{you}' \nand computer choose '{compt}'")


    if you == "q":
        print("thaank you for playing you scores are BELOW  : ")
        break

    elif you not in choic:
        print("invalid response ")


    elif you == compt:
        print("draw")

    elif you == "r" and  compt == "s":
        print("you won")
        y += 1

    elif you  == "r" and compt == "p":
        print("l bozo")
        c += 1

    elif you == "p" and compt == "r":
        print("w")
        y += 1

    elif you == "p" and compt == "s":
        print("l")
        c += 1

    elif you == "s" and compt == "r":
        print("l")
        y += 1
    
    elif you == "s" and compt == "p":
        print("l")


print ()

print ()
print ()

print(f"you won {y} time" )

print(f"compt won {c} times")

