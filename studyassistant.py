print('''Welcome to the Study Assistant 
Choose a tool:  
1. Flashcard Quiz  
2. Pomodoro Timer  
3. Calculator 
4. GPA Calculator  
5. Random Motivator  
6. to do list
7. Exit
8. to see the tool again'''
)
print()
ten = 10
tasks = []



def flashcard():
        
        temp_num = 0
        temp_numm = 0
        score = 0
        print("-------------------------------FLASHCARD QUIZ-------------------------------")
        print()

        print("here are some flashcard quiz for you bro try out dont cheat")
        print()

        print("---------------quiz---------------")
        print()
        questions = [
        "What is the capital of France?",
        "Which data type is immutable in Python?",
        "What does CPU stand for?",
        "Which planet is known as the Red Planet?",
        "What is the output of 3 * 2 ** 2 in Python?",
        "Which keyword is used to define a function in Python?",
        "What does RAM stand for?"
    ]
        
        options = [
        ["A) Berlin", "B) Paris", "C) Madrid", "D) Rome"],
        ["A) List", "B) Set", "C) Tuple", "D) Dictionary"],
        ["A) Central Process Unit", "B) Central Processing Unit", "C) Computer Personal Unit", "D) Control Processing Unit"],
        ["A) Venus", "B) Saturn", "C) Mars", "D) Jupiter"],
        ["A) 12", "B) 18", "C) 6", "D) 3"],
        ["A) func", "B) define", "C) def", "D) fn"],
        ["A) Readable Access Memory", "B) Random Access Memory", "C) Real-time Allocation Module", "D) Rapid Access Module"]
    ]



        answers = ['B' , 'C' , 'B' , 'C' , 'A' , 'C' , 'B']

        for question in questions:
            print("-----------------------------------------")
            print(question)
            for option in options[temp_num]:
                print(option)
            temp_num += 1

            for answer in answers[temp_numm]:
                print("--------------------------")
                correct_answer = answers[temp_numm]

                answer_ofuser = (input("enter a option : ")).upper()

                if correct_answer == answer_ofuser:
                    print("good boy")
                    print()
                    score += 1
                else:
                    print(f"pur bitch answer is {answer}")
                temp_numm += 1

        if score >= 4:
            print(f"you scored {score} out of 7 Good its above avergae")
            print()
        
        else:
            print(f"you scored {score} out of 7 ")
            print()
            print("try hard next time ")
            print()


def pomodoro():
     print("----------------------------------welcome to Pomodoro Technique--------------------------------")

     print()

     print("The Pomodoro Technique is a time management method developed by Francesco Cirillo in the late 1980s.It uses a kitchen timer to break work into intervals, typically 25 minutes in length, separated by short breaks. Each interval is known as a pomodoro, from the Italian word for tomato, after the tomato-shaped kitchen timer that Cirillo used while he was a university student ")

     print()
     import time
     pomodoro_step = int(input("How many pomodoro you want ? each pomodor is of 25 mintues with 5 min break : "))

     ptrue = 0     
     while ptrue < pomodoro_step:
        print("Your work time starts now")
        print()
        ptrue += 1
        for x in range (10 , 0 , -1):
            second = x % 60
            minute = x // 60 
            print(f"{minute}  mintues : {second}  seconds ")
            time.sleep(1)



        
        print("your breaks start now come back after 5 min ")
        print()

        import os
        os.system('spd-say "your break starts"')

        for y in range (3, 0, -1 ):
            secondd = y % 60
            minutee = y // 60
        
            print(f"{minutee}:{secondd}:00")
            time.sleep(1)
            
        print("Time's up")
        print()


        import os
        os.system('spd-say "get to work"')
\

def gpa():
    print("------------Welcome to GPA calculator----------------")

    subjectlist = {}
    gpa_input = int(input(" how many subjets you have:   "))
    print()

    for i in range (gpa_input):
        key = input(f"name of the subject   {i + 1}    :         ")
        value = input(f"score of the subject  {key} :        ")
        print()

        subjectlist[key] = value

    vd = subjectlist.values()
    total_score = 0

    for val in vd:
        total_score += int(val)

    print(f"total score of your subjet is = {total_score}" )
    print()

    print(f"your GPA IS = {total_score / gpa_input} %")
    print()
    

