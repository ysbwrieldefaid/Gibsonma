import os
import time
import random
points = 0
continue_playing = True
credits = 5

def initialise():
    answer = False
    suitable_answer = False
    choice = "no"
    while suitable_answer is False:  
        choice = input("""
 ___________________________________________________________________
|                                                                   |
| W E L C O M E  T O  M A T T ' $  M A G N I F I C E N T  $ L O T $ |
|                                                                   |
| T H E R E ' S  N O  W H E R E  E L S E  B E T T E R  T O  B E !   |
|                                                                   |
| I F  Y O U  A R E  R E A D Y  P L E A S E  T Y P E  ' y e s '     |
|___________________________________________________________________|

           """"")
        if choice.isdigit():
            print()
            print("Please write yes or no. \n")
            print()
            suitable_answer = False
        else:
            suitable_answer = True
    choice = choice.lower().strip()
    if choice == "yes":
        answer = True
    else:
        answer = False
    return answer


def rolling():
    displayed_roll = ["+", "x"]
    for m in range(0, 5):
        for i in range(0, 2):
            os.system('cls')
            print(displayed_roll[i], " ", displayed_roll[i], " ", displayed_roll[i])
            print("Rolling")
            time.sleep(0.2)


def selecting_fruit(fruit_choice):
    return random.choice(fruit_choice)


