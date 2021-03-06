import time
from colorama import Fore
from typewriter import typewriter
from banner import banner
from thanks import thank

SEC = 2
TXTCLR = Fore.GREEN  # Text color variable
RST = Fore.RESET  # Reset the text color variable
QCLR = Fore.RED  # Text color for inputs


def beginning():
    """
    This function tells the story that will enable the user,
    to take the first decision for the game,
    and includes how to act in possible decisions.
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

    quest1 = input(QCLR + "LEFT OR STRAIGHT (L/S)\n" + RST)

    if quest1.lower() == "s":
        typewriter(TXTCLR + "ROAD WAS TO DARK...\n" + RST)
        print()
        typewriter(TXTCLR + "HENRY DIDN'T SEE THE WELL AND HE FELL...\n" + RST)
        print()
        typewriter(TXTCLR + "FILLED WITH ALLIGATORS... HE IS DEAD!\n" + RST)
        print()
        print(Fore.BLUE + "TRY AGAIN! SAVE HENRY!" + Fore.RESET)
        time.sleep(SEC)
        banner()
        time.sleep(SEC)
        start()
    elif quest1.lower() == "l":
        cliff()
    else:
        print(Fore.BLUE + "Invalid Entry\n" + RST)
        print()
        print(Fore.BLUE + "Wait for the game to load" + Fore.RESET)
        print()
        print(Fore.BLUE + "Game will continue where you left off" + Fore.RESET)
        print()
        time.sleep(SEC)
        return beginning()


def cliff():

    """
    This function tells the story that will enable the user,
    to take the second decision for the game,
    and includes how to act in possible decisions.
    """
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
    typewriter(TXTCLR + "AFTER SOME TIME HE HEARD SOME NOISE..\n" + RST)
    print()
    typewriter(TXTCLR + "HE STARTED RUNNIG TOWARDS THE NOISE...\n" + RST)
    print()
    typewriter(TXTCLR + "HE CAME TO THE END OF THE ROAD...\n" + RST)
    print()
    typewriter(TXTCLR + "THERE IS LEFT TURN AND RIGHT TURN...\n" + RST)
    print()
    typewriter(TXTCLR + "NOISE COMES FROM RIGHT SIDE...\n" + RST)
    print()
    typewriter(TXTCLR + "HE IS SCARED, HE HAS TO CHOOSE...\n" + RST)
    print()
    quest2 = input(QCLR + "LEFT OR RIGHT (L/R)\n" + RST)
    if quest2.lower() == "r":
        typewriter(TXTCLR + "THE ROAD GETTING DARKER, WRONG EXIT...\n" + RST)
        typewriter(TXTCLR + "HENRY'S FEET SLIPPED DOWNHILL.\n" + RST)
        typewriter(TXTCLR + "FELL OFF THE CLIFF.\n" + RST)
        print()
        print(Fore.BLUE + "TRY AGAIN! SAVE HENRY!" + Fore.RESET)
        time.sleep(SEC)
        banner()
        time.sleep(SEC)
        start()
    elif quest2.lower() == "l":
        poison_room()
    else:
        print(Fore.BLUE + "Invalid Entry\n" + RST)
        print()
        print(Fore.BLUE + "Wait for the game to load" + Fore.RESET)
        print()
        print(Fore.BLUE + "Game will continue where you left off" + Fore.RESET)
        print()
        time.sleep(SEC)
        return cliff()


def poison_room():

    """
    This function tells the story that will enable the user,
    to take the third decision for the game,
    and includes how to act in possible decisions.
    """
    print()
    print()
    typewriter(TXTCLR + "ROAD GETS BRIGHTER...\n" + RST)
    print()
    typewriter(TXTCLR + "BIRD CHIRPS GOT LOUDER...\n" + RST)
    print()
    typewriter(TXTCLR + "HE SAW A ROOM WITH STONE DOOR...\n" + RST)
    print()
    typewriter(TXTCLR + "HE GOT CURIOUS...\n" + RST)
    print()
    quest3 = input(QCLR + "DO YOU WANT HENRY TO SEE THE ROOM?(Y/N)\n" + RST)
    if quest3.lower() == "y":
        print()
        typewriter(TXTCLR + "HENRY OPENS AND ENTERING THE ROOM..\n" + RST)
        print()
        typewriter(TXTCLR + "THE DOOR CLOSED...\n" + RST)
        print()
        typewriter(TXTCLR + "ROOM WAS FILLED WITH CYANURIC ACID...\n" + RST)
        print()
        typewriter(TXTCLR + "HENRY POISONED BY CYANURIC ACID...\n" + RST)
        print()
        print(Fore.BLUE + "TRY AGAIN! SAVE HENRY!" + Fore.RESET)
        time.sleep(SEC)
        banner()
        time.sleep(SEC)
        start()
    elif quest3.lower() == "n":
        no_exit()
    else:
        print(Fore.BLUE + "Invalid Entry\n" + RST)
        print()
        print(Fore.BLUE + "Wait for the game to load" + Fore.RESET)
        print()
        print(Fore.BLUE + "Game will continue where you left off" + Fore.RESET)
        print()
        time.sleep(SEC)
        return poison_room()


def no_exit():
    """
    This function tells the story that will enable the user,
    to take the last decision for the game,
    and includes how to act in possible decisions.
    """
    print()
    print()
    typewriter(TXTCLR + "HENRY HAS PASSED THE ROOM...\n" + RST)
    print()
    typewriter(TXTCLR + "THE ROAD IS GETTING BRIGHTER...\n" + RST)
    print()
    typewriter(TXTCLR + "HE REMEMBERED HE HAS WATER...\n" + RST)
    print()
    typewriter(TXTCLR + "HE REACHED HIS BACKPACK...\n" + RST)
    print()
    typewriter(TXTCLR + "DRANK SOME WATER...\n" + RST)
    print()
    typewriter(TXTCLR + "END OF THIS ROAD THERE WAS TWO ROADS...\n" + RST)
    print()
    quest4 = input(QCLR + "DO YOU WANT HENRY TO TURN RIGHT/LEFT?(R/L)\n" + RST)
    if quest4.lower() == "l":
        print()
        typewriter(TXTCLR + "HENRY COULDN'T FIND THE EXIT...\n" + RST)
        print()
        typewriter(TXTCLR + "HENRY STARVED TO DEATH...\n" + RST)
        print()
        print(Fore.BLUE + "TRY AGAIN! SAVE HENRY!" + Fore.RESET)
        time.sleep(SEC)
        banner()
        time.sleep(SEC)
        start()
    elif quest4.lower() == "r":
        print()
        typewriter(TXTCLR + "HENRY MADE IT...\n" + RST)
        print()
        typewriter(TXTCLR + "WITH YOUR HELP...\n" + RST)
        print()
        thank()
        print()
        time.sleep(3)
        banner()
        ply = input(QCLR + "Press 'P' to Play Again\n" + RST)
        if ply.lower() == "p":
            return start()
        else:
            print()
            print()
            print(QCLR + "Invalid Entry" + RST)
            return start()
    else:
        print(Fore.BLUE + "Invalid Entry\n" + RST)
        print()
        print(Fore.BLUE + "Wait for the game to load" + Fore.RESET)
        print()
        print(Fore.BLUE + "Game will continue where you left off" + Fore.RESET)
        print()
        time.sleep(SEC)
        return no_exit()


def start():

    """
    This function is the main function of the game.
    it starts and exits the game.
    It warns and restarts the game when used out of duty.
    """
    typewriter(TXTCLR + "THIS GAME IS ABOUT TEACHER HENRY!\n" + RST)
    print()
    typewriter(TXTCLR + "CAN YOU GET HIM OUT OF THE CAVE?\n" + RST)
    print()
    question = input(QCLR + "WOULD YOU LIKE TO HELP HENRY? (Y/N):\n " + RST)
    if question.lower() == "n":
        print()
        typewriter(TXTCLR + "Go home coward! \n " + RST)
        print()
        time.sleep(SEC)
        banner()
        ply = input(QCLR + "Press 'P' to restart the game\n" + RST)
        if ply.lower() == "p":
            return start()
        else:
            print()
            print()
            print(QCLR + "Invalid Entry" + RST)
            return start()
    elif question.lower() == "y":
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
