import time
from pyfiglet import Figlet
from colorama import Fore


def thank():

    """This is function to print thank,
    to user playing the game(Saving Henry)"""

    custom_fig = Figlet(font="bubble")
    thanks = custom_fig.renderText("THANK YOU FOR SAVING HENRY!")
    time.sleep(0.5)
    print()
    print()
    print(Fore.GREEN + thanks + Fore.RESET)


thank()
