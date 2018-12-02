import sys, time, os, random

number_multiplier = 36

def print1by1(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)

def rules():
    print1by1("Welcome to Roulette! \n")
    print1by1("These are the Rules: \n")
    print1by1("Using your chips, you can place bets on whether you think what's rolled will be even or odd \n")
    print1by1("You can bet on whether what rolled is black or red, or if you are feeling lucky green \n")
    print1by1("You can also bet on whether a specific number will be rolled \n")
    print1by1("Based on the odds of rolling, your money either doubles/triples... \n")

def spinning():
    displayed_spin = ["o", "O",]
    for m in range(0, 5):
        for i in range(0, 2):
            os.system('cls')
            print(displayed_spin[i], " ", displayed_spin[i], " ", displayed_spin[i])
            print("Spinning")
            time.sleep(0.5)

rules()
print1by1("So... Do you want to play Roulette? \n")
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
                print("\nPlease input a number in the given range.")
                users_gamble_valid = False
    print("\nYou have chosen number",users_gamble)
    print("Now it is time to bet!")
    users_bet_valid = False
    while users_bet_valid == False:
        users_bet = input("How much money do you want to bet?")
        if int(users_bet) < 0 or int(users_bet) > 10000:
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
    print1by1("\nYou win:",(int(users_bet)*(number_mulitplier)),)
else:
    print("\nNice Try!")
    time.sleep(100)
