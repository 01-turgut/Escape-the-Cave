import time
from colorama import Fore, Back
from typewriter import typewriter
from banner import banner

SEC = 2
TXTCLR = Back.RED + Fore.WHITE
RST = Back.RESET


def beginning():
    """
    The initial function of this game.
    This will give the user the first interaction with the game.
    """
    print()
    print()
    typewriter(TXTCLR + "YOU ARE AMAZING!\n" + RST)
    typewriter(TXTCLR + "THIS CAVE IS NEAR HENRY'S HOUSE...\n" + RST)
    typewriter(TXTCLR + "HENRY WANTS TO DISCOVER THE CAVE\n" + RST)
    typewriter(TXTCLR + "AS FAR AS HE KNOWS THE CAVE HAS TWO ENTRANCE\n" + RST)
    typewriter(TXTCLR + "HENRY CANNOT FIND THE EXIT...\n" + RST)
    typewriter(TXTCLR + "HE IS LOST AND TIRED, PHONE NOT WORKING\n" + RST)
    typewriter(TXTCLR + "HE ALREADY CHECKED DOOR HE ENTERED...\n" + RST)
    typewriter(TXTCLR + "IT'S BLOCKED, HE DOESN'T KNOW HOW...\n" + RST)
    typewriter(TXTCLR + "HE SAW A NEW ROAD, THAT HE DIDN'T CHECK...\n" + RST)
    typewriter(TXTCLR + "HE STARTED WALKING TO FIND THE EXIT\n" + RST)
    typewriter(TXTCLR + "HE WALKED A LITTLE, SAW A NEW ROAD ON LEFT\n" + RST)
    typewriter(TXTCLR + "ROAD ON LEFT WAS LITTLE BRIGHTER\n" + RST)
    typewriter(TXTCLR + "HE HAS TO CHOOSE LEFT OR STRAIGHT\n" + RST)

    choice1 = input(TXTCLR + "LEFT OR STRAIGHT (L/S)" + RST)
    if choice1 == "s" or choice1 == "S":
        typewriter(TXTCLR + "ROAD WAS TO DARK...\n" + RST)
        typewriter(TXTCLR + "HENRY DIDN'T SEE THE WELL AND HE FELL...\n" + RST)
        typewriter(TXTCLR + "FILLED WITH ALLIGATORS... HE IS DEAD!\n" + RST)
        print(RST)
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
        typewriter(TXTCLR + "\n" + RST)


def start():

    """
    This function is the main function of the game.
    it starts and exits the game.
    It warns and restarts the game when used out of duty.
    """
    typewriter(TXTCLR + "THIS GAME IS ABOUT TEACHER HENRY!\n" + RST)
    typewriter(TXTCLR + "CAN YOU GET HIM OUT OF THE CAVE?\n" + RST)
    question1 = input("WOULD YOU LIKE TO HELP HENRY? (Y/N): ")
    if question1 == "N" or question1 == "n":
        print()
        typewriter(TXTCLR + "Go home coward! \n " + RST)
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
