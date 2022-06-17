import time
from pyfiglet import Figlet
from colorama import Fore


def banner():
    """This is my function to print my banner using pyfiglet library"""
    custom_fig = Figlet(font="slant")
    logo = custom_fig.renderText("ESCAPE")
    logo2 = custom_fig.renderText("THE")
    logo3 = custom_fig.renderText("CAVE")

    custom_fig2 = Figlet(font="digital")
    welcome = custom_fig2.renderText("Welcome To Escape The Cave")

    print(Fore.BLUE + logo + Fore.RESET)
    time.sleep(0.5)
    print(Fore.BLUE + logo2 + Fore.RESET)
    time.sleep(0.5)
    print(Fore.BLUE + logo3 + Fore.RESET)
    time.sleep(2)
    print()
    print()
    print(Fore.GREEN + welcome + Fore.RESET)
