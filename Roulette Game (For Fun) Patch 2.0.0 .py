import sys, time, os, random
number_multiplier = 3
colour_multiplier = 2
users_money = 1000
def print1by1(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)

def rules():
    global users_money
    print("Welcome to Roulette! You have",users_money,"dollars to spend!") 
    time.sleep(1)
    print1by1("These are the Rules: \n")#
    time.sleep(1)
    print1by1("Using your chips, you can place bets on whether you think what's rolled will be even or odd \n")
    time.sleep(1)
    print1by1("You can bet on whether what rolled is black or red, or if you are feeling lucky green \n")
    time.sleep(1)
    print1by1("You can also bet on whether a specific number will be rolled \n")
    time.sleep(1)
    print1by1("Based on the odds of rolling, your money either doubles/triples... \n")
    time.sleep(5)

def spinning():
    displayed_spin = ["o", "O",]
    for m in range(0, 5):
        for i in range(0, 2):
            os.system('cls')
            print(displayed_spin[i], " ", displayed_spin[i], " ", displayed_spin[i])
            print("Spinning")
            time.sleep(0.5)

def main_game():
    global users_money 
    global currently_playing
    print1by1("So... are you ready to play Roulette?! \n")
    play_game = input("Please Type Yes or No \n")
    if play_game.lower().strip() == "yes":
        lets_play = True 
        print("\nOkay lets play! \n")
        name_check = False
        while name_check == False:
            name = input("What is your name? ")
            if name.isalpha():
                name_check = True
            else:
                name_check = False
                os.system('cls')
        print("\nHello",name,"Welcome to Roulette!")
        print1by1("\nI'll be your host, Matt!")            
    else:
        lets_play = False
        print1by1("No worries. Thank you for coming!")
        print1by1("\nPlease come back soon!")
        time.sleep(2)
        quit

    if lets_play == True:
        secret_spin_choice = random.randint(0,36)
        secret_colour_choice = random.randint(0,36)
        secret_colour = " "
        if int(secret_colour_choice) == 0:
            secret_colour = "green"
        elif int(secret_colour_choice) != 0 and float(secret_colour_choice) % 2 == 0:
            secret_colour = "red"
        elif int(secret_colour_choice) != 0 and float(secret_colour_choice) % 2 != 0:
            secret_colour = "black"
        print1by1("\nWhat do you want to bet on?")
        print1by1("\nFor simplicity- Even numbers are red, odd numbers are black and zero is of course green.")
        time.sleep(1)
        print1by1("\nOptions include: 'number' , 'colour' , 'odd' or 'even'")
        user_choice = input("\nPlease choose: ")
        if user_choice.lower().strip() == "number":
            print("\nI see you want to choose a number...")
            users_gamble_valid = False
            while users_gamble_valid == False:
                users_gamble = input("\nPlease choose a number between 0-36, including 0 and 36 if needs be.")
                if int(users_gamble) > -1 and int(users_gamble) < 37:
                    users_gamble_valid = True
                else:
                    os.system('cls')
                    print("Please input a number in the given range.")
                    users_gamble_valid = False
            print("\nYou have chosen number",users_gamble,)
            print("Now it is time to bet!")
            users_bet_valid = False
            while users_bet_valid == False:
                users_bet = input("How much money do you want to bet? ")
                if int(users_bet) < int(users_money):
                    print("/nPlease bet a suitable amount!")
                    users_bet_valid = False
                else:
                    users_bet_valid = True
            print1by1("Time to spin!")
            time.sleep(1)
            spinning()
            print("\nYou span",secret_spin_choice)
            print("\nYou chose",users_gamble)
            if int(secret_spin_choice) == int(users_gamble):
                print1by1("\nNo Way! You got it!")
                users_money = (users_money - users_bet) + (users_bet * number_multiplier)
                print1by1("\nYou win:",(int(users_bet)*(number_multitplier)),)
                print1by1("\nNew Balance",users_money,)
                currently_playing_answer = input("\nPlay again? please type y or n ")
                if currently_playing_answer.lower().strip() == "y":
                    currently_playing = True 
            else:
                print("\nNice Try!")
                users_money = users_money - users_bet
                print1by1("\nNew Balance",users_money,)
                currently_playing_answer = input("Play again? Please type y or n ")
                if currently_playing_answer.lower().strip() == "n":
                    currently_playing = False
        if user_choice.lower().strip() == "colour":
            print("\nI see you want to choose a colour...")
            users_gamble_valid = False
            while users_gamble_valid == False:
                users_gamble = input("\nPlease choose a colour, either red, black or green ")
                if users_gamble.lower().strip() != "green" and users_gamble.lower().strip() != "red" and users_gamble.lower().strip() != "black":
                    os.system('cls')
                    print("\nplease choose either green, red or black.") 
                    users_gamble_valid = False
                else:
                    users_gamble_valid = True
            print("\nYou have chosen colour",users_gamble,)
            print("Now it is time to bet!")
            users_bet_valid = False
            while users_bet_valid == False:
                users_bet = input("How much money do you want to bet? ")
                if int(users_bet) <= int(users_money):
                    users_bet_valid = True
                else:
                    os.system('cls')
                    print("Please bet a suitable amount!")
                    users_bet_valid = False
            print1by1("Time to spin!")
            time.sleep(1)
            spinning()
            print("\nYou span",secret_colour,)
            print("\nYou chose",users_gamble,)
            if str(secret_colour_choice) == str(users_gamble):
                print1by1("\nNo way! You got it.")
                users_money = (users_money - users_bet) + (users_bet * colour_multiplier)
                print("\nYou win:",(int(users_bet)*(colour_multiplier)),)
                print("\nNew Balance",users_money,)
                currently_playing_answer = input("\nPlay again? please type y or n ")
                if currently_playing_answer.lower().strip() == "y":
                    currently_playing = True
                else:
                    currently_plaing = False
            else:
                print("\nNice Try!")
                users_money = int(users_money) - int(users_bet)
                print("\nNew Balance",users_money,)
                currently_playing_answer = input("Play again? Please type y or n ")
                if currently_playing_answer.lower().strip() == "n":
                    currently_playing = False

rules()
currently_playing = True 
while users_money != 0 and currently_playing == True:
    os.system('cls')
    main_game()
if currently_playing == False:
    os.system('cls')
    print("thanks for playing. come back soon!")
if users_money == 0:
    os.system('cls')
    print("You got no money left! Come back soon!") 

time.sleep(100)