def main_game():
    continue_playing_check = True
    global credits  
    global points   
    print("\nWelcome to Slots! \n")
    time.sleep(1)
    print("You start with the five credits you inserted. This value changes based of how many times you continue playing. \n")
    time.sleep(1)
    print("Every time you roll you use up one of your credits \n")
    time.sleep(1)
    print("If you have no credits left the game is Over! \n")
    time.sleep(1)
    print("Depending on what you roll, you may earn more credits and points. \n")
    time.sleep(1)
    print("As long as you have credits remaining, you may continue to roll and gain points! \n")
    time.sleep(1)
    print("You are also able to trade 100 points for one credit. \n")
    time.sleep(1)
    print("you have %s remaining credits! and %s points.\n" % (credits, points))
    time.sleep(1)
    print("Use them wisely! Good luck! \n")
    time.sleep(1)
    currently_playing = True
    while currently_playing is True and credits != 0:  
        use_credit = input("Do you want to use a credit? yes or no? \n")
        print("\n")
        use_credit = use_credit.lower().strip()
        if use_credit == "yes":
            rolling()
            os.system('cls')
            credits = credits - 1
            fruit_choice = ["#", "%", "?", "£"]
            first_slot = selecting_fruit(fruit_choice)
            second_slot = selecting_fruit(fruit_choice)
            third_slot = selecting_fruit(fruit_choice)
            print("$ L O T $ \n")
            print(first_slot," ",second_slot," ",third_slot)
            print("\n$ L O T $\n")
            currently_playing = True
            if first_slot == second_slot and third_slot == first_slot:
                points = points + 500
                credits = credits + 1
                print("Woah you got three in a row! \n")
                print("You get one extra credit for that! \n")
                print("Three in a row gives you 500 points! \n")
                print("You currently have", points, "points and", credits, "credits! \n")
            elif first_slot == second_slot or second_slot == third_slot:
                points = points + 200
                print("Nice one you managed to roll two in a row! \n")
                print("Two in a row gives you 200 points! \n")
                print("You currently have", points, "points and", credits, "credits! \n")
            elif first_slot != second_slot and second_slot != third_slot:
                points = points - 50
                if points < 0:
                    points = 0
                print("Boring! You got nothing! \n")
                print("You lose 50 points \n")
                print("You currently have", points, "points and", credits, "credits! \n")
        else:
            currently_playing = False
    time.sleep(3)
    print("\n")   
    os.system('cls')
    print("Thanks for playing! You ended with", points, "points and", credits, "credits left!")

    if -1 < points < 10:
        print("""
 ___________________
 |  _____________  |
 | |             | |
 | |  0 points   | |
 | |             | |
 | |             | |
 | |_____________| |
 |_________________|
     _[_______]_
 ___[___________]___
|         [_____] []|
|         [_____] []|
L___________________J

    """)

    elif points == 50:
        print("""
 ___________________
 |  _____________  |
 | |             | |
 | |  50 points  | |
 | |             | |
 | |             | |
 | |_____________| |
 |_________________|
     _[_______]_
 ___[___________]___
|         [_____] []|
|         [_____] []|
L___________________J

    """)

    elif 99 < points < 1000:
        print("""
 ___________________
 |  _____________  |
 | |             | |
 | |""", points, """points  | |
 | |             | |
 | |             | |
 | |_____________| |
 |_________________|
     _[_______]_
 ___[___________]___
|         [_____] []|
|         [_____] []|
L___________________J

    """)

    elif 999 < points < 10000:
        print("""
 ___________________
 |  _____________  |
 | |             | |
 | |""", points, """points | |
 | |             | |
 | |             | |
 | |_____________| |
 |_________________|
     _[_______]_
 ___[___________]___
|         [_____] []|
|         [_____] []|
L___________________J

    """)
    if points > 99:
        withdrawal_credits = ""
        points_exchange = input("Do you want to exchange points for credits to continue playing? \n")
        if points_exchange.lower().strip() == "yes":
            time.sleep(1)
            print("\nRemember trading in 100 points gives you 1 credit! \n")
            time.sleep(1)
            print("You have", points, "points. \n")
            credits_added = input("Do you want to exchange points for credits? \n\n")
            if credits_added.lower().strip() == "yes":
                points_division = int(points / 100)
                points = points - (100 * int(points / 100))
                credits = credits + points_division
                print("you now have", credits, "credits. \n")
                withdrawal_credits = input("Would you like to withdrawal these credits? \n")
        else:
            print("No worries. Thanks for playing.\n")
            continue_playing_check = False
        if withdrawal_credits.lower().strip() == "yes":
            os.system('cls')
            print("D I S P E N S I N G  C R E D I T S \n")
            time.sleep(1)
            os.system('cls')
            print("\nD I S P E N S I N G  C R E D I T S \n")
            time.sleep(1)
            os.system('cls')
            print("\n\nD I S P E N S I N G  C R E D I T S \n")
            time.sleep(1)
            os.system('cls')
            print("Your", credits, "credits have been dispensed. Enjoy! \n")
            time.sleep(3)
            quit()
        if withdrawal_credits.lower().strip() != "yes":
            continue_playing = True 
        if continue_playing_check == False:
            continue_playing = False
    else:
        time.sleep(1)
        print("Oh no! You do not have enough points to trade for credits!")
        time.sleep(5)
        continue_playing = False
    return continue_playing


while continue_playing is True:
    if initialise() is True:
        continue_playing = main_game()

    else:
        continue_playing = False

if credits != 0:
    points_division = int(points / 100)
    points = points - (100 * int(points / 100))
    credits = credits + points_division
    os.system('cls')
    time.sleep(1)
    print("D I S P E N S I N G  C R E D I T S \n")
    time.sleep(1)
    os.system('cls')
    print("\nD I S P E N S I N G  C R E D I T S \n")
    time.sleep(1)
    os.system('cls')
    print("\n\nD I S P E N S I N G  C R E D I T S \n")
    time.sleep(1)
    os.system('cls')
    print("\n\n\nD I S P E N S I N G  C R E D I T S \n")
    os.system('cls')
    time.sleep(1)
    print("Your", credits, "credits have been dispensed. Come back soon! \n")
    time.sleep(200)

if credits == 0:
    print("\nOh no, you lost all your credits. Thanks for playing! \n")
    time.sleep(1)
    print("Goodbye!")
    time.sleep(1)
    quit()