def random_motiv():
    print("-----winners dont need motivation----- but you take one anyway--------")

    print()
    import random
    quotes = [
    "Small steps every day lead to big results.",
    "Discipline will take you places motivation can't.",
    "If you get tired, learn to rest - not to quit.",
    "Your only limit is your mind.",
    "Do it for the future you.",
    "Success is built on consistency, not intensity.",
    "One hour of focus can change your whole day.",
    "Don't wait for the perfect moment - start now.",
    "The only bad study session is the one you didn't do.",
    "You're closer than you think. Keep going."
]

    
    quote = random.choice(quotes)
    print()
    print(f"Bro ,{quote}")
    print()

def calculator():
    print("------------Welcome to calculator----------------")
    print()
    import math
    while True:
        solve = input("Type + , - , * , /  for doing the basic calculations type s , c , t for finding sin , cos , tan " \
        " when you done press q to exit : ").lower()
        print()

        if solve == "q":
            break
        num1 = int(input("enter 1st number: "))
        print()
        num2 = int(input ("enter 2nd number: "))
        print()
        print()

        if solve == "q":
            cal_true = 10
    
        elif solve == "-":
            print(num1 - num2)
            print()
            print()
        elif solve == "+":
            print(num1 + num2)
            print()
            print()

        elif solve =="*":
            print(num1 * num2)
            print()
            print()
        elif solve =="/":
            print(num1 / num2)
            print()
            print()

        elif solve =="s":
            print(math.sin(num1))
            print(math.sin(num2))
            print()
            print()
            
        elif solve =="c":
            print(math.cos(num1))
            print(math.cos(num2))
            print()
            print()
        elif solve =="t":
            print(math.tan(num1))
            print(math.tan(num2))
            print()
            print()
        else:
            print("cant be done dude get help: ")


def to_do_list():
    print()
    print("------------------- welcome to  your do to list ------------------")
    print()
    menu = (""" 
            
                1. Add task
                2. View tasks
                3. Remove task
                4. Back to main menu """)
    print(menu)
    print()
    print()
    print()

    while True:
        task_input = int(input(">>> what you wanna do : "))
        print()
        if task_input == 1:
            truee = True
            while truee:
                add_task = input("     Write your tasks when done press exit to exit: ")

                print()


                if add_task == "exit":
                    truee = False
                else:
                    tasks.append(add_task)

            print(f"Your task are {tasks}")
            print()
        
        elif task_input == 2:
            x = 1
            print("Your task are: ")
            print()
            for task in  tasks:
                print(f"{x}:     {task}")
                print()
                x += 1
        
        elif task_input ==3:
            x = 1
            for task in  tasks:
                print(f"{x}:     {task}")
                x += 1
            
            print()
            print()
            while True:
               remove_task = input("   enter the task number you want to remove , press q to exit: ")
               print()
               if remove_task == "q":
                   break
               else:
                c = int(remove_task)
                b = tasks[c - 1]
                print(f"the task removed was {b}")
                print()
                tasks.remove(b)
                print(f"Your new task are {tasks}")
                print()

        elif task_input == 4:
            break

while ten == 10:
    user_input = int(input("enter tool number : "))

    print()

    if user_input ==   1:
        flashcard()
    elif user_input == 2:
        pomodoro()
    elif user_input == 3:
        calculator()
    
    elif user_input == 4:
        gpa()
    
    elif user_input == 5:
        random_motiv()
    
    elif user_input ==6:
        to_do_list()
    
    elif user_input ==7:
        ten = 11
    elif user_input ==8:
        print('''Welcome to the Study Assistant 
        Choose a tool:  
        1. Flashcard Quiz  
        2. Pomodoro Timer  
        3. Calculator 
        4. GPA Calculator  
        5. Random Motivator  
        6. to do list
        7. Exit
        8. to see the tool again''')



print("------------Thank you for using this assitant----------------")

