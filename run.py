# Write your code to expect a terminal of 80 characters wide and 24 rows high
import time
from colorama import Fore, Back
from typewriter import typewriter
from banner import banner

SEC = 1
TXTCLR = Back.RED + Fore.WHITE
RESET = Back.RESET + Fore.RESET

def beginning():


def start():
    """This function is starting the game"""
    question1 = input("Would you like to start the game? (Y/N): ")
    if question1 == "N" or question1 == "n":
        print()
        typewriter(TXTCLR + "Go home coward! \n" + RESET)
    elif question1 == "Y" or question1 == "y":
        beginning()
    else:
        print(Fore.RED + "Invalid Entry, Wait for game to load again...\n" + Fore.RESET)
        time.sleep(SEC)
        banner()
        time.sleep(4)
        return start()


banner()
time.sleep(2)
start()

# typewriter("You were walking around and saw a cave\n" + Back.RESET)
