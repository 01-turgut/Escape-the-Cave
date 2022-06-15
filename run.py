import time
from colorama import Fore, Back
from typewriter import typewriter
from banner import banner

SEC = 2
TXTCLR = Fore.GREEN
RST = Fore.RESET


def beginning():
    """
    The initial function of this game.
    This will give the user the first interaction with the game.
    """
    print()
    print()
    typewriter(TXTCLR + "YOU ARE AMAZING!\n" + RST)
    print()
    typewriter(TXTCLR + "THIS CAVE IS NEAR HENRY'S HOUSE...\n" + RST)
    print()
    typewriter(TXTCLR + "HENRY WANTS TO DISCOVER THE CAVE\n" + RST)
    print()
    typewriter(TXTCLR + "AS FAR AS HE KNOWS THE CAVE HAS TWO ENTRANCE\n" + RST)
    print()
    typewriter(TXTCLR + "HENRY CANNOT FIND THE EXIT...\n" + RST)
    print()
    typewriter(TXTCLR + "HE IS LOST AND TIRED, PHONE NOT WORKING\n" + RST)
    print()
    typewriter(TXTCLR + "HE ALREADY CHECKED DOOR HE ENTERED...\n" + RST)
    print()
    typewriter(TXTCLR + "IT'S BLOCKED, HE DOESN'T KNOW HOW...\n" + RST)
    print()
    typewriter(TXTCLR + "HE SAW A NEW ROAD, THAT HE DIDN'T CHECK...\n" + RST)
    print()
    typewriter(TXTCLR + "HE STARTED WALKING TO FIND THE EXIT\n" + RST)
    print()
    typewriter(TXTCLR + "HE WALKED A LITTLE, SAW A NEW ROAD ON LEFT\n" + RST)
    print()
    typewriter(TXTCLR + "ROAD ON LEFT WAS LITTLE BRIGHTER\n" + RST)
    print()
    typewriter(TXTCLR + "HE HAS TO CHOOSE LEFT OR STRAIGHT\n" + RST)

    choice1 = input("LEFT OR STRAIGHT (L/S)\n")
    if choice1 == "s" or choice1 == "S":
        typewriter(TXTCLR + "ROAD WAS TO DARK...\n" + RST)
        typewriter(TXTCLR + "HENRY DIDN'T SEE THE WELL AND HE FELL...\n" + RST)
        typewriter(TXTCLR + "FILLED WITH ALLIGATORS... HE IS DEAD!\n" + RST)
        print()
        banner()
        time.sleep(SEC)
        start()
    
    elif choice1 == "l" or choice1 == "L":
        choice2()
    else:
        print(Fore.RED + "Invalid Entry\n" + RST)
        print(Fore.RED + "Wait for the load" + Fore.RESET)
        print(Fore.RED + "Game will continue where you left off" + Fore.RESET)
        print()
        time.sleep(SEC)
        return beginning()


def choice2():
    print()
    print()
    typewriter(TXTCLR + "THIS ROAD IS BRIGHT, BIRDS ARE TWEETING.\n" + RST)
    print()
    typewriter(TXTCLR + "HENRY HAS HOPE!\n" + RST)
    print()
    typewriter(TXTCLR + "HE IS TIRED, IT'S BEEN HOURS...\n" + RST)
    print()
    typewriter(TXTCLR + "HE WANTED TO SIT AND GET SOME REST...\n" + RST)
    print()
    typewriter(TXTCLR + "AFTER SOME TIME HE STARTED WALKING AGAIN...\n" + RST)
    print()


def start():

    """
    This function is the main function of the game.
    it starts and exits the game.
    It warns and restarts the game when used out of duty.
    """
    typewriter(TXTCLR + "THIS GAME IS ABOUT TEACHER HENRY!\n" + RST)
    typewriter(TXTCLR + "CAN YOU GET HIM OUT OF THE CAVE?\n" + RST)
    question1 = input("WOULD YOU LIKE TO HELP HENRY? (Y/N):Y\n ")
    if question1 == "N" or question1 == "n":
        print()
        typewriter(TXTCLR + "Go home coward! \n " + RST)
        print()
        time.sleep(SEC)
        banner()
        ply = input("Press 'P' to start the game\n")
        if ply == "p" or ply == "P":
            return start()
    elif question1 == "Y" or question1 == "y":
        beginning()
    else:
        print(Fore.RED + "Invalid Entry, Wait for game to load again!\n")
        print(Fore.RESET)
        time.sleep(SEC)
        banner()
        time.sleep(3)
        return start()


banner()
time.sleep(2)
start()
